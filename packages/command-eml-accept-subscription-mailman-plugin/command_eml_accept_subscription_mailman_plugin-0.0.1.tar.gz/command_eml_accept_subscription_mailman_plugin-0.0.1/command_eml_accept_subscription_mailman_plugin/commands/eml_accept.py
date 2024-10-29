"""The 'accept' email command."""

from mailman.core.i18n import _
from mailman.interfaces.command import ContinueProcessing, IEmailCommand
from mailman.interfaces.member import (
    AlreadySubscribedError,
    MembershipIsBannedError,
)
from mailman.interfaces.pending import IPendings
from mailman.interfaces.subscriptions import ISubscriptionManager, TokenOwner
from mailman.rules.approved import Approved
from public import public
from zope.component import getUtility
from zope.interface import implementer
from mailman.model.pending import Pended, PendedKeyValue
from mailman.database.transaction import dbconnection
from sqlalchemy.orm import aliased
from sqlalchemy import and_
import json
from mailman.interfaces.pending import PendType


@public
@implementer(IEmailCommand)
class Accept:
    """The email 'accept' command."""

    name = 'accept'
    argument_description = 'token'
    description = _('Accept a subscription')
    short_description = description

    def process(self, mlist, msg, msgdata, arguments, results):
        """See `IEmailCommand`."""
        # The subscriber email must be in the arguments.
        if len(arguments) == 0:
            print(_('No subscriber email found'), file=results)
            return ContinueProcessing.no
        # Searching pending request for this subscription
        emailsubscriber = arguments[0]
        pendingSubscriber = self.queryPendingSubscriber(mlist=mlist, emailsubscriber=emailsubscriber).first()
        if pendingSubscriber is None:
            print(_('No pending subscription request found for this email'), file=results)
            return ContinueProcessing.no
        # Make sure we don't try to confirm the same token more than once.
        token = pendingSubscriber.token
        tokens = getattr(results, 'confirms', set())
        if token in tokens:
            # Do not try to confirm this one again.
            return ContinueProcessing.no
        tokens.add(token)
        results.confirms = tokens
        # now figure out what this token is for.
        pendable = getUtility(IPendings).confirm(token, expunge=False)
        if pendable is None:
            print(_('Confirmation token did not match'), file=results)
            results.send_response = True
            return ContinueProcessing.no
        # Is this confirmation approved?
        approved = Approved().check(mlist, msg, msgdata)
        if not approved:
            print(_('Invalid Approved: password'), file=results)
            return ContinueProcessing.no
        try:
            new_token, token_owner, member = ISubscriptionManager(
                mlist).confirm(token)
            if new_token is None:
                assert token_owner is TokenOwner.no_one, token_owner
                # We can't assert anything about member.  It will be None when
                # the workflow we're confirming is a subscription request,
                # and non-None when we're confirming an unsubscription request.
                # This class doesn't know which is happening.
                succeeded = True
            elif token_owner is TokenOwner.moderator:
                # This must have been a confirm-then-moderate (un)subscription.
                assert new_token != token
                # We can't assert anything about member for the above reason.
                succeeded = True
            else:
                assert token_owner is not TokenOwner.no_one, token_owner
                assert member is None, member
                succeeded = False
        except LookupError:
            # The token must not exist in the database.
            succeeded = False
        except (MembershipIsBannedError, AlreadySubscribedError) as e:
            print(str(e), file=results)
            return ContinueProcessing.no
        if succeeded:
            print(_('Confirmed'), file=results)
            # After the 'confirm' command, do not process any other commands in
            # the email.
            return ContinueProcessing.no
        print(_('Confirmation token did not match'), file=results)
        return ContinueProcessing.no

    @dbconnection
    def queryPendingSubscriber(
        self, store, mlist, emailsubscriber
    ):
        query = store.query(Pended)

        pkv_alias_mlist = aliased(PendedKeyValue)
        query = query.join(pkv_alias_mlist).filter(and_(
            pkv_alias_mlist.key == 'list_id',
            pkv_alias_mlist.value == json.dumps(mlist.list_id)
            ))

        pkv_alias_token_owner = aliased(PendedKeyValue)
        query = query.join(pkv_alias_token_owner).filter(and_(
            pkv_alias_token_owner.key == 'token_owner',
            pkv_alias_token_owner.value == json.dumps(TokenOwner.moderator.name)
            ))

        pkv_alias_type = aliased(PendedKeyValue)
        query = query.join(pkv_alias_type).filter(and_(
            pkv_alias_type.key == 'type',
            pkv_alias_type.value == PendType.subscription.name
            ))

        pkv_alias_email = aliased(PendedKeyValue)
        query = query.join(pkv_alias_email).filter(and_(
            pkv_alias_email.key == 'email',
            pkv_alias_email.value == json.dumps(emailsubscriber)
            ))

        return query
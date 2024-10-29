from public import public
from mailman.interfaces.plugin import IPlugin
from zope.interface import implementer


@public
@implementer(IPlugin)
class CommmandEmlAddMemberPlugin:
    def pre_hook(self):
        pass

    def post_hook(self):
        pass

    @property
    def resource(self):
        return None
    
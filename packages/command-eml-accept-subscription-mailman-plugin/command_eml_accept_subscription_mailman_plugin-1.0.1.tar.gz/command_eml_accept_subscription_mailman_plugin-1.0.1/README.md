# command-eml-accept-subscription-mailman-plugin

> Github repository : https://github.com/Tann-dev/command-eml-accept-subscription-mailman-plugin

This plugin provides a custom command to accept a member's subscription by email. To use this command, simply send an email to the address `list-request@domain.org` with the subject

`accept email@address.subscriber`.

In the body of the message, you must also provide the password for the mailing list, with the keyword `Approved:`. For example, 

`Approved: password`.

Please note that the member must request to join the list in order to be accepted onto the mailing list. If there is no current subscription request, the member will not be added to the mailing list.

## Install the plugin

### PIP

To install this package with pip, you can use the following command:

```
python3 -m pip install command-eml-accept-subscription-mailman-plugin
```

### Docker

If you want to use mailman with the `maxking/mailman-core` docker image [from this repository] (https://github.com/maxking/docker-mailman), you can take the `Dockerfile` from this repository, and modify it as you wish. You will also need the `requirements-docker.txt` file.

Or you can also use the `tannndev/mailman-with-plugin` docker image

## Activate the plugin in Mailman Core

In order to activate the plugin in Mailman Core, add the following config to
mailman.cfg:

```
# Plugin configuration.
[plugin.command_eml_accept_subscription_mailman_plugin]
class: command_eml_accept_subscription_mailman_plugin.CommmandEmlAcceptMemberPlugin
enabled: yes
```
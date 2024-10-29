# command-eml-accept-subscription-mailman-plugin

## Activate plugin in Mailman Core
In order to activate the plugin in Mailman Core, add the following config to
mailman.cfg:

```
# Plugin configuration.
[plugin.command_eml_accept_subscription_mailman_plugin]
class: command_eml_accept_subscription_mailman_plugin.CommmandEmlAddMemberPlugin
enabled: yes
```
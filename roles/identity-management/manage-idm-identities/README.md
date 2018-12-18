Manage IPA/IdM identities (users/groups)
========================================

An ansible role that manages IPA/IdM identities - users and groups.


Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**ipa_host**|The hostname/ip used to conmect to for IPA/IdM management|yes|N/A|
|**ipa_admin_user**|The IPA/IdM admin user with proper permissions to administer identities|yes|N/A|
|**ipa_admin_password**|The IPA/IdM admin password for the above mentioned admin user|yes|N/A|
|**ipa_validate_certs**|Whether to validate the IPA/IdM certificate|no|True|

In addition to the above mentioned variables, the role also requires an `identity` dictionary with a list of users and groups as documented in the [identity-management README](../README.md).


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

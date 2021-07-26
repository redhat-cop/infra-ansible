Remove IPA/IdM identities (users)
========================================

An ansible role that removes IPA/IdM identities (users).

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**ipa_host**|The hostname/ip used to connect to for IPA/IdM management|yes|N/A|
|**ipa_admin_user**|The IPA/IdM admin user with proper permissions to administer identities|yes|N/A|
|**ipa_admin_password**|The IPA/IdM admin password for the above mentioned admin user|yes|N/A|
|**ipa_validate_certs**|Whether to validate the IPA/IdM certificate|no|True|

In addition to the above mentioned variables, the role also requires an `identity` dictionary with a list of users and groups as documented in the [identity-management README](../README.md).

The role will keep track of the identities that have been removed for futher use in the following variables.

| Output | Description |
| :----- | :---------- |
| users_removed_success | List of users who were successfully removed as per the results of the API request to IPA. |
| users_removed_failed | List of users who failed to be removed, possibly due to an error in the API request to IPA. |
| users_removed_skipped | List of users who were skipped as they were not found in IPA.


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

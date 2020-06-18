Manage Red Hat Single Sign-on identities (users/groups)
=======================================================

An ansible role that manages Red Hat Single Sign-On identities - users and groups.


Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**id_mgmt_sso_host**|The hostname/ip used to conmect to for RH SSO management|yes|N/A|
|**sso_admin_user**|The RH SSO admin user with proper permissions to administer identities|yes|N/A|
|**sso_admin_pass**|The RH SSO admin password for the above mentioned admin user|yes|N/A|
|**user_name**|The username used by the user to authenticate|yes|N/A|
|**first_name**|The user's first name|no|N/A|
|**last_name**|The user's last name|no|N/A|
|**email**|The user's email address. It must be unique|no|N/A|
|**enabled**|Whether the user is active or not. Inactive users can't login|no|True|
|**email_verified**|Whether the user confirmed its email address|no|False|
|**user_groups**|A list of groups the user belongs to|no|N/A|

In addition to the above mentioned variables, the role also requires an `identity` dictionary with a list of users and groups as documented in the [identity-management README](../README.md).

If you don't have access to the server hosting Red Hat Single Sign-On, update the `identity-hosts` entry in the hosts file to use localhost, and move the variables from `identity-hosts.yml` to `all.yml`.

Using Tags
----------

This role currently supports the usage of four different tags:

- create-user: Specify this tag to create one or more users
- delete-user: Specify this tag to delete one or more users
- create-group: Specify this tag to create one or more groups
- delete-group: Specify this tag to delete one or more groups

All of tags will act upon the values defined in the `identity-hosts.yml` file.


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.


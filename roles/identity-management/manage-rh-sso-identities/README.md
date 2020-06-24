Manage Red Hat Single Sign-on identities (users/groups)
=======================================================

An ansible role that manages Red Hat Single Sign-On identities - users and groups.


Role Variables                                                                                                        
--------------

The following would represent a single account in a Red Hat Single Sign-On instance (e.g. `group_vars/identity-hosts.yml`)

```yaml
---                                                        

identities:
  targets:
    - rh-sso

  users:
    - user_name: example
      first_name: First
      last_name: Last
      email: user@example.com
      enabled: true
      email_verified: yes

  groups:
    - group_name: group-01
```

Variable Descriptions
---------------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**rh_sso_host**|The hostname/ip used to connect to for RH SSO management|yes|N/A|
|**rh_sso_port**|The port that RH SSO instance listens to|no|8080|
|**sso_admin_user**|The RH SSO admin user with proper permissions to administer identities|yes|N/A|
|**sso_admin_pass**|The RH SSO admin password for the above mentioned admin user|yes|N/A|

In addition to the above mentioned variables, the role also requires an `identity` dictionary with a list of users and groups as documented in the [identity-management README](../README.md).

If you don't have access to the server hosting Red Hat Single Sign-On, update the `identity-hosts` entry in the hosts file to use localhost, and move the variables from `identity-hosts.yml` to `all.yml`.


Using Tags
----------

This role currently supports the usage of two different tags:

- **create-user:** Specify this tag to create one or more users
- **delete-user:** Specify this tag to delete one or more users
- **create-group:** Specify this tag to create one or more groups
- **delete-group:** Specify this tag to delete one or more groups

All tags will act upon the values defined in the mandatory variables from the `identity-hosts.yml` file.


Requirements
------------

There are a few requirements for this role to function correctly. Please, make sure you read the information below before running the automation.

01. When creating a user, you may omit the `user_groups` variable, however, if it's specified, the group must exist.
02. When creating a user, although the e-mail address is optional, if specified, it must be unique.
03. When creating a user, make sure the username is unique, otherwise, the user will be **updated** with the information from `identity-hosts.yml` file.


Execution Example
-----------------

To create a user, run:
- `ansible-playbook playbooks/manage-identities/manage-rh-sso-identities.yml -i inventory/rh-sso/ --tags="create-user"`

To create a group, run:
- `ansible-playbook playbooks/manage-identities/manage-rh-sso-identities.yml -i inventory/rh-sso/ --tags="create-group"`


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.


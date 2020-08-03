Ansible Tower roles
====================

This directory contains various roles to install, configure and manage Ansible Tower.


Requirements
------------

- For Install: Access to the Ansible Tower software and an Ansible Tower license.
- For Management: Access to a running Ansible Tower with admin permissions.

Variables
---------
The following is a list of required variables for the Ansible Tower roles that are common to all of them.

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**ansible_tower.url**|URL for the Ansible Tower |yes||
|**ansible_tower.admin_user**|Admin user for the Ansible Tower |yes||
|**ansible_tower.admin_password**|Admin password for the Ansible Tower |yes||


Roles
-----

The following roles exists in this directory:

- [config-ansible-tower](config-ansible-tower) role used to install and do initial configuration of Ansible tower.
- [config-ansible-tower-ldap](config-ansible-tower-ldap) role used to configure Ansible Tower to use a LDAP backend for authentication.
- [config-ansible-tower-license](config-ansible-tower-license) role used to configure Ansible Tower licensing.
- [manage-credential-types](manage-credential-types) role used to manage and populate Ansible Tower Credential Types ("Settings >> Credential Types").
- [manage-credentials](manage-credentials) role used to manage and populate Ansible Tower Credentials ("Settings >> Credentials").
- [manage-inventories](manage-inventories) role used to manage and populate Ansible Tower Inventories ("Inventories").
- [manage-job-templates](manage-job-templates) role used to manage and populate Ansible Tower Job Templates ("Templates >> ADD >> Job Templates").
- [manage-projects](manage-projects) role used to manage and populate Ansible Tower Projects ("Projects").
- [manage-settings](manage-settings) role used to manage and configure Ansible Tower Settings ("Settings").
- [manage-workflow-templates](manage-workflow-templates) role used to manage and Ansible Tower WorkFlow templates. ("WorkFlow").


Example Inventory
-----------------

```yaml
---

ansible_tower:
  url: https://tower.example.com
  admin_user: 'admin'
  admin_password: 'password'
  install:
    : # see config-ansible-tower README for more details
  ldap:
    : # see config-ansible-tower-ldap README for more details
  license:
    : # see config-ansible-tower-license README for more details
  credential-types:
    : # see manage-credential-types README for more details
  credentials:
    : # see manage-credentials README for more details
  inventories:
    : # see manage-inventories README for more details
  job-templates:
    : # see manage-job-templates README for more details
  projects:
    : # see manage-projects README for more details
  settings:
    : # see manage-settings README for more details
  workflow-templates:
    : # see manage-workflow-templates README for more details
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

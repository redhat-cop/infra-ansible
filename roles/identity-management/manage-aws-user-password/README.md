Manage AWS User password
====================================

An Ansible role that manages AWS user's password

Role Variables
--------------

The following would represent a single account as an Ansible host (e.g., `host_vars/aws-profile-na-1.yml`)

```yaml
---

ansible_connection: local

identities:
  targets:
    - aws

  users:
    - user_name: admin-user
      first_name: First
      last_name: Last
      email: "admin@example.com"

  groups:
    - group_name: "admin-group"
      managed_policy_arn:
        - "arn:aws:iam::aws:policy/AdministratorAccess"
      members:
        - admin-user
```

Variable Descriptions
---------------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|targets|Target environment, (e.g., AWS IAM, IdM, etc)|yes|N/A|
|users|Each user must exist in a profiles.groups.members to be created in an account|yes|N/A|

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

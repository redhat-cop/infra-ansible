Manage AWS Identities (users/groups)
==========================================

An Ansible role that manages AWS identities - users and groups for multiple AWS profiles.

This role assumes that you have your [AWS Named Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) configured and the profile names match your account alias.

The email address is not related to the AWS IAM User but will be used to send a one-time password upon account creation. Since we are using named profiles, they will be notified with a sign-in link for "https://{{ profile_name}}.signin.aws.amazon.com/console"

Role Variables
--------------

```yaml
---

identities:
  targets:
    - aws

  users:
    - user_name: admin-user
      first_name: First
      last_name: Last
      email: "admin@example.com"
    - user_name: read-only-user
      first_name: First
      last_name: Last
      email: "read-only@example.com"

  profiles:
    - profile_name: aws-profile-na-1
      groups:
        - group_name: "view-group"
          managed_policy_arn:
            - "arn:aws:iam::aws:policy/ReadOnlyAccess"
            - "arn:aws:iam::aws:policy/IAMUserChangePassword"
          members:
          - read-only-user
        - group_name: "admin-group"
          managed_policy_arn:
            - "arn:aws:iam::aws:policy/AdministratorAccess"
          members:
            - admin-user
    - profile_name: aws-profile-emea-2
      groups:
        - group_name: "view-group"
          managed_policy_arn:
            - "arn:aws:iam::aws:policy/ReadOnlyAccess"
            - "arn:aws:iam::aws:policy/IAMUserChangePassword"
          members:
          - read-only-user
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
|targets|This will differentiate your inventory from other Identity Management inventories|yes|N/A|
|users|Each user must exist in a profiles.groups.members to be created in an account|yes|N/A|
|profiles|Define profile, with unique groups and members per profile|yes|N/A|

Sample Inventory
--------------



License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

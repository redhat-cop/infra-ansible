Manage AWS Identities (users/groups)
==========================================

An Ansible role that manages AWS identities - users and groups for multiple AWS profiles.

This role assumes that you have your [AWS Named Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) configured and the profile names match your account alias.

The email address is not related to the AWS IAM User but will be used to send a one-time password upon account creation. Since we are using named profiles, they will be notified with a sign-in link for:

https://{{ aws_profile }}.signin.aws.amazon.com/console

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
|targets|Target environment, (e.g., AWS IAM, IdM, etc)|yes|N/A|
|users|Each user must exist in a profiles.groups.members to be created in an account|yes|N/A|
|profiles|Define profile, with unique groups and members per profile|yes|N/A|

Example Notification
--------------------

```yaml
---

title: Login Info - Hooli AWS Account

body: |
  Hi {{ first_name }}, <br />
  Please use the following temporary password to access the Hooli AWS Account

  Username: **{{ user_name }}** <br />
  Temporary password: **{{ password }}**

  Login to the AWS Console at: https://{{ aws_profile }}.signin.aws.amazon.com/console

  You will be prompted to change your password on first login.

  Please reply to this e-mail if you have any questions.

  Regards <br />
  The Hooli Team
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

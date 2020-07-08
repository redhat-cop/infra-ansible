Manage AWS Identities (users/groups)
====================================

An Ansible role that manages AWS identities - users and groups for multiple AWS profiles.

This role assumes that you have your [AWS Named Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) configured and the profile names match your account alias.

The email address is not related to the AWS IAM User but will be used to send a one-time password upon account creation. Since we are using named profiles, they will be notified with a sign-in link for:

https://{{ aws_profile }}.signin.aws.amazon.com/console

Example Hosts File
------------------

The data has been structured to allow for a separation of multiple AWS accounts mapped to Ansible Host Vars and users created in [identity hosts] will maintain their separate user data when the [mail-host] notifications kick off. Just remember to set `ansible_connection: local` for these two groups since you will not be able to use `localhost` as your host and maintain data isolation.

```ini
[identity-hosts]
aws-profile-na-1
aws-profile-na-2
aws-profile-apac-1
aws-profile-emea-1
aws-profile-latam-1

[mail-host]
aws-profile-na-1
aws-profile-na-2
aws-profile-apac-1
aws-profile-emea-1
aws-profile-latam-1
```

Role Variables
--------------

The following would represent a single account as an Ansible host (e.g., `host_vars/aws-profile-na-1.yml`)

```yaml
---

ansible_connection: local

identities:
  targets:
    - aws

  profile_name: aws-profile-na-1

  users:
    - user_name: admin-user
      first_name: First
      last_name: Last
      email: "admin@example.com"
      access_key_state: create
      key_count: 2
    - user_name: read-only-user
      first_name: First
      last_name: Last
      email: "read-only@example.com"

  policies:
    - policy_name: CustomManagedPolicy
      policy_description: "Describe your custom managed policy"
      policy:
        Version: '2012-10-17'
        Statement:
          - Action: s3:Get*
            Effect: Allow
            Resource: "*"
          - Action: sns:Publish
            Effect: Allow
            Resource: "*"

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
    - group_name: "custom-group"
      managed_policy_arn:
        - "CustomManagedPolicy"
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

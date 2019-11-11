htpasswd-from-dict
==================

Create a htpasswd file based on a dictionary list

Requirements
------------

This module will require passlib to be installed

Role Variables
--------------

| Name | Description | Default | Required |
| ---- | ----------- | ------- | -------- |
| htpasswd_output_path | Where to write the htpasswd file | /tmp/htpasswd | no |
| htpasswd_users | List of usernames & passwords| [] | no |

Example Playbook
----------------

Including an example of how to use your role
```
---
- hosts: localhost
  roles:
    - identity-management/htpasswd-from-dict
  vars:
    htpasswd_output_path: /var/www/htpasswd
    htpasswd_users:
      - username: user1
        password: password1
      - username: user2
        password: password2
```

License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

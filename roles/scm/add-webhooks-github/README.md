Add Webhooks github.com
=======================

Add webhooks to an existing repository on Github


Role Variables
--------------

```
---
api_token: 1234567890abcdefghijklmnopqrstuvwxyz9876

owner: aGithubUser

repo: aRepo

webhooks:
  - url: "https://website1.com/"
    events: 
      - push
    is_active: true
```

Also checkout [this file](tests/inventory/group_vars/all.yml)!

Example Playbook
----------------

```
---
- hosts: webhooks-server
  roles:
    - add-webhooks-github

```

Also checkout [this file](tests/test.yml)!

License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

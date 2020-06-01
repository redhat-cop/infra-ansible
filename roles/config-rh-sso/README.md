Role Name
=========

This deploys RH SSO in Standalone mode without a database.

## Requirements
Active Red Hat Subscription to enable repositories and download the SSO package group.

## Dependencies
None


### Example Playbook
```
- hosts: rh-sso-hosts
  become: yes

  roles:
    - config-rh-sso

```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

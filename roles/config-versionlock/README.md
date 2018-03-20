Role Name
=========

This role allows the system to be configured with versionlock'ed packages.

Requirements
------------

Proper repos available for the `versionlock` package.

Role Variables
--------------

- versionlock_packages : a list of packages to lock, e.g.:

```
versionlock_packages:
  - 'docker-1.12.6'
  - 'chrony-3.1-2'
  - 'bash-*'

```

Dependencies
------------

N/A

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: config-versionlock

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

Role Name
=========

This role allow users to add or remove a floating IP to an instance.

Requirements
------------

1. A valid OpenStack RC file, with the proper access rights to an OpenStack tenant, needs to be sourced before using this role.
1. The `openstack` python shade packages to allow for interactions with the platform.


Role Variables
--------------

See `Example Inventory` below for more specific details. At a high level, the following variables need to be defined:

- `osp_floating_ips`: A list of floating ip's to create

Dependencies
------------

None


Example Playbook
----------------

```
    - hosts: servers
      roles:
      - role: osp_floating_ips
```

**Note:** Make sure to source the OpenStack RC file (with proper access rights) before running this playbook/role.

Example Inventory
----------------

```
osp_floating_ips:
- server: "server1"
```


License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

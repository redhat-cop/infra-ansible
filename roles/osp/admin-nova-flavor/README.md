Role Name
=========

This role allow users to add nova flavors to OpenStack.

Requirements
------------

2 Requirements:

1. A valid OpenStack RC file, with the proper access rights to an OpenStack tenant, needs to be sourced before using this role.
1. The `openstack` binary, compatible with the target OpenStack environment, is accessible part of your path.


Role Variables
--------------

See `Example Inventory` below for more specific details. 

The following inventory variable is required:
- `osp_custom_flavors`: A list of flavors to manage


Dependencies
------------

None


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
    - hosts: servers
      roles:
      - role: admin-nova-flavor
```

**Note:** Make sure to source the OpenStack RC file (with proper access rights) before running this playbook/role.

Example Inventory
----------------

```
osp_custom_flavors:
- name: "m1.tiny"
  ram: 512
  disk: 10
  vcpus: 1
```


License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

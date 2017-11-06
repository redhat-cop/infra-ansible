Role Name
=========

This role allow users to automate the creation of their OpenStack Platform (OSP) volumes (cinder). 

Requirements
------------

1. A valid OpenStack RC file, with the proper access rights to an OpenStack tenant, needs to be sourced before using this role.
1. The `openstack` python shade packages to allow for interactions with the platform.


Role Variables
--------------

See `Example Inventory` below for more specific details. At a high level, the following variables need to be defined:

- `osp_volumes`: A list of volumes to create

Dependencies
------------

None


Example Playbook
----------------

```
    - hosts: servers
      roles:
      - role: osp-admin-volume
```

**Note:** Make sure to source the OpenStack RC file (with proper access rights) before running this playbook/role.

Example Inventory
----------------

```
osp_volumes:
- name: "vol1"
  display_description: "Volume 1"
  display_name: "Vol1"
  size: 5
- name: "vol2"
  display_description: "Volume 2"
  display_name: "Vol2"
  size: 15

```


License
-------

BSD

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

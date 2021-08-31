Role Name
=========

This role allow users to add or remove a images in OpenStack

Requirements
------------

1. A valid OpenStack RC file, with the proper access rights to an OpenStack tenant, needs to be sourced before using this role.
1. The `openstack` python shade packages to allow for interactions with the platform.


Role Variables
--------------

See `Example Inventory` below for more specific details. At a high level, the following variables need to be defined:

- `osp_images`: A list of images to add

Dependencies
------------

None


Example Playbook
----------------

```
    - hosts: servers
      roles:
      - role: admin-image
```

**Note:** Make sure to source the OpenStack RC file (with proper access rights) before running this playbook/role.

Example Inventory
----------------

```
osp_images:
- filename: "/the/path/to/my/image.qcow2"
  disk_format: qcow2
  is_public: yes
  name: my-image
```


License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

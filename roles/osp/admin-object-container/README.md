Role Name
=========

This role allow users to automate the creation of their OpenStack Platform (OSP) Object Containers (swift) with content

Requirements
------------

1. A valid OpenStack RC file, with the proper access rights to an OpenStack tenant, needs to be sourced before using this role.
1. The `openstack` python shade packages to allow for interactions with the platform.

Role Variables
--------------

See `Example Inventory` below for more specific details. The following variable needs to be defined:

- `osp_container_objects`: A list of files to create in object container(s)


Dependencies
------------

* A valid OSP tenant with the proper configuration 
  * User or service account used to manage content needs to have the 'swiftoperator' role assigned


Example Playbook
----------------

```
- hosts: servers
  roles:
  - role: osp/admin-object-container
```

**Note:** Make sure to source the OpenStack RC file (with proper access rights) before running this playbook/role.

Example Inventory
----------------

```
osp_container_objects:
  - name: "test-file-1.txt"
    container: "my-test-container
    container_access: "public"
    filename: "{{ inventory_dir }}/../files/test-file-1.txt"
  - name: "test-file-2.txt"
    container: "my-test-container
    container_access: "public"
    filename: "{{ inventory_dir }}/../files/test-file-2.txt"
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

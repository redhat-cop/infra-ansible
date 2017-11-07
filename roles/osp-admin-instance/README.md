Role Name
=========

This role allow users to automate the creation of their OpenStack Platform (OSP) instances based on their pre-defined inventory (see example below). 

Requirements
------------

1. A valid OpenStack RC file, with the proper access rights to an OpenStack tenant, needs to be sourced before using this role.
1. The `openstack` python shade packages to allow for interactions with the platform.

Role Variables
--------------

See `Example Inventory` below for more specific details. The following variable needs to be defined:

- `osp_instances`: A list of instances to create


Dependencies
------------

* A valid OSP tenant with the proper configuration for:
  * Network (can be done with the `osp-admin-network` role)
  * Security Groups (can be done with the `osp-admin-sec-group` role)
  * Volumes (can be done with the `osp-admin-volume` role) 


Example Playbook
----------------

``` 
- hosts: servers
  roles:
  - role: osp-admin-instance
```

**Note:** Make sure to source the OpenStack RC file (with proper access rights) before running this playbook/role.

Example Inventory
----------------

```
osp_instances:
- name: "host1"
  meta:
    group: my-instances
  image: "Fedora-Cloud-Base-26-1.5.x86_64"
  key_name: "my_keypair"
  flavor: "m1.medium"
  network: "my-network"
  security_groups:
  - my_sec_group
  auto_ip: False
  volumes:
  - vol1
- name: "host2"
  meta:
    group: my-instances
  image: "CentOS-7-x86_64"
  key_name: "my_keypair"
  flavor: "m1.small"
  network: "my-network"
  security_groups:
  - icmp_group
  - ssh_group
  volumes:
  - vol1
  - vol2
- name: "host3"
  state: "absent"
  delete_fip: True

```


License
-------

BSD


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.


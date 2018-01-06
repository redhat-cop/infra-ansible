Role Name
=========

This role allow users to automatically create their OpenStack Platform (OSP) Networking - i.e.: network, subnets, and routers - based on their pre-defined inventory.

Requirements
------------

2 Requirements:

1. A valid OpenStack RC file, with the proper access rights to an OpenStack tenant, needs to be sourced before using this role.
1. The `openstack` binary, compatible with the target OpenStack environment, is accessible part of your path.


Role Variables
--------------

See `Example Inventory` below for more specific details. At a high level, the following variables need to be defined:

- `osp_networks`: A list of networks to create
- `osp_subnets`: A list of subnets to be created with the above network(s)
- `osp_routers`: A list of routers to be created with the above subnet(s)


Dependencies
------------

None


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
    - hosts: servers
      roles:
      - role: osp-admin-network
```

**Note:** Make sure to source the OpenStack RC file (with proper access rights) before running this playbook/role.

Example Inventory
----------------

```
osp_networks:
- name: "my-network"
  description: "My Network"

osp_subnets:
- name: "my-subnet"
  network_name: "my-network"
  allocation_pool_start: "192.168.10.2"
  allocation_pool_end: "192.168.10.254"
  dns_nameservers:
  - "192.168.1.11"
  - "192.168.1.12"
  cidr: "192.168.10.0/24"
  gateway_ip: "192.168.10.1"

osp_routers:  
- name: "my-router"
  external_gateway: "external"
  subnet: "my-subnet"


```


License
-------

BSD

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

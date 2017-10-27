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
      - role: osp-admin-sec-group
```

**Note:** Make sure to source the OpenStack RC file (with proper access rights) before running this playbook/role.

Example Inventory
----------------

```
osp_security_groups:
- name: "my-sec-group"
  description: "My Security Group"
  rules:
  - protocol: tcp
    port_range_min: 80
    port_range_max: 80
    direction: ingress
    remote_ip_prefix: 0.0.0.0/0 
  - protocol: tcp
    port_range_min: 22
    port_range_max: 22
    direction: ingress
    remote_ip_prefix: 192.168.10.0/24
- name: "icmp-group"
  description: "ICMP Security Group"
  rules:
  - protocol: icmp
    direction: ingress
    remote_ip_prefix: 0.0.0.0/0 

```


License
-------

BSD

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

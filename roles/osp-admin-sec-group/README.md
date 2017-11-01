Role Name
=========

This role allow users to automate the creation of their OpenStack Platform (OSP) secrurity groups (with corresponding security rules). 

Requirements
------------

1. A valid OpenStack RC file, with the proper access rights to an OpenStack tenant, needs to be sourced before using this role.
1. The `openstack` python shade packages to allow for interactions with the platform.



Role Variables
--------------

See `Example Inventory` below for more specific details. At a high level, the following variable needs to be defined:

- `osp_security_groups`: A list of security groups, with rules, to create


Dependencies
------------

None


Example Playbook
----------------

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

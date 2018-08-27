Set of Roles
============

The ansible roles found in this directory are associated with prepping for a vLAN (virtual LAN) install and configuring a vLAN install. VLANs allow for creating virtual area networks to avoid the costly process of buying and configuring new expensive routers for what may be a temporary measure.

The role is relatively straightforward:  it configures the vLANS interfaces and brings them online.

Requirements
------------

None beyond ansible.

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**ifcfg.device**| the home directory where all the VNC files live | yes | ``` /home/ ``` |

Dependencies
------------
No software dependencies that aren't taken care of by the ```/roles/prereq.yml```

Example Playbooks
----------------

```
---

- name: 'Configure VLANs on the infrastructure hosts'
  hosts: infra_hosts
  roles:
  - role: config_vlans
  tags:
  - configure_infra_hosts
```

Example Inventory
----------------
**hosts:**
```
[all:vars]

[infra_hosts]
infra-1.example.com ansible_user=root ansible_host=192.168.1.11
infra-2.example.com ansible_user=root ansible_host=192.168.1.12
```
**host_vars/infra-1.example.com**
```
---

mgmt_net_ip: '192.168.1.11'
mgmt_net_netmask: '255.255.255.0'
mgmt_net_gateway: '192.168.1.1'
mgmt_net_dns1: '8.8.8.8'
mgmt_net_dns2: '8.8.4.4'
```

**host_vars/infra-2.example.com**
```
---

mgmt_net_ip: '192.168.1.12'
mgmt_net_netmask: '255.255.255.0'
mgmt_net_gateway: '192.168.1.1'
mgmt_net_dns1: '8.8.8.8'
mgmt_net_dns2: '8.8.4.4'
```

**group_vars/infra-hosts.yml**
```
---

vlans:
- device: tenant.vlan11
  physdev: eth0
  vlan_id: 11
- device: tenant.vlan12
  physdev: eth0
  vlan_id: 12
- device: tenant.vlan13
  physdev: eth0
  vlan_id: 13
```
License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

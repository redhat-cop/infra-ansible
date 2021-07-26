config-bonding
==============

name: config-bonding
The purpose of this role is to create network bonds on systems interfaces. 

Requirements
------------

None

Variables
---------

Defaults file has example of variables that can be used. It is advisable to create the following vars.

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**mgmt_net_ip**|  Management ip address | yes | N/A |
|**mgmt_net_netmask**| Management netmask | yes | N/A |
|**mgmt_net_gateway**| Management gateway | yes | N/A |
|**mgmt_net_dns1**| Management dns server | yes | N/A |
|**mgmt_net_dns2**| Management dns server | yes | N/A |

Example Playbook
----------------

```
    - name: 'Configure bonding on the infrastructure hosts'
      hosts: infra_hosts
      roles:
        - role: config_bonding
      tags: 
       - configure_infra_hosts
```

Example Inventory
-----------------
inventory/hosts:

```
[ha-nodes]
192.168.122.10

```
inventory/group_vars/ha-nodes.yml

```
---
bonds:
- device: bond0.mgmt
  bonding_opts: 'mode=4 miimon=100'
  slaves: 
  - device: eth0
  - device: eth1
  ipaddr: '{{ mgmt_net_ip }}'
  netmask: '{{ mgmt_net_netmask }}'
  gateway: '{{ mgmt_net_gateway }}'
  dns1: '{{ mgmt_net_dns1 }}'
  dns2: '{{ mgmt_net_dns2 }}'
- device: bond1.vms
  bonding_opts: 'mode=4 miimon=100'
  slaves:
  - device: eth2
  - device: eth3
```

License
-------
Apache License 2.0

Author Information
------------------
Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

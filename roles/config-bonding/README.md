config-bonding
==============

name: config-bonding
The purpose of this role is to create network bonds on systems interfaces. 

Requirements
------------

None

Variables
------------------

Defaults file has example of variables that can be used. It is advisable to create the following vars.

```
# Variables to set
mgmt_net_ip:
mgmt_net_netmask:
mgmt_net_gateway:
mgmt_net_dns1:
mgmt_net_dns2:

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
Example Playbook
----------------
    - name: 'Configure bonding on the infrastructure hosts'
      hosts: infra_hosts
      roles:
        - role: config_bonding
      tags: 
       - configure_infra_hosts


License
-------

MIT


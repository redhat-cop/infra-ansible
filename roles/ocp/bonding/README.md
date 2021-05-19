bonding
=========

This role will create machine config files to setup ethernet bonding on cluster nodes. This can easily be modified to directly apply these machine configs, however it is often preferred to add these machine configs at install time so writing to a file for injecting into install manifests was the goal here.

Requirements
------------

- Appropriate variables setup in playbook
- A configuration file to pass with bonding settings


Role Variables
--------------

See `Example Playbook` below for more specific details on global vars. At a high level, the following variables need to be defined:

- **Passed as extra var or environment variable**
  - `config`: The json config file that holds the bonding details
  - `destination`: Where to create the machine config files (-e destination=./out)
  - `type`: [OPTIONAL] The type of node to create machine configs for, default is all

**NOTE:** Type corresponds to the parent keys in the config file passed. (master, worker, etc...)

Dependencies
------------

The following python modules are required:

```
Jinja2
```


Example config file
-------------------

```
{
  "master": {
    "block_storage_vlan_parent_iface": "bond0",
    "block_storage_vlan_id": "1305",
    "block_storage_mtu": "9000",
    "bonding": {
        "bond-0": {
          "name": "bond0",
          "interfaces": "ens1f0,ens1f1",
          "bootproto": "dhcp",
          "mtu": "1500",
          "options": "mode=802.3ad,miimon=500"
      },
      "bond-1": {
          "name": "bond1",
          "interfaces": "ens3f0,ens3f1",
          "mtu": "9000",
          "bootproto": "dhcp",
          "options": "mode=active-backup,miimon=100,updelay=500,downdelay=1000,arp_interval=500,primary=ens1f0"
      }
    }
  },
  "worker": {
    "block_storage_vlan_parent_iface": "bond0",
    "block_storage_vlan_id": "1305",
    "block_storage_mtu": "9000",
    "bonding": {
        "bond-0": {
          "name": "bond0",
          "interfaces": "ens1f0,ens1f1",
          "bootproto": "dhcp",
          "mtu": "1500",
          "options": "mode=802.3ad,miimon=500"
      },
      "bond-1": {
          "name": "bond1",
          "interfaces": "ens3f0,ens3f1",
          "mtu": "9000",
          "bootproto": "dhcp",
          "options": "mode=active-backup,miimon=100,updelay=500,downdelay=1000,arp_interval=500,primary=ens1f0"
      }
    }
  }
}
```

Example Playbook
----------------

```
---
- hosts: localhost
  tasks:
  - name: Set do_all var if type is not set
    set_fact:
      do_all: true
    when: type is not defined

  - name: Fail if config is undefined
    fail:
      msg: "You need to define a config file with -e 'config=<json file>' to run this playbook."
    failed_when: config is not defined

  - name: Fail if destination is undefined
    fail:
      msg: "You need to define destination with -e 'destination=<path to generate files>' to run this playbook."
    failed_when: destination is not defined

  - name: Create single node type bonding config
    include_role:
        name: bonding
    when: type is defined

  - name: Create all node type bonding configs
    include_role:
      name: bonding
    vars:
      jsonconf: "{{lookup('file', config)}}"
      type: "{{line_item}}"
    with_items: "{{ jsonconf.keys()|list }}"
    loop_control:
      loop_var: line_item
    when: do_all is defined
```

**Note:** The playbook must define all required variables before running this playbook


License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

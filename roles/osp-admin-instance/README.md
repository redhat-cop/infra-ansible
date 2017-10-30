Role Name
=========


Requirements
------------


Role Variables
--------------


Dependencies
------------


Example Playbook
----------------



Example Inventory
----------------

```
osp_instances:
- name: "host1"
  meta:
  - group: my-instances
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
  - group: my-instances
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


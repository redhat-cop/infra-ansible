Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }



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
  image: "CentOS...."
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


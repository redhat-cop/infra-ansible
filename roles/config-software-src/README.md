Set of Roles
============

The ansible roles found in this directory are associated with configuring a software source to be shared across a network. First the role will prep the system by ensuring that a NFS package is installed, used for sharing file systems across a network. Then it simply mounts the software to the disk to create the connection. NOTE: it is not unmounted because it is supposed to be used as a form of persistent storage across the network.

Requirements
------------

No specific system requirements.

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**iso_repo_dir**| Local ISO storage repository | no | N/A |
|**iso_repo_nfs**| N/A |


Dependencies
------------
There are no strict dependencies for this role beyond ansible.

Example Playbooks
----------------
from ```/tests/test.yml```

```
- hosts: all
  roles:
    - config-software-src
```

Example Inventory
----------------


```
[all:vars]

iso_repo_dir: /dev/ISO/path
iso_repo_nfs: /dev/ISO/new/path
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

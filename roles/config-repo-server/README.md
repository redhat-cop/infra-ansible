Set of Roles
============

The ansible roles found in this directory are associated with mounting an ISO. It, first, ensures that the ISO mount directory exists and, second, mounts the ISOs.

Requirements
------------

No specific system requirements.

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**iso_repo_nfs**|  The NFS directory for ISOs | yes | N/A |
|**iso_repo_dir**| Local directory for ISO storage | yes |  |
|**iso_file_path**|  Local directory where the ISO is stored | yes | N/A |
|**iso_file_target**| The target directory to mount the ISO on | yes | |


Dependencies
------------
This role uses NFS to mount the repo, so make sure to specify a valid NFS server / path to where the ISOs can be found. This also relies on the role ```config-httpd```.

Example Playbooks
----------------
from ```tests/test.yml```

```
---

- hosts: repo_server
  roles:
    - config-repo-server
```

Example Inventory
----------------

```
[all:vars]

iso_repo_nfs: "my-nfs-server:/software"
iso_repo_dir: "/mnt/software"

hosted_isos:
- name: "fedora25-server"
  iso_file_path: "/mnt/software/ISOs/Fedora-Server-dvd-x86_64-25-1.3.iso"
  iso_file_target: "/var/www/html/fedora/25/server/x86_64"

[repo-server]
192.168.1.10
ansible_user: fedora
ansible_become: True
```



License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

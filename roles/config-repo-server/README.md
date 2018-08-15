Set of Roles
============

The ansible roles found in this directory are associated with configuring a httpd web server. It is broken into two steps, prep and seeding. In prep it sets up httpd and firewalld (opening it up on port 80). In seed it fills up the web server with content from a pre-determined location.

Requirements
------------

No specific system requirements.

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**httpd_seed_dir**|  Local directory with webserver content used to seed the web server | no | N/A |
|**html_document_root**| sets the default root folder for the where to deposit the web files that have been retrieved. | no | /var/www/html/ |


Dependencies
------------
This role uses NFS to mount the repo, so make sure to specify a valid NFS server / path to where the ISOs can be found.

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

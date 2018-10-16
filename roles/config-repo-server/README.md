config-repo-server
==================

This role takes a list of (local) ISO images paired with target directories and mounts the ISO at the directory location - with the purpose of host the ISOs as web content (e.g.: for PXE/ks installs, etc.)


Requirements
------------

- The [config-httpd](../config-httpd) role is used to ensure a valid web server is running before the ISOs are mounted and served.
- The ISO image(s) to be mounted needs to exist on the target host(s) (either locally or through another mounted file system).

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|iso_file_path| Path to the local ISO to be mounted | yes | |
|iso_file_target| The target directory to mount the ISO on | yes | |


Dependencies
------------



Example Playbooks
----------------

```
---

- hosts: repo-server
  roles:
  - config-repo-server
```

Example Inventory
----------------

**inventory/hosts**
```
[repo-server]
192.168.1.10
```

**inventory/repo-server**
```
hosted_isos:
- name: "fedora27-server"
  iso_file_path: "/mnt/software/ISOs/Fedora-Server-dvd-x86_64-27-1.3.iso"
  iso_file_target: "/var/www/html/fedora/27/server/x86_64"
- name: "fedora28-server"
  iso_file_path: "/mnt/software/ISOs/Fedora-Server-dvd-x86_64-28-1.1.iso"
  iso_file_target: "/var/www/html/fedora/28/server/x86_64"
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

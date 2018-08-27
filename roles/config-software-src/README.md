config-software-src
===================

This role mounts a NFS mount (`server:/directory`) to be used locally on the target host(s).

Requirements
------------

A valid NFS server with a directory already shared out.


Role Variables
--------------

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|**iso_repo_nfs**| The NFS server path/directory to be mounted | yes | |
|**iso_repo_dir**| Path to where the NFS target is to be mounted on the target host(s) | yes | |


Dependencies
------------

A valid NFS server with a directory already shared out.


Example Playbooks
----------------

```
- hosts: repo_servers
  roles:
  - config-software-src
```

Example Inventory
----------------

**inventory/hosts**
```
[repo_servers]
192.168.10.12
```


**inventory/group_vars/repo_servers**

```
iso_repo_nfs: "nfs.server.example.com:/software"
iso_repo_dir: "/mnt/software"

```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

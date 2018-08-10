Set of Roles
============
The ansible roles found in this directory are associated with configuring a pxe, or pre execution environment. First, it installs sys-linux, tftp-server, and firewall, then it makes sure that firewalld is running with port 69 is open and that the tftp-server is running. After the basic prep work is done, the next step is to ensure that the basic directories are set up and then to populate them, then the necessary system specific defaults are set. Kickstart files are then copied over.

Requirements
------------
Nothing is required. However, this playbook will work best on a RHEL OS.

Role Variables
--------------

```
docker_username: root
docker_install: True
```

Dependencies
------------
There are no strict dependencies for this role beyond ansible.

Example Playbooks
----------------

```
- hosts: bastion
  roles:
    - role: config-docker
```

Example Inventory
----------------

```
docker_install: True
docker_username: bob
```

License
-------
Apache License 2.0

Author Information
------------------
Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

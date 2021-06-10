config-crc-server
=========

Ansible role that installs CodeReady Containers server.

Requirements
------------

This role has the following requirements:
    - Access to the URL to download the CodeReady Containers CLI release
    - KVM, QEMU Libvirtd pre-installed

Role Variables
--------------

Default variables and descriptions are available in `defaults/main.yml`.

Dependencies
------------

No external dependencies.

Example Playbook
----------------

```yaml
- name: Provision CRC Servers
  hosts: crc_servers
  roles:
    - role: config-crc-server
```

License
-------

Apache 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

config-crc-client
=========

Ansible role that installs CodeReady Containers client.

Requirements
------------

This role has the following requirements:
    - Access to the URL to download the OpenShift CLI release

Role Variables
--------------

Default variables and descriptions are available in `defaults/main.yml`.

Dependencies
------------

No external dependencies.

Example Playbook
----------------

```yaml
- name: Provision CRC Clients
  hosts: crc_clients
  roles:
    - role: config-crc-client
```

License
-------

Apache 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

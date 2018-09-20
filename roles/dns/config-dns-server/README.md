Role Name: config-dns-server
=========

This role installs and configures a DNS server. The following technologies are supported:

  - named


Requirements
------------


Role Variables
--------------

The following dictionary is expected:

  - named_config: This dictionary will be used to ensure the DNS server is properly configured.

> **Note:** This role does **not** configure any views/zones - please use the `manage-dns-zones` for this purpose.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: dns-servers
  role: config-dns-server
```

Example Inventory
----------------

See README one level up.


License
-------

Apache License 2.0


Author Information
------------------

This role has be created by the Red Hat Containers & PaaS Community of Practice

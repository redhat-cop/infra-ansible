config-dns-server
=================

This role installs and configures a DNS server. The following technologies are supported:

  - named


Requirements
------------


Role Variables
--------------

The following dictionary is expected:

  - dns_data.named_global_config: This dictionary will be used to ensure the DNS server is properly configured. See README one level up for more details.

> **Note:** This role does **not** configure any views/zones - please use the [manage-dns-zones](../manage-dns-zones) role for this purpose.


Example Playbook
----------------

```
- hosts: dns-servers
  roles:
  - role: dns/config-dns-server
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

Role Name: config-dns-server
=========

This role installs and configures a DNS server with multiple views and zones.

  - named


Requirements
------------


Role Variables
--------------

The following dictionary is expected:

  - dns_data: This list with the nested dictionaries will be used to ensure the DNS server is properly configured and set up for use with the remaining data in this dictionary.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: servers
  role: config-dns-server
```

Example Inventory
----------------

Please see the example inventory [at the top level of this repo](../../inventory/dns-server)


License
-------

BSD

Author Information
------------------

This role has be created by the Red Hat Containers & PaaS Community of Practice

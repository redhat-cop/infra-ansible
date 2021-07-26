Role Name
=========

This role can be used to manage views and zones for named (bind).


Requirements
------------

The following packages are required:

  - python >= 2.6
  - boto

Role Variables
--------------

A dictionary, `dns_data`, with the following variables is expected:

  - named_global_config: if `named` is used, this will be the global configuration for the named/bind server.
  - views: List with views to configure as part of the DNS server/service.
    - name: Name of the view
    - zones: List of Hosted Zones
      - dns_domain: The Domain Name for the Hosted Zone
  - state: The desired state, present or absent






Example Playbook
----------------

```
- hosts: servers
  roles:
    - role: manage-dns-zones-bind
```

Example Inventory
-----------------

See the [top level README](../README.md)


License
-------

Apache License 2.0


Author Information
------------------

This role has be created by the Red Hat Containers & PaaS Community of Practice

Role Name
=========

This role can be used to manage views and zones for different DNS service providers. The supported ones are:

  - named
  - route53


Requirements
------------

The following packages are required:

  - python >= 2.6
  - boto

    Requirements specific for **`route53`**
    ---------------------------------------

      The following ENV variables associated with your AWS account must exist to use the module:

        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_ACCESS_KEY

      As an alternative (not recommended for being sensible data) the following ansible variables can be defined as part of the inventory:

        - aws_access_key
        - aws_secret_key

Role Variables
--------------

A dictionary, `dns_data`, with the following variables is expected:

  - named_global_config: if `named` is used, this will be the global configuration for the named/bind server.
  - views: List with views to configure as part of the DNS server/service.
    - name: Name of the view
    - zones: List of Hosted Zones
      - dns_domain: The Domain Name for the Hosted Zone
  - state: The desired state, present or absent

  Role specific variables for **`route53`**
  -----------------------------------------
  - route53: To interact with route53 dns provider
    - aws_access_key: AWS key ID, defined on AWS_ACCESS_KEY_ID environment variable
    - aws_secret_key: AWS secret KEY, defined on AWS_SECRET_ACCESS_KEY environment variable
    - vpc_id: This variable is required when creating private Zones
    - vpc_region: This variable is required when creating private Zones





Example Playbook
----------------

```
- hosts: servers
  roles:
    - role: manage-dns-zones
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

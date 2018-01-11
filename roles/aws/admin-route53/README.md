Role Name
=========

Manage Route 53 Zones

Requirements
------------

The following packages are required:

  - python >= 2.6
  - boto

The following ENV variables associated with your AWS account must exist to use the module:

  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY

As an alternative (not recommended for being sensible data) the following ansible variables can be defined as part of the inventory:
  
  - aws_access_key
  - aws_secret_key

Role Variables
--------------

Two differnt lists can be defined as variables, with another nested list included on each:

  - zone_add --> This list with the nested elements will be used to asure the zone and entries exists on Route 53 DNS service
  - zone_rm --> This list with the nested elements will be used to asure the zone or the entries do not exist on Route 53 DNS service
  - zone --> The Domain Name for the Hosted Zone
  - entries --> This is the list of records to be added/deleted from the parent zone
  - type --> The type of DNS record
  - hostname --> Name of the record set
  - ip --> The value for the record set

There is no support to remove not empty Zones.

Zone will be only removed when no entries are specified as part of the inventory for that Zone:

- zone: example.com
  entries: []

NOTE: The eempty entries declaration is mandatory for the role to work properly. Check tests directory for extended example

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: localhost
      roles:
        - aws/admin-route53

License
-------

BSD

Author Information
------------------

This role has be created by the Red Hat Containers & PaaS Community of Practice
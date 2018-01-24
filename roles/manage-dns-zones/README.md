Role Name
=========

This role can be used to manage views and zones for different DNS services providers. These are the supported ones:

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

  Two different lists can be defined as variables, with another nested list included on each:

    - dns_records_add --> This list with the nested elements will be used to asure the zone exists on the DNS service
    - dns_records_add --> This list with the nested elements will be used to asure the zone does not exist on Route 53 DNS service
    - view --> The name of the view
    - zone --> The Domain Name for the Hosted Zone

    Role specific **`named`** variables
    -----------------------------------

      The following nested list called


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

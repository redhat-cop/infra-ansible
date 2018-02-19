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

A dictionary with the following variables is expected:

  - dns_data: This list with the nested elements will be used to asure the views/zones are on the desired state on the DNS service
  - view: The name of the view
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

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: servers
  roles:
    - role: manage-dns-zones
```

Example Inventory
-----------------

```
dns_data:
- view: "private"
  zones:
    - dns_domain: "roletest4.com"
      state: absent
      named: True
      route53:
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        vpc_id: vpc-9dcde6f8
        vpc_region: eu-west-1
- view: "public"
  zones:
    - dns_domain: "roletest3.com"
      named: True
      route53:
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
    - dns_domain: "roletest5.com"
      state: absent
      route53:
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
```

License
-------

BSD

Author Information
------------------

This role has be created by the Red Hat Containers & PaaS Community of Practice

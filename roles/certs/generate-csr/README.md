generate-csr
============

This ansible role is used to create a CSR (Certificate Signing Request) for use with CA to generate valid certificates.

Requirements
------------

- An operational IdM/IPA account with the proper permissions to manage hosts.

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|csr_host_name| The hostname/FQDN of the host | yes | |
|csr_country| CSR Country (e.g.: 'US') | yes | |
|csr_state| CSR State (e.g.: North Carolina) | yes | |
|csr_location| CSR Location/City/Town (e.g.: Raleigh) | yes | |
|csr_org_name| CSR Organization/Company Name (e.g.: Red Hat, Inc.) | yes | |
|csr_org_unit| CSR Organization Name (e.g.: Community of Practice) | yes | |
|csr_email| CSR E-mail address to be used | true | |
|csr_subject_alt_names| List of CSR SANs | false | |



Example Playbooks
----------------

```
- hosts: csr-host
  roles:
  - generate-csr
```

Example Inventory
----------------

**inventory/hosts**
```
[csr-host]
localhost
```

**inventory/csr-host**
```
---
csr_host_name: "host-1.example.com"
csr_country: "US"
csr_state: "North Carolina"
csr_location: "Raleigh"
csr_org_name: "Red Hat, Inc."
csr_org_unit: "Open Innovation Labs"
csr_email: "myemail@example.com"
csr_subject_alt_names:
- my-host-1.example.com
- www-host-1.example.com

target_csr_file: "/tmp/{{ csr_host_name }}.csr"
target_host_key_file: "/tmp/{{ csr_host_name }}.key"
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

generate-csr
============

This ansible role is used to create a CSR (Certificate Signing Request) for use with CA to generate valid certificates.

Requirements
------------

- need to have the `python2-pyOpenSSL` and/or `python3-pyOpenSSL` package installed (Fedora/RHEL)

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|host_name | The hostname/FQDN of the host | yes | |
|csr.country | CSR Country (e.g.: 'US') | yes | |
|csr.state | CSR State (e.g.: North Carolina) | yes | |
|csr.location | CSR Location/City/Town (e.g.: Raleigh) | yes | |
|csr.org_name | CSR Organization/Company Name (e.g.: Red Hat, Inc.) | yes | |
|csr.org_unit | CSR Organization Name (e.g.: Community of Practice) | yes | |
|csr.email | CSR E-mail address to be used | true | |
|csr.subject_alt_names | List of CSR SANs | false | |
|target_cert_files.csr | File used for writing the CSR content | false | |
|target_cert_files.key | File used for writing the Certificate Private Key | false | |



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
host_name: "host-1.example.com"
csr:
  country: "US"
  state: "North Carolina"
  location: "Raleigh"
  org_name: "Red Hat, Inc."
  org_unit: "Open Innovation Labs"
  email: "myemail@example.com"
  subject_alt_names:
    - my-host-1.example.com
    - www-host-1.example.com

target_cert_files:
  csr: "/tmp/{{ csr_host_name }}.csr"
  key: "/tmp/{{ csr_host_name }}.key"
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

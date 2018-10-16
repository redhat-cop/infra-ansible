Set of Roles
============

This ansible role is used to create certificates, using the Red Hat IdM as a Certificate Authority.

A certificate is created by adding the FQDN for the requested certificate as a host, then the CSR is created and submitted before the host certificate & key (+ CA certificate) are retrieved. The certificates can optionally be written to local files for consumption.

Requirements
------------

An IDM account and ansible.

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**idm_fqdn**| FQDN of the IdM used as the CA | yes | N/A |
|**idm_user**| the idm user name | yes | N/A |
|**idm_password**| the idm password | yes | N/A |
|**csr_country**| country in which the certificate is made | yes | N/A |
|**csr_state**| state for the certificate | yes | N/A |
|**csr_location**| city of the certificate | yes | N/A |
|**csr_org_name**| organization for the certificate | yes | N/A |
|**csr_org_unit**| specific team for the certificate | yes | N/A |
|**csr_email**| email with which to register the certificate | yes | N/A |
|**host_name**| the domain name of the host (this is different than the fully qualified domain name) | yes | N/A |
|**host_realm**| the base URL of the host to which everything is tied | yes | N/A |
|**host_description**| description of the host | no | empty string |
|**target_host_cert_file**| the hosts certificate | yes | N/A |
|**target_host_key_file**| The target location for where the host certificate **key** file is written to | no | N/A |
|**target_ca_cert_file**| The target location for where the CA certificate file is written to | no | N/A |
|**target_ca_cert_file**| The target location for where the CA certificate file is written to | no | N/A |
|**host_force_add**| add the host even if no DNS record(s) exists for the host | no | True |
|**api_version**| API version to be passed | no | 2.213 |

Dependencies
------------
There are no strict dependencies for this role beyond ansible and an idm account.

Example Playbooks
----------------

from ```test/test.yml```

```
- hosts: localhost
  vars:
    idm_fqdn: "idm.example.com"
    idm_user: "admin"
    idm_password: "admin!"
    csr_country: "US"
    csr_state: "North Carolina"
    csr_location: "Raleigh"
    csr_org_name: "Red Hat, Inc."
    csr_org_unit: "Open Innovation Labs"
    csr_email: "myemail@example.com"
    host_name: "host-1.example.com"
    host_realm: "EXAMPLE.COM"
    host_description: "Testing My Host Cert"
    target_host_cert_file: "/tmp/{{ host_name }}.pem"
    target_host_key_file: "/tmp/{{ host_name }}.key"
    target_ca_cert_file: "/tmp/ca.pem"
  roles:
  - idm-host-cert
```

Example Inventory
----------------

from ```test/inventory```
```
localhost
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

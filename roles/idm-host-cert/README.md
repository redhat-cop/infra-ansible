Set of Roles
============

The ansible roles found in this directory are associated with creating and configuring idm host certs.

First it logs into idm, creates a session, and then registers the host. Then, it generates a private key and csr. Next, it creates the cert, retrieves the old one, and overwrites it. As a final check, it prints out the certs.

Requirements
------------

An IDM accout and ansible.

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**idm_fqdn**| is the fully qualified domain name for the host | no | N/A |
|**idm_user**| the idm user name | yes | N/A |
|**idm_password**| the idm password | yes | N/A |
|**csr_country**| country in which the certificate is made | yes | N/A |
|**csr_state**| state for the certificate | yes | N/A |
|**csr_location**| city of the certificate | yes | N/A |
|**csr_org_name**| organization for the certificate | yes | N/A |
|**csr_org_unit**| specific team for hte certificate | yes | N/A |
|**csr_email**| email with which to register the certificate | yes | N/A |
|**host_name**| the domain name of the host (this is different than the fully qualified domain name) | yes | N/A |
|**host_realm**| the base URL of the host to which everything is tied | yes | N/A |
|**host_description**| description of the host | yes | N/A |
|**target_host_cert_file**| the hosts certificate | yes | N/A |
|**target_host_key_file**| the key for the host | yes | N/A |
|**target_ca_cert_file**| the certificate authority file which is cryptographically linked with the host key | yes | N/A |

```
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
target_ca_cert_file: "/tmp/ca.pem"alsamix

```

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

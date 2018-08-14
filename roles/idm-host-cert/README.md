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
|**idm_fqdn**| sets up the directory for where to retrieve the content, eventually to be used to seed the web server | no | N/A |
|**idm_user**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**idm_password**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**csr_country**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**csr_state**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**csr_location**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**csr_org_name**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**csr_org_unit**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**csr_email**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**host_name**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**host_realm**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**host_description**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**target_host_cert_file**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**target_host_key_file**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |
|**target_ca_cert_file**| sets the default root folder for the where to deposit the web files that have been retrieved. | yes | N/A |

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

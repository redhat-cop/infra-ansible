idm-host-cert
=============

This ansible role is used to create host certificates, using the Red Hat IdM / FreeIPA as a Certificate Authority.

A certificate is created by adding the FQDN for the requested certificate as a host entry in the IdM/IPA, then the CSR is submitted to generate a host certificate. The host certificate, key and CA are all retrieved and can optionally be written to files specified in the inventory.

Requirements
------------

- An operational IdM/IPA account with the proper permissions to manage hosts.

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|idm_fqdn| FQDN of the IdM/IPA used as the CA | yes | |
|idm_user| The IdM/IPA user name | yes | |
|idm_password| The IdM/IPA password | yes | |
|host_name| The hostname/FQDN of the host | yes | |
|host_realm| The IdM/IPA REALM to associated the host with | yes | |
|host_description| Description of the host | no | '' |
|target_host_cert_file| Optional file to write the host certificate to | no | |
|target_ca_cert_file| Optional file to write the CA certificate to | no | N/A |
|host_force_add| Force add the host even if no DNS record(s) exists for the host | no | True |
|api_version| The IdM/IPA API version to be passed | no | 2.213 |


Dependencies
------------
This role depends on a CSR being available for consumption. The CSR can be genreated with the (generate-csr)[../generate-csr] role.

Example Playbooks
----------------

```
- hosts: cert-host
  vars:
    target_cert_files:
      csr: ...
      key: ...
  roles:
  - idm-host-cert
```

Example Inventory
----------------

**inventory/hosts**
```
[cert-host]
localhost
```

**inventory/cert-host**
```
idm_fqdn: "idm.example.com"
idm_user: "admin"
idm_password: "admin!"
host_name: "host-1.example.com"
host_realm: "EXAMPLE.COM"
host_description: "Testing My Host Cert"
target_host_cert_file: "/tmp/{{ host_name }}.pem"
target_ca_cert_file: "/tmp/ca.pem"
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

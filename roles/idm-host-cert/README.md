Set of Roles
============

The ansible roles found in this directory are associated with configuring a docker set up.

Effectively, the `docker.yml` task will install packages for docker and add users to the docker user group.

Requirements
------------

1. Docker installed on the host machine.
2. A username for configuring docker access


Role Variables
--------------
docker_install is used to control if Docker should be installed or not. docker_username is used to configure which user should have access to use docker (and hence be part of the 'docker' group).

```
docker_username: root
docker_install: True
```

Dependencies
------------
There are no strict dependencies for this role beyond ansible.

Example Playbooks
----------------

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

```
localhost
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

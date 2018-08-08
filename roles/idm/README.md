Role Name
=========

This deploys IdM servers with optional replicas and no integrated DNS

## Requirements
The IdM server role requires that external DNS server be fully functional with forward and reverse DNS

## Dependencies

None

## Optional Vars

idm_master_hostname is optional if Replica are NOT required and only setting up a single IdM server

#### NOTE: If you want to join an active directory then idm-domain MUST equal idm-realm

### Example Inventory

```
[all:vars]
idm_master_hostname=idm1.test.lab
idm_domain=test.lab
idm_realm=test.lab
idm_dm_password=test123$
idm_admin_password=test123$

[idm]
idm1.test.lab
idm2.test.lab idm_src=idm1.test.lab
idm3.test.lab idm_src=idm1.test.lab
```
### Example Playbook
```
- hosts: idm
  become: yes

  roles:
    - idm

```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

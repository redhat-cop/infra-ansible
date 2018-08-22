Role Description
================

This ansible role updates a hosts' hostname or FQDN

Requirements
------------

No specific system requirements.

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
| hostname | The (short) hostname to use for the host | no | the 'inventory_hostname_short' fact |
| dns_domain | DNS domain to append to the hostname to make a FQDN | no | |


Dependencies
------------

N/A

Example Playbooks
----------------

```
- hosts: my-host
  roles:
  - config-hostname
```

Example Inventory
----------------

**inventory/hosts:**
```
[my-host]
192.168.1.10
```

**inventory/group_vars/my-host.yml:**

```
---

hostname: "my-cool-host"
dns_domain: "my-cool-domain.com"
```



License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

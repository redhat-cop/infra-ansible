Set of Roles
============

The ansible roles found in this directory are associated with configuring routes for an interface. It is broken into two steps: prep and routing. In prep, it checks whether the OS it is operating on is Fedora or RHEL and makes the appropriate installs. In routing, it configures the routes using the template found at ```/templates/route.j2 ```.

Requirements
------------

This requires that the OS is based on Fedora or RHEL.

Role Variables
--------------

no custom role variables


Dependencies
------------
There are no strict dependencies for this role beyond ansible and the ```route.j2``` route configuration.

Example Playbooks
----------------
from ```/tests/infrahosts.yml```

```
---

- name: 'Configure routes on the host'
  hosts: infra_hosts
  roles:
  - role: config-routes
```

Example Inventory
----------------

**inventory/hosts:**
```
[all:vars]
ansible_user: fedora
ansible_become: True
ansible_host: 192.168.1.10

[infra_hosts]
infra-1.example.com
```

**inventory/group_vars/infra-hosts.yml:**

```
---

routes:
- device: eth0
  entries:
  - address: 192.168.10.0
    netmask: 255.255.255.0
    gateway: 192.168.1.1
  - address: 192.168.11.0
    netmask: 255.255.255.0
    gateway: 192.168.1.1
```



License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

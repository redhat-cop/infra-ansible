Role Name
=========

This role performs reboot of a host (and waits for it to come back).


Requirements
------------

N/A

Role Variables
--------------

N/A

Dependencies
------------

N/A

Example Playbook
----------------

```
  - hosts: test_hosts
    roles:
      - role: reboot-host
```


Example Inventory
-------------------

Hosts to reboot.

```
  [test_hosts]
  host1.test.lab ansible_user=root ansible_host=192.168.1.1
  host2.test.lab ansible_user=root ansible_host=192.168.1.2
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.


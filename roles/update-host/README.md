Role Name
=========

This role performs updates and reboots a host (and waits for it to come back).


Requirements
------------

A Linux distro supporting the `package` module.

Role Variables
--------------

`pkg_update`: Optional variable controls if packages should be updated or not (useful to avoid surprises when this role is part of a bigger playbook).
`force_host_reboot`: Optional variable to force a reboot even if no updates were performed.

| Name | What | Default|
|---|---|---|
|pkg_update|Boolean|False|
|force_host_reboot|Boolean|False|


Dependencies
------------

N/A

Example Playbook
----------------

```
  - hosts: servers
    roles:
      - role: update-host
```


Example Inventory 1
-------------------

Enable updates on all hosts

```
  [all:vars]
  pkg_update=True

  [test_hosts]
  host1.test.lab ansible_user=root ansible_host=192.168.1.1
  host2.test.lab ansible_user=root ansible_host=192.168.1.2
```

Example Inventory 2
-------------------

Enable updates on all hosts except 1

```
  [all:vars]
  pkg_update=True

  [test_hosts]
  host1.test.lab ansible_user=root ansible_host=192.168.1.1
  host2.test.lab ansible_user=root ansible_host=192.168.1.2 pkg_update=False

```

Example Inventory 3
-------------------

Update 1 host

```
  [all:vars]
  pkg_update=False

  [test_hosts]
  host1.test.lab ansible_user=root ansible_host=192.168.1.1
  host2.test.lab ansible_user=root ansible_host=192.168.1.2 pkg_update=True

```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.


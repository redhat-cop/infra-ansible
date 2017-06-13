# update-hosts role

This role drive when the role updates the packages on the inventory

## Role Variables

`pkg_update: Boolean` defaults: False

This variable controls the package updates in the role.

Inventory example 1:
Enable updates on all hosts

```
[all:vars]
pkg_update=True

[test_hosts]
host1.test.lab ansible_user=root ansible_host=192.168.1.1
host2.test.lab ansible_user=root ansible_host=192.168.1.2
```

Inventory example 2:
Enable updates on all hosts except 1

```
[all:vars]
pkg_update=True

[test_hosts]
host1.test.lab ansible_user=root ansible_host=192.168.1.1
noupdate.test.lab ansible_user=root ansible_host=192.168.1.2 pkg_update=False

```

Inventory example 3:
Update 1 host

```
[all:vars]
pkg_update=False

[test_hosts]
host1.test.lab ansible_user=root ansible_host=192.168.1.1
update.test.lab ansible_user=root ansible_host=192.168.1.2 pkg_update=True

```

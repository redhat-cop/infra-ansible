# update-hosts role

This role performs updates and reboots a host (and waits for it to come back).

## Role Variables

`pkg_update` variable controls the package updates in the role.

| Name | What | Default|
|---|---|---|
|pkg_update|Boolean|False|


#### Inventory example 1:
Enable updates on all hosts

```
[all:vars]
pkg_update=True

[test_hosts]
host1.test.lab ansible_user=root ansible_host=192.168.1.1
host2.test.lab ansible_user=root ansible_host=192.168.1.2
```

#### Inventory example 2:
Enable updates on all hosts except 1

```
[all:vars]
pkg_update=True

[test_hosts]
host1.test.lab ansible_user=root ansible_host=192.168.1.1
host2.test.lab ansible_user=root ansible_host=192.168.1.2 pkg_update=False

```

#### Inventory example 3:
Update 1 host

```
[all:vars]
pkg_update=False

[test_hosts]
host1.test.lab ansible_user=root ansible_host=192.168.1.1
host2.test.lab ansible_user=root ansible_host=192.168.1.2 pkg_update=True

```

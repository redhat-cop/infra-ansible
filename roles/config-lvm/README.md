Role Name
=========

This role configures PV/VG/LVs

Requirements
------------



Role Variables
--------------

See `Example Inventory` below for more specific details. At a high level, the following variables need to be defined:

- `lvm_entries`: A list of devices to be configured (and mounted)

Dependencies
------------

None


Example Playbook
----------------

```
    - hosts: servers
      roles:
      - role: config-lvm
```


Example Inventory
----------------

```
lvm_entries:
- storage_device: "/dev/vdb"
  vg_name: "vg1"
  lv_name: "lv1"
  mount_path: "/mnt/vg1-lv1" 

```


License
-------

BSD

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

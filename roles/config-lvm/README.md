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
  lv_size: "50G"
  lv_fstype: "ext4"
  mount_path: "/mnt/vg1-lv1"

```

* By default the lv_size will be `100%VG` (globally configurable through `default_lv_size`)
* By default the lvm will be formatted using xfs (globally configurable through `lvm_fstype`)

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

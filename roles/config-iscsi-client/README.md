Set of Roles
============

The ansible roles found in this directory are associated with configuring an iSCSI client. In prep it installs some required packages for the client. Then, it checks that the initiator name and the service are set and running correctly. next, it configures the multipath set up and restarts it. After this is configures the LVM, updates the meta-data, and runs through final checks.

Requirements
------------

This requires a correct iSCI initiator name.

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**iscsi_target**|  the storage resource used in linking data storage | no | N/A |
|**iscsi_brand**| the type of linked sorage| no | N/A |
|**iscsi_initiatorname**| used for identifiying a specific element | yes | n/a|


Dependencies
------------
There are no strict dependencies for this role beyond ansible and it is useful to have the content to seed the web server already prepared.

Example Playbooks
----------------
from ```tests/test.yml```

```
---

- hosts: iscsi
  roles:
  - role: config-iscsi-client
```

Example Inventory
----------------

from ```tests/inventory```
```
[iscsi]
node-1 ansible_user=fedora ansible_become=True ansible_host=192.168.1.11
node-2 ansible_user=fedora ansible_become=True ansible_host=192.168.1.12
```

from ```tests/host_vars/node-1.yml```
```
---

iscsi_initiatorname: iqn.1994-05.com.example:node-1

disk_mapping:
- lun: 0
  vg: vg0
  lv: lv0
  mount_path: /mnt/vg0-lv0
- lun: 1
  vg: vg1
  lv: lv0
  mount_path: /var/vg1-lv0
- lun: 2
  vg: vg2
```

from ```tests/host_vars/node-1.yml```
```
---

iscsi_initiatorname: iqn.1994-05.com.example:node-2

disk_mapping:
- lun: 0
  vg: vg0
  lv: lv0
  mount_path: /mnt/vg0-lv0

```

from ```tests/group_vars/iscsi.yml```

```
---

iscsi_target: "192.168.1.21"
iscsi_brand: "NETAPP"

```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

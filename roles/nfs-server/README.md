# nfs-server role


## Inventory
Below is an example inventory for the NFS server:

```
nfs_storage_device=/dev/vdb

nfs_shares:
- name: registry
- name: metrics
  nfs_owner: nfsnobody       # (optional - default: "nfsnobody") 
  nfs_group: nfsnobody       # (optional - default: "nfsnobody") 
  nfs_mode: 0777             # (optional - default: "0777")
  nfs_share_options          # (optional - default: "rw,root_squash,no_wdelay")
- name: logging
```

## Optional Server Config Parameters

| variable | purpose | default value |
|:---------|:--------|:--------------|
|nfs_vg_name|The Volume Group (VG) name used for creating the NFS share|nfs|
|nfs_lv_name|The Logical Volume (LV) named used fro creating the NFS share|exports|
|nfs_share_basedir|NFS share directory base mount point|/exports|







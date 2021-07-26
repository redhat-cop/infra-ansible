config-container-storage-setup
==============================

name: config-container-storage-setup
The purpose of this role is configure container storage. 

Requirements
------------

No specific system requirements.

Variables
------------------

Defaults file has examples of variables that can be used. The are also listed below.

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**docker_dev**|  The disk device that will be used. | no | /dev/vdb |
|**docker_vg**|  Name of the volume group to be created. | no | docker-vol |
|**docker_data_size**|  How much of the vg should be used. | no | 95%VG |
|**docker_dm_basesize**|  This value affects the system-wide “base” empty filesystem that may already be initialized and inherited by pulled images. | no | "3G" |
|**container_root_lv_name**|  Name given to the root logical volume used by docker. | no | dockerlv |
|**container_root_lv_mount_path**|  The location the root logical volume will be mounted. | no | /var/lib/docker |
|**config_file_dest**|  The location where templates will be copied. | no | /etc/sysconfig/docker-storage-setup |


Example Playbook
----------------

```
- name: 'Configure chronyd'
  hosts: docker_hosts
  roles:
    - config-container-storage-setup
  tags: 
    - configure_docker_hosts
```

License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
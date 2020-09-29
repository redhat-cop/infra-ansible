config-libvirt
==============

name: config-libvirt
The purpose of this role is to install and configure a basic libvirt installation. 

Requirements
------------

No specific system requirements.

Variables
------------------

Defaults file has example of variables that can be used. 

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**libvirtenable**|  determines if libvirt will be installed or not | no | true |
|**virt_manager_install**| Determines is virt-manager is installed | no | true |
|**virt_manager_package**| The Name of the virt manager package| no | List of packages found in [defaults/main.yml](defaults/main.yml) |
|**libvirt_base_packages**| List of all the packages required to deploy libvirt | no | List of packages found in [defaults/main.yml](defaults/main.yml) |
|**service_name**| The name of the libvirt service | no | 'libvirtd' |


Example Playbook
----------------

```
- name: 'Configure libvirt'
  hosts: libvirt_hosts
  roles:
    - config-libvirt
  tags: 
    - configure_libvirt
```

License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

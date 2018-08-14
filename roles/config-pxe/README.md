Set of Roles
============
The ansible roles found in this directory are associated with configuring a pxe, or pre execution environment.

First, it installs sys-linux, tftp-server, and firewall, then it makes sure that firewalld is running with port 69 is open and that the tftp-server is running. After the basic prep work is done, the next step is to ensure that the basic directories are set up and then to populate them, then the necessary system specific defaults are set. Kickstart files are then copied over.

Requirements
------------
Nothing is required. However, this playbook will work best on a RHEL OS.

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**ks_files**| kickstart files' source | no | N/A |
|**ks_files_destination**| kickstart files' source | yes | N/A |

```
ks_files: "{{ inventory_dir }}/../files/ks/"
ks_files_destination: "/var/www/html/ks"
```
| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**name**| the name that will show up in the PXE config/menu | yes | N/A |
|**source**| where the source for the PXE boot binaries are stored (BIOS, not UEFI) | yes | N/A |
|**destination**| where the PXE boot binaries are to be copied to (BIOS, not UEFI) | yes | N/A |
|**menu_label**| the descriptive string that will show in the PXE menu | no | N/A |
|**kernel**| the boot kernel path (relative to the TFTP server) for this entry | yes | N/A |
|**append**| where the source for the PXE boot binaries are stored (BIOS, not UEFI) | yes | N/A |
|**initrdefi**| The initrd for UEFI PXE boot | yes | N/A |

```
pxe_entries:
- name: "Fedora25-Server-x86_64"
  source: "/var/www/html/fedora/25/server/x86_64/images/pxeboot/"
  destination: "images/fedora/25/server/x86_64/pxeboot"
  menu_label: "Fedora 25 Server (64-bit) - manual"
  kernel: "/images/fedora/25/server/x86_64/pxeboot/vmlinuz"
  append: "initrd=/images/fedora/25/server/x86_64/pxeboot/initrd.img sshd text ip=dhcp inst.repo=http://my-web-server.example.com/fedora/25/server/x86_64"
  initrdefi: "/images/fedora/25/server/x86_64/pxeboot/initrd.img"
```

```
[pxe-server]
192.168.1.10
```

```
---
ansible_user=fedora
ansible_become=True
```

Dependencies
------------
There are no strict dependencies for this role beyond ansible and, ideally, a rhel OS.

Example Playbooks
----------------

```
- hosts: pxe-server
  roles:
  - config-pxe
```

Example Inventory
----------------

```
[all:vars]

tftpserver_root_dir: "/var/lib/tftpboot"
pxe_menu_title: "My cool PXE server"
pxe_timeout: 300
uefi_source: "/var/www/html/rhel/7/3/x86_64/EFI/BOOT/"
ks_files: "{{ inventory_dir }}/../files/ks/"
ks_files_destination: "/var/www/html/ks"

pxe_entries:
- name: "Fedora25-Server-x86_64"
  source: "/var/www/html/fedora/25/server/x86_64/images/pxeboot/"
  destination: "images/fedora/25/server/x86_64/pxeboot"
  menu_label: "Fedora 25 Server (64-bit) - manual"
  kernel: "/images/fedora/25/server/x86_64/pxeboot/vmlinuz"
  append: "initrd=/images/fedora/25/server/x86_64/pxeboot/initrd.img sshd text ip=dhcp inst.repo=http://my-web-server.example.com/fedora/25/server/x86_64"
  initrdefi: "/images/fedora/25/server/x86_64/pxeboot/initrd.img"



[pxe-server]
192.168.1.10 ansible_user=fedora ansible_become=True
```

License
-------
Apache License 2.0

Author Information
------------------
Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

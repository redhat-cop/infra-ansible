config-vnc-server
=================

This role installs, configures and enables a VNC server on the target host(s).

Requirements
------------

None. However, if installed on a system requiring entitlements, make sure the correct channels are enabled for package installations.

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|**vnc_home_dir**| The home directory path for the user | no | `/home` |
|**main_user**| The user that the VNC will be run from | yes | |
|**vnc_password**| The vnc password to be used for the above user | no | vncpasswd01 |
|**gome_install**| True/False if `gnome` will be used with this VNC server | no | False |
|**xfce_install**| True/False if `XFCE` will be used with this VNC server | no | False |
|**lxde_install**| True/False if `LXDE` will be used with this VNC server | no | False |
|**mate_install**| True/False if `MATE` will be used with this VNC server | no | False |

_**Note:**_ The various graphical options above are only needed to get the correct xstartup file installed for the VNC server. To actually install the graphical system, make sure to use the other `config_[gnome|xfce|lxde|mate]` roles for the target setup. Also note that these are mutual exlusive in that only one of these can be started by the VNC server as-is (since only one server is supported by this role at the moment).


Dependencies
------------

N/A

Example Playbooks
----------------

```
- hosts: vnc-server
  roles:
  - role: config-vnc-server
```

Example Inventory
----------------


**inventory/hosts**
```

[vnc-server]
192.168.10.43
```

**inventory/group_vars/vnc-server.yml**
```
---

vnc_home_dir: /lclhome
main_user: user1
vnc_password: password
lxde_install: True

```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

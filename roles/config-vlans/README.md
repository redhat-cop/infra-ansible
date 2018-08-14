Set of Roles
============

The ansible roles found in this directory are associated with prepping for a vLAN (virtual LAN) install and configuring a vLAN install. VLANs allow for creating virtual area networks to avoid the costly process of buying and configuring new expensive routers for what may be a temporary measure.

The role is relatively straightforward:  it configures the vlans interfaces and brings them online.

Requirements
------------

None beyond ansible.

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**ifcfg.device**| the home directory where all the VNC files live | yes | ``` /home/ ``` |
|**main_user**| the user that the VNC will be run from| yes | root |
|**vnc_password**| the vnc password | no | vncpasswd01 |
|**passwd_info.stat.exists**| a boolean variable that indicates whether or not a password exists  | no | False |
|**gnome_install**| whether or not the system the VNC server is being installed on uses gnome | no | False |
|**xfce_install**| whether or not the system the VNC server is being installed on uses XFCE | no | False |
|**lxde_install**| whether or not the system the VNC server is being installed on uses LXDE | no | False |
|**mate_install**| whether or not the system the VNC server is being installed on uses MATE | no | False |

Dependencies
------------
No software dependencies that aren't taken care of by the ```/roles/prereq.yml```

Example Playbooks
----------------

```
- hosts: localhost
  roles:
  - role: config-vnc-server
```

Example Inventory
----------------

```
[all:vars]
vnc_home_dir: /.vnc
main_user: root
vnc_password: password!
passwd_info.stat.exists: False
gnome_install: True
xfce_install: False
lxde_install: False
mate_install: False

```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

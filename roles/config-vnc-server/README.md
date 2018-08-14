Set of Roles
============

The ansible roles found in this directory are associated with prepping for a VNC (virtual network computing) server install and configuring a VNC server install.

First, if necessary, it preps the system for the install by installing firewalld and enabling it. Then it opens up firewall so that a network file system can be used. NOTE: this step can be skipped if a network file system is already in place. Afterwards, it installs additional packages, ensures the appropriate directories are in place, and sets up the VNC password. The final steps are modifying the start up scripts, user configs, and SELinux configs so that it can be used.

Requirements
------------

1. Python should be installed on the existing machine.

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**vnc_home_dir**| the home directory where all the VNC files live | yes | ``` /home/ ``` |
|**main_user**| the user that the VNC will be run from| yes | root |
|**vnc_password**| the vnc password | no | vncpasswd01 |
|**passwd_info.stat.exists**| a boolean variable that indicates whether or not a password exists  | no | False |
|**gnome_install**| whether or not the system the VNC server is being installed on uses gnome | no | False |
|**xfce_install**| whether or not the system the VNC server is being installed on uses XFCE | no | False |
|**lxde_install**| whether or not the system the VNC server is being installed on uses LXDE | no | False |
|**mate_install**| whether or not the system the VNC server is being installed on uses MATE | no | False |

Dependencies
------------
A version of Python should be installed.

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

```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

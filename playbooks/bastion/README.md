# Bastion Host / Control Host playbook

This playbook uses a variety of roles in this repo to setup a bastion host, also some times called a control host. The inventory can be used (per instructions below) to control which software and services get installed on the bastion host. 


## Prerequisites
A running instance (VM or cloud image) such as Fedora, CentOS or Red Hat Enterprise Linux. The instance needs to be subscribed (if applicable) and configured with access to the necessary repos (in most cases, the exsisting repos / configuration is sufficient).

## Inventory Options

| variable | info |
|:--------:|:----:|
|main_user|The username this bastion is primerly being enabled for| 
|ipa_install|Set to "yes" if you'd like to integrate with a backend IPA/IdM service|
|ipa_domain|If `ipa_install` is set to "yes", set this domain to match what your environment uses (obtain from sys admin if not known)|
|ipa_automount|If `ipa_install` is set to "yes", set the required automount location for home directories (obtain from sys admin if not known)|
|ipa_username|If `ipa_install` is set to "yes", this is the username of an account that has the permission to join this host to the above IPA/IdM domain (obtain from sys admin if not known)|
|ipa_password|If `ipa_install` is set to "yes", this is the password of an account that has the permission to join this host to the above IPA/IdM domain (obtain from sys admin if not known)
|docker_install|Set to "yes" if you'd like to enable docker on this host|
|docker_username|Set to the desirable user (your username) to be added to the docker group (to allow for docker admin)|
|xfce_install|Set to "yes" if you'd like XFCE enabled on this host for a graphical UI (note XFCE often works better than gnome for VNC)|
|gnome_install|Set to "yes" if you'd like gnome enabled on this host for a graphical UI|
|vnc_server_install|Set to "yes" if you'd like to enable a VNC server on this host for graphical access to the host|



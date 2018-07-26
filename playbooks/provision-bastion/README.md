# Bastion Host / Control Host playbook

This playbook uses a variety of roles in this repo to setup a bastion host, also some times called a control host. The inventory can be used (per instructions below) to control which software and services get installed on the bastion host.


## Prerequisites
A running instance (VM or cloud image) such as Fedora, CentOS or Red Hat Enterprise Linux. The instance needs to be subscribed (if applicable) and configured with access to the necessary repos (in most cases, the exsisting repos / configuration is sufficient).

If the IdM / IPA integration is to be used, it is a prerequisites that the environment is set up with automatic client server discovery vis DNS SRV records (consult your sys admin if this is an unfamiliar area).

## Gotcha's
1. If running in a cloud environment, for example OpenStack, make sure to have the correct ports open in the security groups (e.g.: 5901 for VNC, 22 for SSH, etc.)
2. When enabling VNC, and you already have a shared home directory, make sure the proper changes are made to the VNC configuration (typically in `~/.vnc` ) to allow for the service to run correctly.

## Example run
How to run the playbook may depend on the options selected. However, below is an example execution whereas the password for IPA/IdM integration (with `ipa_client_install` set to `True` in the inventory) is passed in rather than statically set in the inventory. Modify the inventory to your liking in `playbooks/bastion/inventory`, then at the top level of the repository, execute the following command:

```
> ansible-playbook -i playbooks/bastion/inventory playbooks/bastion/install.yml -e 'ipa_password=<ipa/IdM password>'
```

**Note:** If your password contains any special characters, e.g.: a '!', it's important to use the single quotes for the passed in value as it otherwise may be interpereted by the shell.

## Inventory Options

**Note:** If you are intending to use the IdM/IPA integration, and are unfamiliar with the IdM/IPA variables below, please consult the IdM/IPA documentation or your sys admin for details.

**Note:** When installing a GUI (i.e.: XFCE, LXDE, Gnome), it's recommended that only one is selected as running multiple is not supported nor tested by this playbook/roles.

| variable | info |
|:--------:|:----:|
|main_user|The username this bastion is primerly being enabled for|
|ipa_client_install|Set to `True` if you'd like to integrate with a backend IPA/IdM service|
|ipa_domain|If `ipa_client_install` is set to `True`, set this to the existing IdM / IPA domain your environment uses (obtain from sys admin if not known)|
|ipa_automount_location|If `ipa_client_install` is set to `True`, set the required automount location for home directories (obtain from sys admin if not known)|
|ipa_username|If `ipa_client_install` is set to `True`, this is the username of an account that has the permission to join this host to the above IPA/IdM domain (obtain from sys admin if not known)|
|ipa_password|If `ipa_client_install` is set to `True`, this is the password of an account that has the permission to join this host to the above IPA/IdM domain (obtain from sys admin if not known)
|docker_install|Set to `True` if you'd like to enable docker on this host|
|docker_username|Set to the desirable user (your username) to be added to the docker group (to allow for docker admin)|
|docker_compose_install|Set to `True` if you'd like to have docker-compose installed on this host. NOTE: This will auto set docker_install=True (not supported on CentOS)|
|xfce_install|Set to `True` if you'd like XFCE enabled on this host for a graphical UI (note MATE, XFCE or LXDE often works better than gnome for VNC)|
|lxde_install|Set to `True` if you'd like LXDE enabled on this host for a graphical UI (note MATE, XFCE or LXDE often works better than gnome for VNC)|
|gnome_install|Set to `True` if you'd like gnome enabled on this host for a graphical UI|
|mate_install|Set to `True` if you'd like MATE Desktop enabled on this host for a graphical UI (note MATE, XFCE or LXDE often works better than gnome for VNC)|
|vnc_server_install|Set to `True` if you'd like to enable a VNC server on this host for graphical access to the host|
|list_of_packages_to_install|List of additional packages (RPMs) to be installed at the end of the bastion host preparation, e.g.: `['git', 'vim']`|
|timezone| `Optional` Timezone of the Bastion ie `America/Denver`|
|ansible_python_interpreter| `Optional` Required to be set to `/usr/bin/python3` when using systems like Fedora 28 where certain packages are dependent on python3|
|vnc_password| `Optional` Set VNC password to a specific value instead of accepting the default| 


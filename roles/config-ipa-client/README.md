Role Name
=========

This set up an IdM/IPA integration on a Fedora, CentOS or RHEL based client.

Requirements
------------

- The Fedora system needs to be configured to allow for Ansible interactions (i.e.: SSH enabled & Python2 installed).
- The RHEL system needs to be subscribed/registered and have valid repos enabled for the IPA client (e.g.: rhel-7-server-rpms).
- The CentOS system needs no additional configurations.

Dependencies
------------

None

Variables
---------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**ipa_client_install** | Used to set if IPA client will be installed | yes | false |
|**main_user**| The name of the primary user | yes | no default |
|**admin_group**| The name of the administration group you wish to use | yes | no default |
|**move_local_user_home**|  Use if you wish to change local users home | yes | false |
|**new_local_home_dir**| If changing the user home, this is the new location |  yes | "/lclhome" |
|**temporary_username**| Temp username to use | yes | "lcluser" |


Example Inventory
-----------------

``` yaml
[all:vars]

ipa_client_install=true
ipa_domain=test.example.com
ipa_automount_location=userhome
ipa_username=testuser
ipa_password=testuserpassword

[bastion]
192.168.1.16 ansible_user=fedora ansible_become=True
```

Example Playbook
----------------

``` yaml
- hosts: server
  become: yes

  roles:
    - role: config-ipa-client

```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

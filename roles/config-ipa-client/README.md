Role Name
=========

This set up an IdM/IPA integration on a Fedora, CentOS or RHEL based client.

## Requirements
- The Fedora system needs to be configured to allow for Ansible interactions (i.e.: SSH enabled & Python2 installed)
- The RHEL system needs to be subscribed/registered and have valid repos enabled for the IPA client (e.g.: rhel-7-server-rpms)
- The CentOS system needs no additional configurations

## Dependencies

None


### Example Inventory

```
[all:vars]

ipa_client_install=yes
ipa_domain=test.example.com
ipa_automount_location=userhome
ipa_username=testuser
ipa_password=testuserpassword

[bastion]
192.168.1.16 ansible_user=fedora ansible_become=True
```

### Example Playbook
```
- hosts: server
  become: yes

  roles:
    - role: config-ipa-client

```

Role Name
=========

This deploys IDM servers without integrated DNS and Replicas

Requirements
------------

The IDM server role requires that external DNS server be fully functional withforward and reverse DNS 

Dependencies
------------

None


Example Inventory
----------------

[all:vars]
idm_master_hostname=idm1.test.lab
idm_domain=test.lab
idm_realm=LAB
idm_dm_password=test123$
idm_admin_password=test123$

[idm]
idm1.test.lab 
idm2.test.lab idm_src=idm1.test.lab
idm3.test.lab idm_src=idm1.test.lab

Example Playbook
----------------

- hosts: idm
  become: yes

  roles:
    - idm



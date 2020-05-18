quay-install
=========

> Quay install and configuration.

Installs Quay in either Docker or OpenShift.

Requirements
------------

Registration with Red Hat. 
  github.com/kenhitchcock/ansible-role-redhat-register.git

Deploying on Docker
Docker installed.
  github.com/kenhitchcock/ansible-role-docker-install

Deploying on OpenShift
OpenShift Cluster running
  To create VMs/Instances in Libvirt/AWS
  github.com/kenhitchcock/ansible-role-cornerstone
  OpenShift Prereqs
  github.com/kenhitchcock/ansible-role-ocp-prereqs
  OpenShift ansible installer
  github.com/kenhitchcock/openshift-ansible

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

    # Only variable to set for a default deployment.
    QUAY_DEPLOYTYPE: "openshift"  # Options accepted are "docker" and "openshift"

Example playbook
----------------
    - name: "Test Quay Openshift deployment Role "
      hosts: ocpmaster
      become: true
      vars:
        - QUAY_DEPLOYTYPE: "openshift"

      tasks:
        - include_role:
            name: ../roles/ansible-role-quay-install

Future Releases
---------------

 - Ability to autoconfigure Quay.

License
-------

 MIT

Author Information
------------------

Ken Hitchcock [Github](https://github.com/kenhitchcock)


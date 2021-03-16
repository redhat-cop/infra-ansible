config-ansible-tower-ocp-ssh
============================

This role is a helper for `config-ansible-tower-ocp` to create an Openshift secret from an SSH key, and mount it as read-only in the `awx` users $HOME/.ssh folder

## Requirements

  - A running OpenShift Cluster and installed 'oc' client in the Ansible host


## Role Variables

The variables used to install Ansible Tower on OpenShift are outlined in the table below. 

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ocp_ssh_private_keys.src|File path to ssh private key, for example ssh_private_key.pem|yes||
|ocp_ssh_private_keys.dest|Path where ssh private key will be mounted on the container|yes|/var/lib/awx/.ssh + src \| basename|
|ocp_ssh_private_keys.secret_project|Openshift Project for your tower deployment|no|tower|
|ocp_ssh_private_keys.secret_name|A name for your secret|no|src \| basename|
|ocp_ssh_private_keys.deployment_type|One of deployment or deploymentconfig|no|deployment|
|ocp_ssh_private_keys.deployment_name|The name of the Ansible Tower deployment|no|ansible-tower|

## Example Inventory

```yaml
---

ocp_ssh_private_keys:
  - src: "{{ inventory_dir }}../files/ssh_private_key.pem"
    dest: /var/lib/awx/.ssh/ssh_private_key.pem
    secret_project: "{{ openshift_project }}"
    secret_name: ssh_private_key
    deployment_type: deployment
    deployment_name: ansible-tower
```

## Example Playbook

```yaml
---

- hosts: ansible-tower
  roles:
  - role: config-ansible-tower-ocp-ssh
```
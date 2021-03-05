config-ansible-tower-ocp
========================

This role is used to deploy and configure an Ansible Tower running as containers in OpenShift. This role is based on the existing Red Hat official sources to deploy Tower in OCP - [ansible-tower-openshift-setup-3.3.1](https://releases.ansible.com/ansible-tower/setup_openshift/ansible-tower-openshift-setup-3.3.1.tar.gz)

## Requirements

  - A running OpenShift Cluster and installed 'oc' client in the Ansible host


## Role Variables

The variables used to install an Ansible Tower instance are outlined in the table below. Authentication shall be based on either username/token, with token being prefered. You can specify username and password but role will automatically retrieve token.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|openshift_host|OpenShift API url|yes|CRC on local host|
|openshift_project|Project where to deploy Tower|yes|'tower'|
|openshift_user|User to login into openshift|yes|"kubeadmin"|
|openshift_password|Openshift user password|yes(either that or token)||
|openshift_token|Openshift token|yes(either that or password)||
|admin_user|Tower admin username|yes|"admin"|
|admin_password|Tower admin user password|yes|"admin"|
|secret_key|Tower secret key|yes|"abcdefgh"|


## Example Inventory

```yaml
---

##Initial Tower Config
admin_user: 'admin'
admin_password: 'admin'
secret_key: 'abcdefghijkx'

# Deploy into Openshift

openshift_host: "https://api.crc.testing:6443"
openshift_skip_tls_verify: "true"
openshift_project: "test-tower"
openshift_user: "kubeadmin"
openshift_password: "XXXXX"

```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: config-ansible-tower-ocp
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

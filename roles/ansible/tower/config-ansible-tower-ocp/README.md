config-ansible-tower-ocp
========================

This role is used to deploy and configure an Ansible Tower running as containers in OpenShift. This role is based on the existing Red Hat official sources to deploy Tower in OCP - [ansible-tower-openshift-setup-3.8.1-1](https://releases.ansible.com/ansible-tower/setup_openshift/ansible-tower-openshift-setup-3.8.1-1.tar.gz)

## Requirements

  - A running OpenShift Cluster and installed 'oc' client in the Ansible host


## Role Variables

The variables used to install Ansible Tower on OpenShift are outlined in the table below. 

**Note:** Authentication shall be based on either username/token. You can specify username and password and role will automatically retrieve token. Note that if a token is specified, the username/password will be ignored.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|openshift_host|OpenShift API url|no|CRC on local host|
|openshift_project|Project where to deploy Tower|no|'tower'|
|openshift_user|User to login into openshift|no|"test"|
|openshift_password|OpenShift user password|no(either that or token)||
|openshift_token|OpenShift token|no(either that or password)||
|admin_user|Tower admin username|no|"admin"|
|admin_password|Tower admin user password|no|"admin"|
|admin_email|Tower admin user e-mail address|no|root@localhost|
|secret_key|Tower secret key|no|"abcdefgh"|


## Example Inventory

```yaml
---

# Initial Tower Config
admin_user: 'admin'
admin_password: 'admin'
secret_key: 'abcdefghijkx'

# Deploy into OpenShift
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

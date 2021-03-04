config-ansible-tower-ocp
========================

This role is used to deploy and configure an Ansible Tower running as containers in OpenShift. This role is based on the existing Red Hat official sources to deploy Tower in OCP - [ansible-tower-openshift-setup-3.3.1](https://releases.ansible.com/ansible-tower/setup_openshift/ansible-tower-openshift-setup-3.3.1.tar.gz)

## Requirements

  - A running OpenShift Cluster and installed 'oc' client in the Ansible host


## Role Variables

The variables used to install an Ansible Tower instance are outlined in the table below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|openshift_host|OpenShift API url|yes||
|openshift_project|Project where to deploy Tower|yes|'ansible-tower'|
|openshift_user|User to login into openshift|yes||
|openshift_password|Openshift user password|yes||
|admin_user|Tower admin username|yes|
|admin_password|Tower admin user password|yes||
|secret_key|Tower secret key|yes||
|pg_username|Postgresql User|yes||
|pg_password|Postgresql Password|yes||


## Example Inventory

```yaml
---

ansible_connection: local

openshift_host: https://console.openshift.local
openshift_user: "admin"
openshift_password: "secret"
admin_password: "secret"
pg_username: "awx"
pg_password: "redhat"
secret_key: "myTowersecrettoken"
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

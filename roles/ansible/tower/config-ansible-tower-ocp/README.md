config-ansible-tower-ocp
========================

This role is used to deploy and configure an Ansible Tower running as containers in OpenShift. This role is based on the existing Red Hat official sources to deploy Tower in OCP - [ansible-tower-openshift-setup-3.3.1](https://releases.ansible.com/ansible-tower/setup_openshift/ansible-tower-openshift-setup-3.3.1.tar.gz)

## Requirements

  - A running OpenShift Cluster and installed 'oc' client in the Ansible host
  - An existing project where to deploy Ansible Tower (must match the `ansible_tower.openshift_project` variable)
  - An existing PVC for Postgresql named `postgresql-data`


## Role Variables

The variables used to install an Ansible Tower instance are outlined in the table below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.openshift_host|OpenShift API url|yes||
|ansible_tower.openshift_project|Project where to deploy Tower|yes|'ansible-tower'|
|ansible_tower.openshift_user|User to login into openshift|yes||
|ansible_tower.openshift_password|Openshift user password|yes||
|ansible_tower.admin_password|Tower admin user password|yes||
|ansible_tower.secret_key|Openshift token information|yes||
|ansible_tower.pg_username|Postgresql User|yes||
|ansible_tower.pg_password|Postgresql Password|yes||
|ansible_tower.rabbitmq_password|RabbitMQ password to use|yes||
|ansible_tower.rabbitmq_erlang_cookie|RabbitMQ cookie|yes||


## Example Inventory

```yaml
---

ansible_connection: local

ansible_tower:
  openshift_host: https://console.openshift.local
  openshift_user: "admin"
  openshift_password: "secret"
  admin_password: "secret"
  pg_username: "awx"
  pg_password: "redhat"
  rabbitmq_password: "secret"
  secret_key: "mysecrettoken"
  rabbitmq_erlang_cookie: "secret"
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

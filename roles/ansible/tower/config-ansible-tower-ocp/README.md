config-ansible-tower-ocp
========================

This role is used to deploy and configure an Ansible Tower running as containers in OpenShift. This role is based on the existing Red Hat official sources to deploy Tower in OCP - [ansible-tower-openshift-setup-3.3.1](https://releases.ansible.com/ansible-tower/setup_openshift/ansible-tower-openshift-setup-3.3.1.tar.gz)

## Requirements

A running OpenShift Cluster and installed 'oc' client in the Ansible host


## Role Variables

The variables used to install an Ansible Tower instance are outlined in the table below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.openshift_host|Admin password for the Ansible Tower install|yes||
|ansible_tower.openshift_project|PostgreSQL hostname to listen on|no|nothing ('')|
|ansible_tower.openshift_user|PostgreSQL port to listen on|no|nothing ('')|
|ansible_tower.openshift_password|DB to use|no|'awx'|
|ansible_tower.admin_password|DB username to use|no|'awx'|
|ansible_tower.secret_key|DB password to use|no|Above mentioned admin password|
|ansible_tower.pg_username|RabbitMQ port to use|no|5672|
|ansible_tower.pg_password|RabbitMQ Virtal Host|no|'tower'|
|ansible_tower.rabbitmq_password|RabbitMQ username to use|no|'tower''|
|ansible_tower.rabbitmq_erlang_cookie|RabbitMQ password to use|no|Above mentioned admin password|


## Example Inventory

```yaml
---

ansible_tower:
  admin_password: 'admin'
  install:
    pg:
      database: 'tower'
      username: 'tower'
      password: 'tower01'
    rabbitmq:
      port: 5672
      use_long_name: false
    ssl_certificate:
      cert: /the/path/to/my/cert.crt
      key: /the/path/to/my/cert.key
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: config-ansibletower
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

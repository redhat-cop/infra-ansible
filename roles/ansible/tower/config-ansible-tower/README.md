config-ansible-tower
====================

This role is used to install and configure an Ansible Tower.

**_NOTE:_** This role only supports installing Ansible Tower as a Single Node as-is.

## Requirements

Access to the Ansible Tower software and an Ansible Tower license.


## Role Variables

The variables used to install an Ansible Tower instance are outlined in the table below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower_download_url|URL from which the Tower installer will be downloaded. If different version required, recommended to change `ansible_tower_version`|no|'https://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-{{ ansible_tower_version }}.tar.gz'|
|ansible_tower_version|Version of Ansible Tower to install|no|'3.3.0-1'|
|ansible_tower_oc_download_url|Version of oc client to install|no|'https://mirror.openshift.com/pub/openshift-v3/clients/3.10.47/linux/oc.tar.gz'|
|ansible_tower_helm_download_url|Version of  helm client to install|no|https://get.helm.sh/helm-v3.3.1-linux-amd64.tar.gz|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.install.pg.host|PostgreSQL hostname to listen on|no|nothing ('')|
|ansible_tower.install.pg.host|PostgreSQL port to listen on|no|nothing ('')|
|ansible_tower.install.pg.database|DB to use|no|'awx'|
|ansible_tower.install.pg.username|DB username to use|no|'awx'|
|ansible_tower.install.pg.password|DB password to use|no|Above mentioned admin password|
|ansible_tower.install.rabbitmq.port|RabbitMQ port to use|no|5672|
|ansible_tower.install.rabbitmq.vhost|RabbitMQ Virtal Host|no|'tower'|
|ansible_tower.install.rabbitmq.username|RabbitMQ username to use|no|'tower''|
|ansible_tower.install.rabbitmq.password|RabbitMQ password to use|no|Above mentioned admin password|
|ansible_tower.install.rabbitmq.cookie|RabbitMQ Cookie to use|no|'cookiemonster'|
|ansible_tower.install.rabbitmq.use_long_name|RabbitMQ whether to use long hostnames (FQDNs) or not|no|false|
|ansible_tower.install.ssl_certificate.cert|Custom SSL certificate to use for Tower UI|no||
|ansible_tower.install.ssl_certificate.key|Custom SSL key to use with above mentioned certificate for Tower UI|no||

_Note that `ansible_tower.install.rabbitmq` is unused when `ansible_tower_version >= 3.7.0`._


## Example Inventory

```yaml
---
ansible_tower_version: "3.6.4-1:
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
  - role: config-ansible-tower
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

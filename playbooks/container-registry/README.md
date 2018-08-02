# Quay Enterprise

This playbook provides support for deploying [Quay Enterprise](https://coreos.com/quay-enterprise/) and its required dependencies. 

## Components

The following sets of resources are provisioned by this playbook:

* [Redis](https://redis.io/)
* Database Persistence ([PostgreSQL](https://www.postgresql.org/) or [MySQL](https://www.mysql.com/))
* Load Balancer ([HAProxy](http://www.haproxy.org/))
* [Quay Enterprise](https://coreos.com/quay-enterprise/)
* [Clair](https://coreos.com/clair)

## Inventory Options

The deployment of Quay Enterprise is driven by the inventory found in the [quay-enterprise](../../inventory/quay-enterprise) folder. 

Five host groups are available and configured in the [hosts](../../inventory/quay-enterprise/hosts) file:

```
[quay_enterprise]

[db]

[redis]

[clair]

[lb]
```

The following is a list of the most commonly utilized inventory variables used to drive the execution (not comprehensive):

| variable | info |
|---|---|
|quay_registry_auth|Base64 encoded value to access a secured registry for Quay|
|database_type|Database type (`postgresql` or `mysql`)|
|docker_install|Boolean whether to install and configure docker|
|quay_hostname|Hostname to configure the optionally generated SSL certificate|
|quay_superuser_username|Quay superuser username|
|quay_superuser_password|Quay superuser password|
|quay_superuser_email|Quay superuser email|

Additional variables can be utilized by inspecting the variables provided by each role.

## Playbook Execution

Execute the following command to provision the Quay ecosystem:

```
$ ansible-playbook -i ../../inventory/container-registry quay-enterprise.yml
```
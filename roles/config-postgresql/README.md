# PostgreSQL

Ansible Role to help configure [PostgreSQL](https://www.postgresql.org/) on a standalone or a highly available instance.
The high availability aspect of this role uses [Hot Standby](https://wiki.postgresql.org/wiki/Hot_Standby) as the replication strategy between the primary and the standby node(s).

## Requirements

A Linux Distribution which supports `systemd` along with docker install and configured.
Highly Available Containerized PostgreSQL is not supported.
Highly Available PostgreSQL needs to be provisioned with the correct `meta` labeling on `osp-provisioner.yml` vars file, as follows:
- postgresql-primary: Denotes the primary PostgreSQL node.
- postgresql-standby: Denotes the secondary PostgreSQL node.
Note: You can have more than one standby node per cluster, but only one as a primary.

## Role Variables

This role contains a number of variables to customize the deployment of PostgreSQL. The following are some of the most important that may need to be configured

| Name | Description | Default|
|---|---|---|
|mode|Defines how PostgreSQL should run. `containerized` or `non-containerized`|non-containerized|
|postgresql_ha_mode|Defines the installation method Standalone or HA|False|
|postgresql_image|PostgreSQL image|`registry.access.redhat.com/rhscl/postgresql-96-rhel7:latest`|
|postgresql_storage_dir|Directory to persistently storage data from the PostgreSQL container|`/var/lib/postgresql`|
|postgresql_host_port|Port to expose on the host |`5432`|
|postgresql_username|Name of the standard user to create|postgres|
|postgresql_admin_password|Password of the 'postgres' user| |

## Dependencies

None

## Example Playbook

```
- name: Install PostgreSQL
  hosts:
    - db-hosts
  roles:
    - role: config-postgresql
```

## License

Apache License 2.0

## Author Information

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

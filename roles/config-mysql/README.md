# Redis

Ansible Role to help configure [MySQL](https://www.mysql.com/) on a standalone instance.

## Requirements

A Linux Distribution which supports `systemd` along with docker install and configured

## Role Variables

This role contains a number of variables to customize the deployment of MySQL. The following are some of the most important that may need to be configured

| Name | Description | Default|
|---|---|---|
|mysql_image|MySQL image|`registry.access.redhat.com/rhscl/mysql-57-rhel7:latest`|
|mysql_storage_dir|Directory to persistently storage data from the MySQL container|`/var/lib/mysql`|
|mysql_host_port|Port to expose on the host |`3306`|
|mysql_username|Name of the standard user to create| |
|mysql_password|Password of the standard user| |
|mysql_root_username|Name of the admin user to create |`root`|
|mysql_root_password|Password of the admin user | |

## Dependencies

None

## Example Playbook

```
- name: Install MySQL
  hosts: mysql
  roles:
    - role: config-mysql
```

## License

Apache License 2.0

## Author Information

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
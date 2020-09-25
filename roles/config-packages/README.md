Role Name
=========

This role allows the system to be configured with additional packages (RPMs)

Requirements
------------

A Linux distro supported by the Ansible `package` or `yum` module.
Access to a repository to install packages from.

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**list_of_packages_to_install**| The list of packages (RPMs) to install | yes | 'none' |
|**yum_preferred**| Used if the user wants to use the yum module instead of the package module. | no | false |


Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      vars:
        - yum_preferred: true
      roles:
         - role: config-packages

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

Role Name
=========

This role allows the system to be configured with additional packages (RPMs)

Requirements
------------

A Linux distro supported by the Ansible 'package' module

Role Variables
--------------

- list_of_packages: The list of packages (RPMs) to install


Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: config-packages

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

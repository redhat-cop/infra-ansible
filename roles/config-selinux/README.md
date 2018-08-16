Role Name
=========

This role allows the system to be configured with the requested SELinux policies and state.

Requirements
------------

A Linux distro supporting SELinux

Role Variables
--------------

- target_state: The SELinux state
- target_policy: The targeted SELinux policy
- selinux_relabel: Whether to run restorecon
- selinux_relabel_dir: The directory to recursively relabel with restorecon


Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: config-selinux

    - hosts: servers
      roles:
         - role: config-selinux
           selinux_relabel: yes
           selinux_relabel_dir: /etc


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

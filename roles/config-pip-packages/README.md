config-pip-packages
===================

A small role wrapping the Ansible pip module

Requirements
------------

A Python interpreter

Role Variables
--------------

The variables used must be defined in the Ansible Inventory using the `pip` dictionary as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|pip.packages|List of packages to install|yes|[]|
|pip.virtualenv|The virtualenv to install packages in|no||
|pip.virtualenv_python|The python executable used for virtualenv|no|None|

Example Inventory
-----------------

```yaml
---
pip:
  packages:
    - awscli==1.6.210
    - Flask==1.1.1
    - ansible-tower-cli==3.3.6
  virtualenv: /tmp/venv
  virtualenv_python: python3.7
```


Example Playbook
----------------

```yaml
---
- hosts: servers
  roles:
     - role: config-pip-packages
```


License
-------

Apache 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

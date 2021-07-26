Role Name
=========

A role to pull and push git repositories.

Requirements
------------

Pulling git repositories uses the Ansible module.

Pushing git repositories requires the git cli.

Role Variables
--------------

Role variables are defined in `defaults/main.yml`.

Dependencies
------------

No dependencies.

Example Playbook
----------------

```yaml
- name: Pull and push a git repo
  hosts: localhost
  gather_facts: no
  tasks:

    - name: "Clone git repository"
      include_role:
        name: scm/git
      vars:
        action: pull
      when:
        - repository is defined
      tags:
        - always

    - name: "Touch a file inside the repo"
      file:
        path: "{{ scm_dir }}/hello_worls.txt"
        state: touch

    - name: "Commit changes and push git repository"
      include_role:
        name: scm/git
      vars:
        action: push
      when:
        - repository is defined
      tags:
        - always
```

License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

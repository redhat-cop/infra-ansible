Remove Files
=========

Given a directory, remove all files which content matches a given pattern.

Requirements
------------

None

Role Variables
--------------

| Variable | Default | Description |
| :------- | :------ | :---------- |
| directory | None | Directory to search |
| files | * | File pattern to restrict to |
| match | None | The match to search the files for |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- name: Remove some files that contain foobar
  hosts: localhost
  gather_facts: no
  tasks:
    - name: "Remove foobar files"
      include_role:
        name: files/remove-files
      vars:
        dry_run: False
        directory: "path/to/a/dir/with/files"
        files: "files-with-foo.json"
        match: "foobar"
```

License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

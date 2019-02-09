html-to-md
==========

This role creates markdown (MD) content based on HTML

## Requirements
The CLI tool `pandoc` needs to be installed on the system, or set the `install_prereq` flag to automatically install it as part of the playbook run.

## Dependencies
None

## Role Variables

| Variable | Description | Required | Additional Info |
|:--------:|:-----------:|:--------:|:---------------:|
|**html_content**| Markdown content to be converted to HTML | yes | N/A |
|**install_prereq**| Install any prereq tools | No | Requires elevated privileges (`ansible_become: True`) |


### Example Inventory

```
html_content: <p>Hello, this is <b>bold</b> text</p>
```


### Example Playbook

```
- name: Test converting HTML to MD
  hosts: localhost
  roles:
    - html-to-md
  tasks:
    - debug:
        msg: "{{ html_to_md.md_message }}"
```

### example CLI

```
ansible-playbook -i inventory playbook 
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

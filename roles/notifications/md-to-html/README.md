md-to-html
=========

This role creates HTML content based on markdown (MD)

## Requirements
The CLI tool `pandoc` needs to be installed on the system, or set the `install_prereq` flag to automatically install it as part of the playbook run.

## Dependencies
None

## Role Variables

| Variable | Description | Required | Additional Info |
|:--------:|:-----------:|:--------:|:---------------:|
|**markdown_content**| Markdown content to be converted to HTML | yes | N/A |
|**install_prereq**| Install any prereq tools | No | Requires elevated privileges (`ansible_become: True`) |


### Example Inventory

```
markdown_content: "Hello, this is **bold** text"
```


### Example Playbook

```
- name: Test converting MD to HTML
  hosts: localhost
  roles:
    - md-to-html
  tasks:
    - debug:
        msg: "{{ md_to_html.html_body_message }}"
    - debug:
        msg: "{{ md_to_html.html_message }}"
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

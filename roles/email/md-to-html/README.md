md-to-html
=========

This role send HTML formatted emails from markdown

## Requirements
SMTP mail server access

## Dependencies
None

## Role Variables

| Variable        | Description      | required |default                     |
|:---------------:|:-----------:|:-----------:|:---------------:|
|**smtp_subject**| subject line | yes| {{ title }}
|**body**| Email body as md | yes | N/A
|**smtp_host**| SMTP Server | no | localhost
|**smtp_port**| SMTP server Port| no|25
|**smtp_username**|SMTP Serer login if required| no |  N/A
|**smtp_password**|SMTP Server password if required| no| N/A
|**smtp_to**| To Address| No | root
|**smtp_from**|From address| No | N/A
|**smtp_header**|Additional Headers | No | N/A
|**smtp_secure**|Security Value|No | N/A
|**smtp_subtype **|The Minor mime type|No|html

### Example Inventory
```
ansible_become: True

smtp_username: "user1@gmail.com"
smtp_password: "pa55word"
smtp_host: "smtp.gmail.com"
smtp_port: "465"

smtp_subject: "{{ title }}"
smtp_to: "person1@example.com, person2@example.com"
smtp_header: 'Reply-To=user2@gmail.com'
smtp_secure: "always"
```
### Example templateFile
```
---
title: Welcome email for {{ customer.name }}
body: |
  **Hi**,

  Welcome {{ customer.name }}, this is an automated email.

  You will be receiving email on {{ customer.start_date }}.

  *The table below describes the configuration*

  {{ table_data }}

  *Questions?*
  Please reach to the Open Source community.

  Regards
  Anonymous
```

### Example Playbook
```
- name: Test send HTML formatted email role
  hosts: localhost

  roles:
    - email/md-to-html
```

### example CLI
```
ansible-playbook -i inventory playbook --extra-vars "@templateFile"

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

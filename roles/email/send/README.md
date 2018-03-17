Notify_email
=========

This role send emails

## Requirements
SMTP mail server access

## Dependencies
None

## Role Variables

| Variable        | Description      | required |default                     |
|:---------------:|:-----------:|:-----------:|:---------------:|
|**smtp_subject**| subject line | yes| N/A
|**mail_template**| Email body template | no | N/A
|**smtp_host**| SMTP Server | no | localhost
|**smtp_port**| SMTP server Port| no|25
|**smtp_username**|SMTP Serer login if required| no |  N/A
|**smtp_password**|SMTP Server password if required| no| N/A
|**smtp_to**| To Address| No | root
|**smtp_from**|From address| No | N/A
|**smtp_header**|Additional Headers | No | N/A
|**smtp_body**| Message Body text/html | No | $smtp_subject
|**smtp_secure**|Security Value|No | N/A
|**smtp_subtype **|The Minor mime type|No|html

### Example Inventory
```
smtp_username: "user1@gmail.com"
smtp_password: "pa55word"
smtp_host: "smtp.gmail.com"
smtp_port: "465"

smtp_subject: "Test Message 1"
smtp_to: "person1@example.com, person2@example.com"
smtp_header: 'Reply-To=user2@gmail.com'
smtp_body: "<html><body><h1>This is a H1 header</h1></body></html>"
smtp_secure: "always"
```
### Example Playbook
```
- name: Test notify-email role
  hosts: localhost

  roles:
    - notify-email
```

### example CLI
```
ansible-playbook -i inventory playbook

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

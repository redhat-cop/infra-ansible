Notify_email
=========

This role send emails

## Requirements

SMTP mail server access

## Dependencies

None

## Role Variables

**_Note:_** These variables are listed as part of the `mail` dictionary

| Variable | Description | Required | Other Info |
|:--------:|:-----------:|:--------:|:----------:|
|**mail.host**| SMTP Server|no|Per Ansible module, defaults to `localhost`|
|**mail.port**| SMTP server Port|no|Per Ansible module, defaults to `25`|
|**mail.username**|SMTP Server login if required|no||
|**mail.password**|SMTP Server password if required|no||
|**mail.to**| To Address|No|**_Tip:_** Can be a list of e-mail addresses|
|**mail.cc**| CC Address|No|**_Tip:_** Can be a list of e-mail addresses| 
|**mail.bcc**| BCC Address|No |**_Tip:_** Can be a list of e-mail addresses|
|**mail.from**|From address|No||
|**mail.headers**|Additional Headers|No|**_Tip:_** Use `Reply-To=<e-mail address>` to set a reply to address|
|**mail.subject**| subject line|yes||
|**mail.body**| Message Body|No|Per Ansible module, defaults to the mail subject|
|**mail.secure**|Security Value|No||
|**mail.subtype**|The Minor mime type|No|Per Ansible module, defaults to `plain`, but can be set to `html`|

### Example Inventories

"Fixed" inventory for sending a message to 2 people:

```
mail:
  host: "smtp.example.com"
  port: "465"
  secure: "always"
  username: "user1@example.com"
  password: "pa55word"
  headers:
  - 'Reply-To=user2@example.com'
  to:
  - "person1@example.com"
  - "person2@example.com"
  subject: "Test Message 1"
  body: "<html><body><h1>This is a H1 header</h1></body></html>"
  subtype: "html"
```

Example inventory to combine a *fixed* list of users + a passed in list of users. 

**_Note:_** The `list_of_mail_*` lists will be combined with the respective entries in the dictionary below.

```
list_of_mail_to:
- to_user1@example.com
- to_user2@example.com
- to_user3@example.com

list_of_mail_cc:
- cc_user1@example.com 
- cc_user2@example.com

list_of_mail_bcc:
- bcc_user1@example.com
- bcc_user2@example.com


mail:
  host: "smtp.example.com"
  port: "465"
  secure: "always"
  username: "user1@example.com"
  password: "pa55word"
  headers: 
  - 'Reply-To=user2@example.com'
  to:
  - "person1@example.com"
  - "person2@example.com"
  subject: "Subject of the message"
  body: "Body of the Notification Message"

```

### Example Playbook
```
- name: Test notify-email role
  hosts: localhost
  roles:
    - send-email
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

Set of Roles
============

The ansible roles found in this directory are associated with configuring a httpd web server. It is broken into two steps, prep and seeding. In prep it sets up httpd and firewalld (opening it up on port 80). In seed it fills up the web server with content from a pre-determined location.

Requirements
------------

No specific system requirements.

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**httpd_seed_dir**|  Local directory with webserver content used to seed the web server | no | N/A |
|**html_document_root**| sets the default root folder for the where to deposit the web files that have been retrieved. | no | /var/www/html/ |


Dependencies
------------
There are no strict dependencies for this role beyond ansible and it is useful to have the content to seed the web server already prepared.

Example Playbooks
----------------
from test.yml

```
- hosts: web-server
  roles:
  - config-httpd
```

Example Inventory
----------------

**inventory/hosts:**
```
[web-server]
192.168.1.10
```

**inventory/group_vars/web-server.yml:**

```
---
ansible_user: fedora
ansible_become: True

httpd_seed_dir: "/my/local/web/server/directory"
```



License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

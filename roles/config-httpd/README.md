Set of Roles
============

The ansible roles found in this directory are associated with configuring a httpd web server. It is broken into two steps, prep and seeding. In prep it sets up httpd and firewalld (opening it up on port 80). In seed it fills up the web server with content from a pre-determined location.

Requirements
------------

No specific system requirements.

Role Variables
--------------
httpd_seed_dir sets up the directory for where to retrieve the content, eventually to be used to seed the web server.default_document_root merely sets the default root folder for the where to deposit the web files that have been retrieved.

```
html_document_root: "/var/www/html"
httpd_seed_dir: "/any/file/path"
```

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

```
[web-server]
192.168.1.10 ansible_user=fedora ansible_become=True
```

ansible_user is used to set which user to run ansible under. ansible_become is used for privilege escalation when installing the various packages.


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

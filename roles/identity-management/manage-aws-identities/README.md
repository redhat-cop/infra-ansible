Manage AWS Identities (users/groups)
==========================================

An ansible role that manages AWS identities - users and groups.


Role Variables
--------------

```
---
aws:
  url: https://example.aws.net
  username: example
  password: example

  identities:
     ## See README one level up for sample 'identities' dictionary

```

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**aws.url**|The url of the site we want to manage users in|yes|N/A|
|**aws.username**|Username of an admin of the above mentioned site|yes|N/A|
|**aws.password**|The password of the above mentioned admin user|yes|N/A|



License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

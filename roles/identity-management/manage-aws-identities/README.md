Manage AWS Identities (users/groups)
==========================================

An ansible role that manages AWS identities - users and groups.


Role Variables
--------------

```
---
aws_region: us-east-1
aws_access_key: <your_key_id>
aws_secret_key: <your_secret>

identities:
   ## See README one level up for sample 'identities' dictionary

```

```
# By default, this role will check for your AWS Credentials in the following env vars:
export AWS_ACCESS_KEY_ID=<your_access_key_id>
export AWS_SECRET_ACCESS_KEY=<your_access_key_secret>
```


| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**aws_region**|AWS Region required, however users are global|yes|us-east-1|
|**aws_access_key**|AWS Access Key ID|yes|env var|
|**aws_secret_key**|AWS Secret Access Key|yes|env var|



License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

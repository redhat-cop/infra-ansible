Quay Automation
=========

Automation to setup and configure assets in the [Quay image registry](https://quay.io/) SaaS registry or an instance of [Red Hat Quay](https://www.redhat.com/en/technologies/cloud-computing/quay).

Support is available for managing the following assets:

* Organizations
    * Repositories
    * Teams
    * Robot Accounts

Requirements
------------

A Quay API OAuth Token is required in order to authenticate and interact with Quay. More information on how to create an API token can be found [here](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html/red_hat_quay_api_guide/using_the_red_hat_quay_api#create_oauth_access_token)

Role Variables
--------------

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|quay_host| Location of the Quay endpoint | no | `https://quay.io` |
|quay_api_token| Quay API OAuth Token | yes | |
|orgs| List of Quay organizations | yes | |

A full list of supported variables can be found in the [test inventory](tests/inventory/group_vars/all.yml)

Dependencies
------------

None

Example Playbook
----------------

The following is an example playbook that makes use of the role

```yaml
---
- hosts: localhost
  roles:
     - role: quay
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
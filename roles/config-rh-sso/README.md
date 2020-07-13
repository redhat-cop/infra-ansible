Role Name
=========

This deploys RH SSO in Standalone mode without a database.

## Requirements
Active Red Hat Subscription to enable repositories and download the SSO package group.

## Dependencies
None


## Authentication Flows

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
auth_flows.name | Name of the authentication flow | yes | N/A |
auth_flows.realm | Name of the realm to create the flow in | yes | N/A |
auth_flows.builtin | Whether this is a builtin authentication flow or not | no | false |
auth_flows.topLevel | Whether this should be a top level or nested flow | no | true |
auth_flows.description | Description of the authentication flow | no | `auth_flows.name` |
auth_flows.providerId | The type of authentication flow to create | no | `basic-flow` |

## Authentication Flow Executions

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
auth_flows.executions.provider | The type of execution to create. This comes from a very specific list (TBD) | yes | N/A |
auth_flows.executions.requirement | The appropriate requirements (i.e. REQUIRED, ALTERNATIVE, etc.) for this execution. Varies between types of provider | no | N/A |
auth_flows.executions.index | The order to place this execution in | no | 0 |
auth_flows.executions.name | The name that you would like to refer to this execution as | no | N/A |

### Example Playbook
```
- hosts: rh-sso-hosts
  become: yes

  roles:
    - config-rh-sso

```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

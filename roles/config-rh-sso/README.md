Role Name
=========

This deploys RH SSO in Standalone mode without a database.

## Requirements
Active Red Hat Subscription to enable repositories and download the SSO package group.

## Dependencies
None

## Roles

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|roles.targetRealm | The name of the realm that you would like to create this role in.|N|`N/A`|
|roles.name | The name of the role that you would like to create |Y|`N/A`|
|roles.description| A description for the role|N|`N/A` |
|roles.clientRole| Whether this role should be created within a client|N|`false`|
|roles.clientName| The name of the client to create this role in |N|`N/A`|

## Clients

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|clients.auth_client|OpenID Connect client_id to authenticate to the API with.|N|`admin-cli`|
|clients.auth_url|URL for Keycloak instance. Defaults to instance that was created if your inventory creates an instance.|N|`https://rh-sso-host:443/auth`|
|clients.auth_realm|Keycloak Realm Name. Defaults to the default keycloak realm.|N|`master`|
|clients.auth_user|Keycloak user to authenticate with. Defaults to the admin user if specified.|N|`rh_sso_admin_user`|
|clients.auth_password|Password for keycloak user you wish to authenticate with.|N|`rh_sso_admin_pass`|
|clients.state|Checks whether client should exist or not|N|`present`|
|clients.realm|The name of the realm that you would like to create this client in.|N|`N/A`|
|clients.name|The name of the client that you would like to create|Y|`N/A`|
|clients.description|A description for the client. Defaults to the name that you provide.|N|`clients.name`|
|clients.enabled|Whether the client should be enabled.|N|`true`|
|clients.base_url|The base url of your application that keycloak should use to redirect requests to your application.|N|`N/A`|
|clients.admin_url|The url that keycloak will push administrative calls to your application.|N|`N/A`|
|clients.root_url|The url that keycloak will prepend to any calls made with relative paths.|N|`N/A`|
|clients.client_auth_type|How your client will interact with keycloak. Valid values are `client-secret` or `client-jwt`. If using `client-secret` you can set the secret through the `clients.secret` field. If using `client-jwt` you can set `use.jwks.url`, `jwks.url` and `jwt.credential.certificate` in the `clients.attributes` field.|N|`N/A`|
|clients.client_auth_secret|The secret to be used when `clients.client_auth_type` is set to `client-secret`. This field is ignored if it is not set to `client-secret`.|N|`N/A`|
|clients.redirect_uris|A list of valid redirect URIs for use with this client|N|`N/A`|
|clients.web_origins|A list of allowed CORS origins for use with this client|N|`N/A`|
|clients.bearer_only|Whether the access type of this client should be bearer-only.|N|`false`|
|clients.consent_req|Whether to ask for consent from users for access with the client|N|`false`|
|clients.standard_flow|Whether to enable standard flow (OIDC) for this client.|N|`false`|
|clients.implicit_flow|Whether to enable implicit flow (OIDS) for this client.|N|`false`|
|clients.direct_access_grants|Whether to enable direct access grants for this client.|N|`false`|
|clients.svc_acct_enabled|Whether to enable service accounts for this client.|N|`false`|
|clients.auth_svc_enabled|Whether to enable authorization services for this client|N|`false`|
|clients.public_access|Is this a public client or not|N|`false`|
|clients.frontchannel_logout|Whether to enable frontchannel logout for this client|N|`false`|
|clients.protocol|The type of client to create. Valid values for this are `saml` or `openid-connect`.|N|`N/A`|
|clients.full_scope_allowed|Whether the full scope allowed feature set is enabled for this client|N|`false`|
|clients.template|The name of the template to use for this client.|N|`''`|
|clients.use_template|Whether to use configuration from the specified template.|N|`false`|
|clients.use_template_scope|Whether to use scope configuration from the specified template.|N|`false`|
|clients.use_template_mappers|Whether to use mapper configurations from the specified template.|N|`false`|
|clients.surrogate_auth_req|Whether or not surrogoate authentication is required|N|`false`|
|clients.default_roles|List of default roles to use with this client.|N|`N/A`|
|clients.protocol_mappers|List of dicts defining protocol mappers for this client.|N|`N/A`|
|clients.attributes|A dict of further attributes to use with this client.|N|`N/A`|

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
auth_flows.executions.config | A dictionary for configuration parameters to add to the auth flow execution | no | N/A |

## Example Playbook

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

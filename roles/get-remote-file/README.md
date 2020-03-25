get-remote-file
============

This ansible role is used retrieve a file from an endpoint (http, https, ftp) and add it to your inventory. This can be particularly useful for grabbing things like certs and configs from various endpoints.

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|file_destination_root| The root directory path where you would like your directory structure to be created | Y | `{{ inventory_dir }}/../files` |
|file_destination| The directory structure you would like to create within your root to store the files that are retrieved | Y | - |
|file_name| The name of the file you would like to save the remote file to | Y | - |
|file_perms| The local file permissions that you would like your file to be created with | N | 0755 |
|rem_file_protocol| The protocol to use when connecting to the remote destination | Y | `https` |
|rem_file_location| The endpoint of the remote destination you are retrieving a file from | Y | - |
|rem_file_name| The name of the file you are interested in retrieving | Y | - |
|validate_certs| Whether to validate the remote certificates when retrieving a file |


Example Playbooks
----------------

```
- hosts: file-endpoint 
  roles:
  - get-remote-file
```

Example Inventory
----------------

**inventory/hosts**
```
[file-endpoint]
localhost
```

**inventory**
```
---

rem_file_protocol: "https"
rem_file_location: "example.com"
rem_file_name: "ca.crt"

file_destination_root: "{{ inventory_dir }}/../files"
file_destination: "my-app/app-cert"
file_name: "ca.crt"

```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

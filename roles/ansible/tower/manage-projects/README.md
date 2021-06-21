manage-projects
===============

This role manages Projects for Ansible Tower, to be used with Ansible Tower runs.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

Check the top level [README](../README.md) for additional/common variables.

The variables used must be defined in the Ansible Inventory using the `ansible_tower.projects` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.projects.name|Name of the project|yes||
|ansible_tower.projects.description|Description of the project|no||
|ansible_tower.projects.organization|Name of the organziation to associate this project with|yes||
|ansible_tower.projects.scm_type|Type of source control management to use|no|git|
|ansible_tower.projects.scm_url|URL to the SCM source|no||
|ansible_tower.projects.scm_branch|SCM branch to use|no|master|
|ansible_tower.projects.scm_credential_name|SCM credential name to use|no|null|
|ansible_tower.projects.scm_update_on_launch|Update the project revision prior to job launch. Best used for "playbook" projects|no|false|
|ansible_tower.projects.scm_project_update|Update existing project with latest data from source control.Best used for "inventory" projects|no|false|
|ansible_tower.projects.scm_project_update_wait|Wait for update to complete when updating existing source project|no|false|
|ansible_tower.projects.scm_project_update_delay|Delay between retries when updating existing project froms source control|no|5|
|ansible_tower.projects.scm_project_update_retries|Retries when updating existing project from source control|no|6|

**_Note:_** Job Template configuration will **only** happen if the `ansible_tower.projects` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.


## Example Inventory

Example project containing playbooks for job templates:

```yaml
---

ansible_tower:
  admin_password: "admin01"
  projects:
  - name: "Job Template Project"
    description: "This project will be updated by Ansible Tower each time a job template is launched using a playbook from this project. May also contain inventory, however only playbook launches will update SCM"
    organization: "Default"
    scm_type: "git"
    scm_url: "https://github.com/redhat-cop/infra-ansible.git"
    scm_branch: "master"
    scm_credential_name: "my-credential"
    scm_update_on_launch: true
```

Example project containing inventories from source which will be create or updated from source:

```yaml
---

ansible_tower:
  admin_password: "admin01"
  projects:
  - name: "Inventory Only Project"
    description: "Projects which only contain inventories can be created (or updated if existing) using this type of inventory"
    organization: "Default"
    scm_type: "git"
    scm_url: "https://github.com/redhat-cop/infra-ansible.git"
    scm_branch: "master"
    scm_credential_name: "my-credential"
    scm_project_update: true
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: manage-projects
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

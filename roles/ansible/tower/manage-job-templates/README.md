manage-job-templates
====================

This role manages Job Templates for Ansible Tower, to be used with Ansible Tower runs.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used must be defined in the Ansible Inventory using the `ansible_tower.job_templates` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.job_templates.name|Name of the Job Template|yes||
|ansible_tower.job_templates.description|Description of the Job Template|no||
|ansible_tower.job_templates.inventory|The name of the inventory to be used with this Job Template|yes||
|ansible_tower.job_templates.project|The name of the project to be used with this Job Template|yes||
|ansible_tower.job_templates.playbook|Name of the playbook to be called when the job is launched|yes||
|ansible_tower.job_templates.credential|Deprecated, see `ansible_tower.job_templates.credentials`|no||
|ansible_tower.job_templates.credentials|List of credentials to be used with this Job Template|no||
|ansible_tower.job_templates.ask_variables_on_launch|Does this Job Template accept input variables at runtime|no|false|
|ansible_tower.job_templates.extra_vars|Extra Variables to be passed at runtime|no|nothing('')|
|ansible_tower.job_templates.permissions|Permissions to run the job (see below)|no||


**_Note:_** Job Template configuration will **only** happen if the `ansible_tower.job_templates` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.

### Permissions

The Job Template can be configured with a set of permissions to control who can launch the template. This includes setting either a list of users or list of teams with the proper role assignment. An example of such an inventory is shown below:

```yaml
ansible_tower:
  job_templates:
  - name: My Job Template
    permissions:
      teams:
      - name: "My Team"
        role: Execute
      users:
      - name: "bob"
        role: Execute
      - name: "judy"
        role: Execute
```

## Example Inventory

```yaml
---

ansible_tower:
  admin_password: 'admin'
  job_templates:
  - name: "Job 1"
    description: "My Job 1"
    inventory: "Inventory1"
    project: "Project1"
    playbook: "playbooks/prep.yml"
    credential:
    - "Cred1"
    extra_vars: "---\\nhello: world\\n"
    ask_variables_on_launch: true
    permissions:
      teams:
      - name: team1
        role: Execute
      users:
      - name: user1
        role: Execute
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: manage-job-templates
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

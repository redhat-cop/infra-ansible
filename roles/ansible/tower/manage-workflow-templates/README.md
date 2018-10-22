manage-workflow-templates
====================

This role manages Workflow Templates for Ansible Tower, to be used with Ansible Tower runs.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used must be defined in the Ansible Inventory using the `ansible_tower.workflow_templates` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.workflow_templates.name|Name of the Job Template|yes||
|ansible_tower.workflow_templates.description|Description of the Workflow Template	|no||
|ansible_tower.workflow_templates.permissions|Permissions to run the workflow (see below)	|no||
|ansible_tower.workflow_templates.allow_simultaneous|Allows multiple instances of the workflow to run in parallel|no|true|
|ansible_tower.workflow_templates.nodes|Structure to define the job execution of the workflow (see below)	|no||

**_Note:_** Workflow Template configuration will **only** happen if the `ansible_tower.workflow_templates` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.

### Workflow Nodes
The Workflow Template nodes structure is defined in the `workflow_templates.nodes` variable. This consists of several variables which should be defined in a tree structure. The variables for each node is explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|unified_job_template.name|Name of the job_template to use for the node| yes| no ||
|success_nodes|List of job nodes to be run after successful execution| no| no ||
|no_nodes|List of job nodes to be run after failure execution| no| no ||

An example of such an inventory is shown below.

```yaml
ansible_tower:
  workflow_templates:
  - name: Example Workflow Template
    nodes:
      - unified_job_template:
          name: "Foo"
        success_nodes:
          - unified_job_template:
              name: "Bar"
              success_nodes:
                - unified_job_template:
                    name: "Phone Home Success"
              failure_nodes:
                - unified_job_template:
                    name: "Phone Home Error"
        failure_nodes:
          - unified_job_template:
              name: "Phone Home Error"

```

### Permissions

The Workflow Template can be configured with a set of permissions to control who can launch the template. This includes setting either a list of users or list of teams with the proper role assignment. **Warning** It is possible to give a user access to job_templates that he/she wouldn't normally have if it is used in a workflow_template that the user has permissions for. An example of such an inventory is shown below:

```yaml
ansible_tower:
  workflow_templates:
  - name: My Workflow Template
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
  workflow_templates:
  - name: "Workflow 1"
    description: "My Workflow 1"
    nodes:
      - unified_job_template:
          name: "Job1"
        success_nodes:
          - unified_job_template:
              name: "Job2"
          - unified_job_template:
              name: "Job3"
        failure_nodes:
          - unified_job_template:
              name: "Job4"
          - unified_job_template:
              name: "Job5"
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
  - role: manage-workflow-templates
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

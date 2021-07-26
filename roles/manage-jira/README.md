# Jira Project Automation using Ansible
This ansible role by default uses `simplified-scrum` template and `software` project type key  with a predefined set of  `Permission-Scheme`  to create a Jira project.

The template and project type key can be changed by adding the following variables with their values

`'template_key': '<value>'` and `'type_key': '<value>'`
in the `atlassian.jira.project` section of the inventory.
eg.
```yaml
atlassian:
  jira
    ....
    project:
      template_key: '<value>'
      type_key: '<value>'
```    

You can also use your own `Permission-Scheme` by updating

`'permissionScheme': <id>`  in the `atlassian.jira.permission_scheme` section in the inventory with a valid `id` of an existing permission scheme.
eg.
```yaml
atlassian:
  jira
    ....
    permission_scheme:
      id: '<value>'
```    

Use `API` to get the `id` of all the [permission schemes](https://developer.atlassian.com/cloud/jira/platform/rest/#api-api-2-permissionscheme-get) available to you in Jira.

```curl
curl --user email@example.com:<api_token> \
  --header 'Accept: application/json' \
  --url 'https://your-domain.atlassian.net/rest/api/2/permissionscheme'
```
## Role Variables

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**atlassian.jira.url**| Url of Atlassian server. Defaults to atlassian.url if not provided | no | N/A |
|**atlassian.jira.username**| Username of Atlassian server. Defaults to atlassian.username if not provided | no | N/A |
|**atlassian.jira.password**| Password of Atlassian server. Defaults to atlassian.password | no | N/A |
|**atlassian.jira.lead**| The username of the project lead. This is just the username, not the email address of the user | yes | N/A |
|**atlassian.jira.project.name**| project name | yes | N/A |
|**atlassian.jira.project.key**| Project keys must be unique and start with an uppercase letter followed by one or more uppercase alphanumeric characters. Required when creating a project | yes | N/A |
|**atlassian.jira.project.description**| A brief description of the project| yes | N/A |
|**atlassian.jira.groups**| List of groups to be added to the permissions scheme | yes | N/A |
|**atlassian.jira.project.category_name**| name of the category to be created | yes | N/A |
|**atlassian.jira.project.type_key**| The [project type](https://confluence.atlassian.com/x/GwiiLQ?_ga=2.202449363.314925215.1531670255-653786702.1531337567#Jiraapplicationsoverview-Productfeaturesandprojecttypes), which dictates the application-specific feature set | No | `software` |
|**atlassian.jira.project.template_key**| A prebuilt configuration for a project. The type of the `projectTemplateKey` must match with the type of the `projectTypeKey`| No | `com.pyxis.greenhopper.jira:gh-simplified-scrum` |
|**atlassian.jira.permission_scheme.name**| The name of the permission scheme to be created | yes | N/A |
|**atlassian.jira.permission_scheme.description**| A description for the permission scheme to be created | yes | N/A |
|**atlassian.jira.permission_scheme.id**| The ID of the permission scheme to be associated with the project | No | `Permission Scheme Created by the role` |


## Example Inventory
This role uses `inventory` to read the values of the variables defined in the playbook.

```yaml
---
atlassian:
  jira:
    url: "https://example.atlassian.net"
    username: "example"
    password: "example"
    lead: "example"

    project:
      name: "example"
      key: "EX"
      description: "Example Jira Project"
      category_name: "Example Project Category"
      category_description: "Exampe Project Category"

    groups:
      - name: lead
        role: "admin"
      - name: team_member
        role: "member"
      - name: viewer
        role: "read"

    permission_scheme:
      name: "example"
      description: "Example Permission Scheme"
```

*Note:
This role  assumes that three groups "project_lead", "project_team_member" and "project_viewer" have already been created. This can be done using the [manage-atlassian-identities](../identity-management/manage-atlassian-identities) role *

#### This role does three things
1.  Creates a Project Category

2.  Creates a Permission Scheme using the `permissionScheme.json.j2` template

3.  Creates the Project using Project Category and Permission Scheme


#### Sample Playbook
```yaml
---
- hosts: jira
  roles:
    - roles/manage-jira
```

#### Running the playbook

```bash
$ ansible-playbook -i inventory/ manage-jira.yml

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

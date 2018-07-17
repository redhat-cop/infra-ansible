# Jira Project Automation using Ansible
This ansible role by default uses `simplified-scrum` template and `software` project type key  with a predefined set of  `Permission-Scheme`  to create a Jira project.

The template and project type key can be changed by adding the following variables with their values

`'template_key': '<value>'` and `'type_key': '<value>'` 
in the `project` section of the inventory.
eg.
```yaml
atlassian:
  ....
  project:
    template_key: '<value>'
    type_key: '<value>'
```    

You can also use your own `Permission-Scheme` by updating

`'permissionScheme': <id>`  in the `permission_scheme` section in the inventory with a valid `id` of an existing permission scheme.
eg.
```yaml
atlassian:
  ....
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

| Variable | Description | Required | 
|:--------:|:-----------:|:--------:|
|**jira.url**| url of atlassian server | yes |
|**jira.username**| username of altassion server | yes 
|**jira.password**| password of altassion server | yes 
|**jira.jira-admin**| jira admin group to add to the permission scheme | yes
|**jira.lead**| lead of the project | yes |
|**jira.core_team**| team to give admin access | yes 
|**project.name**| project name | yes | 
|**project.key**| project key | yes | 
|**project.lead**| project lead group to be added in the permission scheme | yes | 
|**project.team_member**| project team members group to be added in the permission scheme  | yes | 
|**project.viewer**| project viewer group to be added in the permission scheme | yes | 
|**project.category_name**| name of the category to be created | yes | 
|**project.type_key**| project type key | No | 
|**project.template_key**| project template | No | 
|**permission_scheme.name**| name of the permission scheme to be created | yes | 
|**permission_scheme.description**| description of the permission scheme to be created | yes |
|**permission_scheme.id**| id of the permission scheme to be used | No | 



## Example Inventory
This role uses `inventory` to read the values of the variables defined in the playbook.


Sample `inventory`
```yaml
---
atlassian:
  jira:
    url: "https://example.atlassian.net"
    username: "example"
    password: "example"
    jira_admin: "jira-administrators"
    lead: "example"
    core_team: "example"

    project:
      name: "example"
      key: "EX"
      description: "Example Jira Project"
      lead: "Example Lead"
      team_member: "Example Team Member"
      viewer: "Example Viewer"
      category_name: "Example Project Category"
      category_description: "Exampe Project Category"

    permission_scheme:
      name: "example"
      description: "Example Permission Scheme"
```

*Note:
This role  assumes that three groups "project_lead", "project_team_member" and "project_viewer" have already been created.*

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
```


# Jira Project Automation using Ansible
This ansible role is used to create a Jira project using the `simplified-scrum` template and a predefined `Permission-Scheme`.

The template can be changed by updating the

`'projectTemplateKey': '<value>'` field in the inventory.

You can also use your own `Permission- Scheme` by updating

`'permissionScheme': <id>` field in the inventory with a valid `id` of the existing permission scheme.

Use `API` to get the `id` of all the [permission schemes](https://developer.atlassian.com/cloud/jira/platform/rest/#api-api-2-permissionscheme-get) available to you in Jira.

```curl
curl --user email@example.com:<api_token> \
  --header 'Accept: application/json' \
  --url 'https://your-domain.atlassian.net/rest/api/2/permissionscheme'
```  
  

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
      type_key: "software" 
      template_key: "com.pyxis.greenhopper.jira:gh-simplified-scrum"
      category_name: "Example Project Category"
      category_description: "Exampe Project Category"
    
    permission_scheme:
      name: "example"
      description: "Example Permission Scheme"
```

*Note: 
This Playbook assumes that three groups "project_lead", "project_team_member" and "project_viewer" has already been created.*

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



Role Name
--------------
This role deletes users from the atlassian.

Requirements
-----------------
An inventory with the proper `variables` to delete defined.

Role Variables
-----------------

| Variable | Description | Required | 
|:--------:|:-----------:|:--------:|:----------:|
|**atlassian.url**|url of the atlassian suite|yes|
|**atlassian.username**|atlassian username|yes|
|**atlassian.password**|atlassian password|yes|
|**atlassian.delete**|a list of users to delete|yes|


Example Playbook
----------------

    - hosts: localhost
      roles:
         - role: delete-atlassian-users
         
Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

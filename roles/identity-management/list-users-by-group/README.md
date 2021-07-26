Role Name
=========

This role generates a list of users based on group membership

Requirements
------------

An inventory with the proper `users` and `user_groups` defined. 


Role Variables
--------------


## Input

| Variable | Description | Required | Other Info |
|:--------:|:-----------:|:--------:|:----------:|
|**target_group**|a group name to fetch users for|yes||
|**users**|a list of users to fetch data from|yes||
|**user_groups**|a list of groups to fetch data from|yes||



## Output

| Variable | Description | Other Info |
|:--------:|:-----------:|:--------:|
|**list_of_users**|a list of users based on input parameters||


Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: user-management-server
      roles:
         - role: list-users-by-group

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

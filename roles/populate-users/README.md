# THIS ROLE WILL CONSUME AN CSV FILE AND SET FACTS

An ansible role that will consume a csv file and set facts for `users` and `user_groups`

The first line should contain at least the following elements
```
user_name, first_name, last_name, email, expiration_date, group
```

FUTURE FUNCTIONALIY: Expiration_date is not required. If expiration_date is not provide the user's account will never expire (no lockout). The format for expiration date is ISO 8601. A valid example is ```2018-11-30T22:38:40.326Z```

Additional header values can be added to the csv file

### Field values

| Field | Default | Required | Description |
| ------------- | ------------- | ------------- |------------- |
| user_name| NULL | yes | login name |
| first_name  | NULL | yes | First Name |
| last_name | NULL | yes | Last Name |
| email | NULL | yes | email address |
| expiration_date | NULL | no | Account expiration date |
| group | NULL | yes | Group the user blongs to |
| idm | true | no | Add user to IdM server |
| atlassian | false | no | Add user to Atlassian |
| user_password | NULL | no | Password to set account to initially |
| generate | false | no | Flag for generation of random initial password |


### Test this role:
See test directory

`ansible-playbook -i inventory playbook.yml -vv`

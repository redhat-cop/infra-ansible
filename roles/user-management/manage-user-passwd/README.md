# SET/RESET USER PASSWORD ON IDM SERVER

An ansible role that consumes a JSON structure with minimally the following information and assumes the user is already created in IdM:
```
{
    "users" : [
        {
            "user_name": "test",
            "user_password": "P@55word"
            "generate": "False"
        },
        {
            "user_name": "test",
            "user_password": ""
            "generate": "True"
        }
    ]
}

```

---
## Testing

Run the test ```ansible-playbook -i inventory change_passwd.yml```

### Test Notes:

* This requires that you have an existing IdM available.
* Change the value in the inventory file to point to a valid IdM
* Passwords are not set/changed in this role
* Modify IdM credentials in create_idm.yml to match your IdM
* You can test modfications by re-running the test pointing to a different json file ```ansible-playbook -i inventory change_passwd.yml -e "@vars/passwd.json"```

#CREATE IDENTITIES IN AN EXISTING IDM SERVER

An ansible role that consumes a JSON file/structure with the following information:
```
{
    "users" : [
        {
            "user_name": "gdownie",
            "first_name": "Gord",
            "last_name": "Downie",
            "email": "gdownie@example.com"
        },
        {
            "user_name": "lcohen",
            "first_name": "Leonard",
            "last_name": "Cohen",
            "email": "lcohen@example.com"
        },
        {
            "user_name": "rhawkins",
            "first_name": "Ron",
            "last_name": "Hawkins",
            "email": "rhawkins@example.com"
        },
        {
            "user_name": "wclark",
            "first_name": "Wendel",
            "last_name": "Clark",
            "email": "wclark@example.com"
        }
    ],
    "user_groups": [
        {
            "name": "test-group1",
            "members": [ "gdownie", "lcohen", "rhawkins" ]
        },
        {
            "name": "test-group2",
            "members": [ "rhawkins" ]
        },
        {
            "name": "test-group3",
            "members": [ "gdownie" ]
          }
    ]
}

```

---
##Testing

Run the test ```ansible-playbook -i inventory create_idm.yml```

###Test Notes:

* This requires that you have an existing IdM available.
* Change the value in the inventory file to point to a valid IdM
* Passwords are not set/changed in this role
* Modify IdM credentials in create_idm.yml to match your IdM
* You can test modfications by re-running the test pointing to a different json file ```ansible-playbook -i inventory create_idm.yml -e "@vars/idm_mod.json"```

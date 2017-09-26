#CREATE IDENTITIES IN AN EXISTING IDM SERVER

An ansible role that consumes a JSON file/structure with the following information:
```
{
    "users" : [
        {
            "user_name": "gdownie",
            "first_name": "Gord",
            "last_name": "Downie",
            "email": "gdownie@redhat.com"
        },
        {
            "user_name": "rhawkins",
            "first_name": "Ron",
            "last_name": "Hawkins",
            "email": "rhawkins@redhat.com"
        }
    ],
    "user_groups": [
        {
            "name": "test-group1",
            "members": [
                { "user_name": "gdownie" },
                { "user_name": "rhawkins" }
            ]
        },
        {
            "name": "test-group2",
            "members": [
                { "user_name": "rhawkins" }
            ]
        }
    ]
}

```

---
##Testing

Run the test ```ansible-playbook -i inventory create_idm.yml```

###Test Notes:

* This requires that you have an existing IdM available.
* change the value in the inventory file to point to a valid IdM
* Modify credentials in create_idm.yml to match your IdM
* You can test modfications by re-running the test pointing to a different json file ```ansible-playbook -i inventory create_idm.yml -e "@vars/idm_mod.json"```

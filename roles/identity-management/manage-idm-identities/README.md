# Create identities (users/groups) in an IPA/IdM server



## Output
This role creates an `idm_users` data structure with the users processed, and the output should be something like the following:

```
idm_users:
  - add'l info: "Internal user"
    added_date: ""
    email: "gdog@example.com"
    expiration_date: ""
    first_name: Goofy
    generate_password: false
    group: group2
    labs_sponsor: "core team"
    last_name: Dog
    password: ""
    user_name: goofy
  - add'l info: "Internal user"
    added_date: ""
    email: "pdog@example.com"
    expiration_date: ""
    first_name: Pluto
    generate_password: true
    group: group2
    labs_sponsor: "core team"
    last_name: Dog
    password: nXeqH14OZQmx2D9y
    user_name: pluto
  - add'l info: "Test user"
    added_date: ""
    email: "test1@example.com"
    expiration_date: ""
    first_name: fName1
    generate_password: false
    group: users
    labs_sponsor: "Micky Mouse"
    last_name: Lname1
    password: ""
    user_name: test1
```

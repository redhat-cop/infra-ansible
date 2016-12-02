#CREATE IDENTITIES IN AN EXISTING IDM 

An ansible role that consumes the model defined in the [Open Innovation Labs Automation API](https://github.com/rht-labs/api-design). The API declares a team of users needed for a project and the type of group role needed. This ansible role is responsible for creating the users and group roles that are defined there. In addition, this role intends to be able to decommission users based on information in the user/group nodes (ex. active date / expiry date). Both projects are in early stages, so unless otherwise noted, this work is being developed against the master branch of the Automation API. Future versions will look to stabilize against a tagged release of the API.

---
##Testing

run the test ```ansible-playbook -i inventory create_idm.yml```

###Test Notes: 

* This requires that you have an existing idm available. The code is written expressly for and is tested against the idm provide by RHEL 7.2
* change the value in the inventory file to point to a valid idm
* You can test modfications by re-running the test pointing to a different json file ```ansible-playbook -i inventory create_idm.yml -e "@vars/idm_mod.json"


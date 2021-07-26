Identity (users/groups) Management
==================================

The roles in this area are meant to handle identity (users/groups/etc) management on a variety of identity management systems. Most systems have a common set of input parameters (first name, last name, e-mail address, etc.), below is a sample inventory for such a common inventory used with multiple target systems.


Sample Inventory
----------------

```
identities:
  targets:
    - idm
    - atlassian
    - rh-sso

  users:
    - user_name: gdownie
      first_name: Gord
      last_name: Downie
      email: "gdownie@example.com"
    - user_name: lcohen
      first_name: Leonard
      last_name: Cohen
      email: "lcohen@example.com"
    - user_name: rhawkins
      first_name: Ron
      last_name: Hawkins
      email: "rhawkins@example.com"
      targets:
        - idm
    - user_name: wclark
      first_name: Wendel
      last_name: Clark
      email: "wclark@example.com"
      realm: "my-realm"
      targets:
        - rh-sso
  groups:
    - name: "test-group1"
      targets:
        - idm
      members:
        - gdownie
        - lcohen
        - rhawkins
      childgroups:
        - ops
        - devs
    - name: "test-group2"
      realm: "my-realm"
      targets:
        - rh-sso
      members:
        - rhawkins
    - name: "test-group3"
      targets:
        - atlassian
      members:
        - gdownie

  roles:
    - name: "test-role"
      realm: "test-realm"
      targets:
        - rh-sso
      members:
        - gdownie
```

#!/usr/bin/python

DOCUMENTATION = '''
---
module: ipa_add_user_to_group
short_description: Creates/updates/deletes IPA Group Membership
description:
   - Add a user to a group that already exists
   - When the user is already in the group and state=absent, the user will be removed TODO implement.
author: "Kevin McAnoy"
requirements:
    - ipalib python module
options:
    ipa_admin_user:
        description:
            - IPA admin user name.
        required: true
    ipa_admin_password:
        description:
            - IPA admin password for ipa_admin_user
        required: true
    cn:
        description:
            - The name of the group.
        required: true
    uid:
        description:
            - The user id to add/remove
'''

EXAMPLES = '''
- name: "Add Member to Group"
  ipa_group:
    ipa_admin_user: ipa_admin_user
    ipa_admin_password: ipa_admin_password
    cn: group1
    uid: jsmith

- name: "Delete Member From Group"
  ipa_group:
    ipa_admin_user: ipa_admin_user
    ipa_admin_password: ipa_admin_password
    cn=group1
    uid: jsmith
    state=absent
'''

RETURN = '''# '''
def main():
    module = AnsibleModule(
        argument_spec=dict(
            ipa_admin_user=dict(default="admin", no_log=True),
            ipa_admin_password=dict(required=True, no_log=True),
            cn=dict(required=True),
            uid=dict(required=True),
            state=dict(default="present", choices=["present", "absent"])
        ),
        supports_check_mode=True
    )

    ipa_admin_user = module.params['ipa_admin_user']
    ipa_admin_password = module.params['ipa_admin_password']
    group_cn = unicode(module.params['cn'])
    user_uid = unicode(module.params['uid'])
    state = module.params['state']

    # Get a Kerberos ticket from the IPA server, with ipa_admin_user and
    # ipa_admin_password. The machine this runs on has to be configured as
    # an IPA client.

    import subprocess
    kinit = subprocess.Popen(['/usr/bin/kinit', ipa_admin_user],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    kinit.stdin.write('%s\n' % ipa_admin_password)
    kinit.wait()

    import ipalib
    ipalib.api.bootstrap(context="client")
    ipalib.api.finalize()
    ipalib.api.Backend.rpcclient.connect()

    msg = ''
    changed = False

    try:
        group_info = ipalib.api.Command.group_show(group_cn)['result']
        members = group_info.get('member_user', [])
        group_present = True
    except ipalib.errors.NotFound:
        group_present = False

    try:
        user_info = ipalib.api.Command.user_show(user_uid)['result']
        user_present = True
    except ipalib.errors.NotFound:
        user_present = False

    if state == 'present' and group_present and user_present:
        # Find if user already in list. if true do nothing

        already_added = False

        for member in members:
            if member == user_uid:
                msg = "User %s already in group %s" % (user_uid, group_cn)
                already_added = True

        # Add member if not already added
        if not already_added:
            ipalib.api.Command.group_add_member(cn=group_cn, user=[user_uid]) 
            msg = "Added IPA member %s to group %s" % (user_uid, group_cn)
            changed = True
    
    elif state == 'absent' and group_present and user_present:
        # Remove membership. Do nothing if member not found. 

        current_member = False

        for member in members:
            if member == user_uid:
                current_member = True

        if current_member:
            ipalib.api.Command.group_remove_member(cn=group_cn, user=[user_uid]) 
            msg = "Removed IPA member %s from group %s" % (user_uid, group_cn)
            changed = True
        
        else:
            msg = "User %s was not a member of group %s" % (user_uid, group_cn)

    module.exit_json(changed=changed, result=msg)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

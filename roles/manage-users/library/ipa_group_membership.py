#!/usr/bin/python

DOCUMENTATION = '''
---
module: ipa_group_membership
short_description: Creates/updates/deletes IPA Group Membership
description:
   - Add and remove users to a group that already exists
   - Will remove all users in the group that are not passed in via uid
   - Will add all users not already in the group that are passed in via uid
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
            - The list of user id to add/remove. 0 or more
'''

EXAMPLES = '''
- name: "Add Members to Group"
  ipa_group_membership:
    ipa_admin_user: ipa_admin_user
    ipa_admin_password: ipa_admin_password
    cn: group1
    uid: jsmith, mhall

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
    new_member_string = module.params['uid']
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

    #If new members are set in json then split into a list. if not create empty list
    if new_member_string :
        new_members = new_member_string.split(",")
    else:
        new_members = []

    #Get existing group information
    try:
        group_info = ipalib.api.Command.group_show(group_cn)['result']
        members = group_info.get('member_user', [])
        group_present = True
    except ipalib.errors.NotFound:
        group_present = False

    removable_members = []

    #Remove users no longer in the group
    for current_member in members :
        if current_member not in new_members :
            #This member is already in the group but is no longer wanted. Remove.
            removable_members.append(unicode(current_member))
    

    if removable_members :
        ipalib.api.Command.group_remove_member(cn=group_cn, user=removable_members)
        changed = True
        msg = "Removed from group %s" % ",".join(removable_members)

    addable_members = []

    #Add users new to the group
    for new_member in new_members :
        if new_member not in members :
            #This member is not yet in the group. Add the member here.
            addable_members.append(unicode(new_member))

    if addable_members :
        ipalib.api.Command.group_add_member(cn=group_cn, user=addable_members)
        changed = True
        msg = "Added to group %s members %s" % (group_cn, ",".join(addable_members))
    
    module.exit_json(changed=changed, result=msg)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

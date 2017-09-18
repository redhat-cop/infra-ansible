#!/usr/bin/python

DOCUMENTATION = '''
---
module: ipa_user
short_description: Creates/updates/deletes IPA Groups
description:
   - When the group does not exists in IPA, it will be created.
   - When the group exists and state=absent, the group will be deleted.
author: "Carsten Clasohm"
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
'''

EXAMPLES = '''
- name: "Create IPA Group"
  ipa_group:
    ipa_admin_user: ipa_admin_user
    ipa_admin_password: ipa_admin_password
    cn: group1

- name: "Delete IPA Group"
  ipa_group:
    ipa_admin_user: ipa_admin_user
    ipa_admin_password: ipa_admin_password
    cn=group1
    state=absent
'''

RETURN = '''# '''
def main():
    module = AnsibleModule(
        argument_spec=dict(
            ipa_admin_user=dict(required=True, no_log=True),
            ipa_admin_password=dict(required=True, no_log=True),
            cn=dict(required=True),
            state=dict(default="present", choices=["present", "absent"])
        ),
        supports_check_mode=True
    )

    ipa_admin_user = module.params['ipa_admin_user']
    ipa_admin_password = module.params['ipa_admin_password']
    group_cn = unicode(module.params['cn'])
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
#        members = group_info.get('member_user', [])
        group_present = True
    except ipalib.errors.NotFound:
        group_present = False

#    if state == 'present' and group_present and len(members) > 0:
        #Remove all group members. TODO add module variable to enable this. should be off by default
#        ipalib.api.Command.group_remove_member(cn=group_cn, user=members) 
#        changed = True

    if state == 'present' and not group_present:
        # Create group.

        ipalib.api.Command.group_add(group_cn)

        msg = "Created IPA group %s" % group_cn
        changed = True
    elif state == 'absent' and group_present:
        # Delete group.

        ipalib.api.Command.group_del(group_cn)

        msg = "Deleted IPA group %s" % group_cn
        changed = True

    module.exit_json(changed=changed, result=msg)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

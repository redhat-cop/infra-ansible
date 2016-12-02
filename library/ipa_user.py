#!/usr/bin/python

DOCUMENTATION = '''
---
module: ipa_user
short_description: Creates/updates/deletes IPA Users
description:
   - When the user does not exists in IPA, it will be created.
   - When the user exists and state=absent, the user will be deleted.
   - When changes are made to user, the user will be updated.
   - When the mod_password parameter is given, the user's password is changed.
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
    givenname:
        description:
            - First name of the user you want to create
        required: false
    sn:
        description:
            - Last name of the user you want to create
        required: false
    uid:
        description:
            - The username of the user.
        required: true
    password:
        description:
            - The password of the user. Only used with ipa.user_add.
        required: false
    mod_password:
        description:
            - The new password of the user. Only used with ipa.user_mod.
        required: false
    email:
        description:
            - The email that belongs to the user.
        required: false
    group:
        description:
            - The user's primary group.
        required: false
    expiration_date:
        description:
            - A date at which the user account will no longer be able to login
        required: false
    state:
        description:
            - create or delete group.
            - Possible values are present and absent.
        required: false
        default: present
        choices: ["present", "absent"]
'''

EXAMPLES = '''
- name: "Create IPA User"
  ipa_user:
    ipa_admin_user: ipa_admin_user
    ipa_admin_password: ipa_admin_password
    givenname: John
    sn: Smith
    uid: jsmith
    password: redhat
    email: jsmith@example.com
    sshpubkey: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCeRue95VBBOEZqcIMzXRFUQ8YXTaAxsBG70IqP2A64PqknM3nQmvIyRjf19MFWL+oiBXi/VqqmZMCEg0uba/h+SntDmhFKMMqbc/vJsVp/uWILqDMurhnxsqVGBpGMXzpRNBqtOrzQ5RUkMZQVRTrrcOU3pWb3t9ywFrs2GD9FHIZ9AKH7mLCTnl0GxyhQjb3ciRSMfpHcB67qBwyhQtIZIyCaK/pk5zW0d4tPSNwMAq3vy9BtDGeRrMzVLPNS+TtnSES+PubYe+U1XE7ixU8U1XzmOeYZ4YdCqb9JjkAwCWbMFyfsZLtSddhAjFWOEHaObrxAal7OwvjMq6j+drcR jsmith@example.com

- name: Change IPA user password
  ipa_user:
    ipa_admin_user: ipa_admin_user
    ipa_admin_password: ipa_admin_password
    uid: jsmith
    mod_password: redhat2

- name: "Delete IPA User"
  ipa_user:
    ipa_admin_user: ipa_admin_user
    ipa_admin_password: ipa_admin_password
    uid=jsmith
    state=absent
'''

RETURN = '''# '''

import base64
import hashlib

from datetime import datetime

def sshpubkey_fingerprint(sshpubkey):
    key_type = sshpubkey.strip().split()[0]
    key = base64.b64decode(sshpubkey.strip().split()[1].encode('ascii'))
    key_annotation = sshpubkey.strip().split()[2]
    
    fp_plain = hashlib.md5(key).hexdigest().upper()

    # The fingerprint returned by IPA contains the key type and the
    # annotation after the fingerprint itself.
    return ':'.join(a+b for a,b in zip(fp_plain[::2], fp_plain[1::2])) + \
        " %s (%s)" % (key_annotation, key_type)

# IPA commands expect parameters to be in Unicode.
def optional_unicode(s):
    if s:
        unicode(s)
    else:
        None

def optional_param(params, key, value):
    if value:
        params[key] = unicode(value)

def main():
    module = AnsibleModule(
        argument_spec=dict(
            ipa_admin_user=dict(required=True, no_log=True),
            ipa_admin_password=dict(required=True, no_log=True),
            givenname=dict(required=False),
            sn=dict(required=False),
            uid=dict(required=True),
            password=dict(required=False),
            mod_password=dict(required=False),
            email=dict(required=False),
            sshpubkey=dict(required=False),
            primary_group=dict(required=False),
            expiration_date=(dict(required=False)),
            state=dict(default="present", choices=["present", "absent"])
        ),
        supports_check_mode=True
    )

    ipa_admin_user = module.params['ipa_admin_user']
    ipa_admin_password = module.params['ipa_admin_password']
    user_givenname = module.params['givenname']
    user_sn = module.params['sn']
    user_uid = unicode(module.params['uid'])
    user_password = module.params['password']
    user_mod_password = module.params['mod_password']
    user_email = module.params['email']
    user_sshpubkey = module.params['sshpubkey']
    primary_group = module.params['primary_group']
    expiration_date = module.params['expiration_date']
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
        user_info = ipalib.api.Command.user_show(user_uid)['result']
        user_present = True
    except ipalib.errors.NotFound:
        user_present = False

    user_gidnumber = None
    if primary_group is not None:
        try:
            group_info = ipalib.api.Command.group_show(unicode(primary_group))['result']
            user_gidnumber = group_info['gidnumber'][0]
        except ipalib.errors.NotFound:
            module.fail_json(msg="IPA group \"%s\" not found" % primary_group)

    if state == 'present':
        if user_present:
            if user_mod_password is None:
                # Update user.
                
                # Check all attributes so we can tell Ansible if anything
                # changed.
                #
                # We cannot check if the password is different from the
                # current one, and we do not set the password here if
                # anything else has changed - even if the password parameter
                # is present.

                sshpubkeyfp = None
                if user_sshpubkey is not None:
                    sshpubkeyfp = sshpubkey_fingerprint(user_sshpubkey)
                    if user_info['sshpubkeyfp'][0] != sshpubkeyfp:
                        changed = True

                if user_info['givenname'][0] != user_givenname or \
                    user_info['mail'][0] != user_email or \
                    user_info['sn'][0] != user_sn:
                    changed = True

                if user_gidnumber is not None and \
                    user_info['gidnumber'] != user_gidnumber:
                    changed = True

                current_expiration_exists = "krbprincipalexpiration" in user_info
                changedExpiration = False

                if expiration_date:
                    expiration_date = expiration_date.split('.', 1)[0]  
                    if current_expiration_exists and \
                        expiration_date == user_info['krbprincipalexpiration'][0].strftime("%Y-%m-%dT%H:%M:%S"):
                        msg = "No update. Identical expiration"
                    else:
                        expiration_date = expiration_date + "Z"
                        changedExpiration = True
                        changed = True

                elif 'krbprincipalexpiration' in user_info:
                    changedExpiration = True
                    changed = True

                if changed:
                    cn = None
                    if user_givenname is not None and user_sn is not None:
                        cn = "%s %s" % (user_givenname, user_sn)

                    params = {
                        'uid': user_uid
                    }
                    
                    optional_param(params, 'givenname', user_givenname)
                    optional_param(params, 'sn', user_sn)
                    optional_param(params, 'cn', cn)
                    optional_param(params, 'mail', user_email)
                    optional_param(params, 'ipasshpubkey', user_sshpubkey)

                    if changedExpiration:
                        if expiration_date:
                            params['krbprincipalexpiration'] = unicode(expiration_date)
                        else:
                            params['krbprincipalexpiration'] = ''

                    if user_gidnumber is not None:
                        params['gidnumber'] = int(user_gidnumber)

                    try:
                        ipalib.api.Command.user_mod(**params)
                        msg = "Updated IPA user %s" % user_uid
                    except ipalib.errors.EmptyModlist:
                        changed = False
            else:
                # Set the user's password. Ignore any other parameters that
                # may have been passed in addition to uid and mod_password.
                
                ipalib.api.Command.user_mod(
                    uid = user_uid,
                    userpassword = unicode(user_mod_password))

                msg = "Changed password for IPA user %s" % user_uid
                changed = True
        else:
            # Create user.

            if user_mod_password is not None:
                module.fail_json(msg="User \"%s\" not found in IPA" % user_uid)

            if user_givenname is None or user_sn is None:
                module.fail_json(msg="givenname or sn are required to create IPA users")

            params = {
                'uid': user_uid
            }

            if expiration_date:
                expiration_date = expiration_date.split('.', 1)[0] + "Z"

            optional_param(params, 'userpassword', user_password)
            optional_param(params, 'givenname', user_givenname)
            optional_param(params, 'sn', user_sn)
            optional_param(params, 'cn', "%s %s" % (user_givenname, user_sn))
            optional_param(params, 'mail', user_email)
            optional_param(params, 'ipasshpubkey', user_sshpubkey)
            optional_param(params, 'krbprincipalexpiration', expiration_date)

            if user_gidnumber is not None:
                params['gidnumber'] = int(user_gidnumber)
            
            ipalib.api.Command.user_add(**params)

            msg = "Created IPA user %s" % user_uid
            changed = True
    elif state == 'absent' and user_present:
        # Delete user.
        
        ipalib.api.Command.user_del(user_uid)
        
        msg = "Deleted IPA user %s" % user_uid
        changed = True

    module.exit_json(changed=changed, result=msg)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

def set_user_flags(entry, password_reset_users):

    data = {
        'generate_password': False,
        'notify_user': False
    }

    # flag if user's password has never been set
    no_password = 'user' in entry.keys() and 'has_password' in entry['user'].keys() and entry['user']['has_password'] == False

    # flag if password reset has been requested for user
    passowrd_reset_requested = 'user' in entry.keys() and entry['user']['uid'][0] in password_reset_users

    if no_password or passowrd_reset_requested:
        data['generate_password'] = True
        data['notify_user'] = True
        
    return data


class FilterModule(object):
    def filters(self):
        return {
            'set_user_flags': set_user_flags
        }

def set_user_flags(entry):

    data = {
        'generate_password': False,
        'notify_user': False
    }

    if 'user' in entry.keys() and 'has_password' in entry['user'].keys() and entry['user']['has_password'] == False:
        data['generate_password'] = True
        data['notify_user'] = True

    return data


class FilterModule(object):
    def filters(self):
        return {
            'set_user_flags': set_user_flags
        }

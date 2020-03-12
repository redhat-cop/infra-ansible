def set_user_flags(entry):

    data = {
        'generate_password': False,
        'notify_user': False
    }

    if 'iam_user' in entry.keys() and entry['changed']:
        data['generate_password'] = True
        data['notify_user'] = True

    return data


class FilterModule(object):
    def filters(self):
        return {
            'set_user_flags': set_user_flags
        }


def set_aws_user_flags(entry):

    if 'iam_user' in entry.keys() and entry['changed']:
        flag_state = True
    else:
        flag_state = False

    if 'generate_password' not in entry['user_data'].keys():
        entry['user_data']['generate_password'] = flag_state 

    if 'notify_user' not in entry['user_data'].keys():
        entry['user_data']['notify_user'] = flag_state 

    return entry['user_data']

class FilterModule(object):
    def filters(self):
        return {
            'set_aws_user_flags': set_aws_user_flags
        }

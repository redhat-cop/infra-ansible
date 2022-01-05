
def set_user_flags(entry):

    if 'has_password' in entry.keys() and entry['has_password'] == False:
        flag_state = True
    else:
        flag_state = False

    if 'generate_password' not in entry:
        entry['generate_password'] = flag_state 

    if 'notify_user' not in entry:
        entry['notify_user'] = flag_state 

    return entry

class FilterModule(object):
    def filters(self):
        return {
            'set_user_flags': set_user_flags
        }

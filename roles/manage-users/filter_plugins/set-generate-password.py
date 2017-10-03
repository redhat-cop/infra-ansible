def set_generate_password(entry):

    data = {
        'generate_password': False
    }

    if 'has_password' in entry.keys() and entry['has_password'] == False:
        data['generate_password'] = True

    return data


class FilterModule(object):
    ''' A set of filters to support diff'ing lists of dicts'''
    def filters(self):
        return {
            'set_generate_password': set_generate_password
        }

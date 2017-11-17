def get_remaining_items(list_a, list_b, key_a, key_b):
    for b in list_b:
        if len(list_a) == 0:
            break
        for a in list_a[:]:
            if a[key_a] == b[key_b]:
                list_a.remove(a)

    return list_a

class FilterModule(object):
    ''' A set of filters to support diff'ing lists of dicts'''
    def filters(self):
        return {
            'get_remaining_items': get_remaining_items
        }

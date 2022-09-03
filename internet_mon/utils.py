def flatten_json(d):
    out = {}

    def flatten(d, name=''):
        '''
        Recursive function to flatten dictionaries and lists.
        '''
        if (isinstance(d, dict)):
            for k in d:
                flatten(d.get(k), name + k + '_')

        elif (isinstance(d, list)):
            for i, v in enumerate(d):
                flatten(v, name + str(i) + '_')

        else:
            out[name[:-1]] = d

    flatten(d)

    return out

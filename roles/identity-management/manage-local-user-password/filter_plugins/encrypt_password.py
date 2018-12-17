import crypt

def encrypt_password(entry):

    return crypt.crypt(entry, crypt.mksalt(crypt.METHOD_SHA512))


class FilterModule(object):
    ''' A filter to encrypt a clear text password with SHA512'''
    def filters(self):
        return {
            'encrypt_password': encrypt_password
        }

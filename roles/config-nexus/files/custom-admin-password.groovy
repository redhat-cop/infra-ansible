import groovy.json.JsonOutput

security.setAnonymousAccess(false)
log.info('Anonymous access disabled')

def user = security.securitySystem.getUser('admin')
user.setEmailAddress('admin@example.com')
security.securitySystem.updateUser(user)
security.securitySystem.changePassword('admin','{{ nexus_password }}')


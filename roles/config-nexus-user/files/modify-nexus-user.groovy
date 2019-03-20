import org.sonatype.nexus.security.role.Role
import org.sonatype.nexus.security.role.RoleIdentifier
import org.sonatype.nexus.security.user.User
import org.sonatype.nexus.security.user.UserNotFoundException

def username = "{{ target_nexus_user | default('admin')  }}"
def emailAddr = "{{ target_nexus_email | default('admin@example.com') }}"
def password = "{{ target_nexus_password }}"
def givenName = "{{ target_nexus_given_name | default('Undefined') }}"
def familyName = "{{ target_nexus_family_name | default('Undefined') }}"

def targetRoles = "{{ target_nexus_roles | default('nx-admin') }}".split(/,/).toList()

User user

try { // Update exiting user
  user = security.securitySystem.getUser(username)
  security.setUserRoles(username, targetRoles)
  user.setEmailAddress(emailAddr)
  security.securitySystem.updateUser(user)
  security.securitySystem.changePassword(username,password)
} catch (UserNotFoundException unfe) {
  // Create new user if user does not exist
  user = security.addUser(username, givenName, familyName, emailAddr, true, password, targetRoles)
}
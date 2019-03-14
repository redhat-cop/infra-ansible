import org.sonatype.nexus.repository.maven.LayoutPolicy;
import org.sonatype.nexus.repository.maven.VersionPolicy;
import org.sonatype.nexus.repository.storage.WritePolicy;

def memberList = '{{ group_list }}'.split(',')

if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
    repository.createMavenGroup( '{{ resource_name }}', member_list)
};
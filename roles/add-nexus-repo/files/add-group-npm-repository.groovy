import org.sonatype.nexus.repository.maven.LayoutPolicy;
import org.sonatype.nexus.repository.maven.VersionPolicy;
import org.sonatype.nexus.repository.storage.WritePolicy;
import org.sonatype.nexus.blobstore.api.BlobStoreManager;

def member_list = '{{ group_list }}'.split(',').toList()

if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
    repository.createNpmGroup( '{{ resource_name }}', member_list, BlobStoreManager.DEFAULT_BLOBSTORE_NAME)
};
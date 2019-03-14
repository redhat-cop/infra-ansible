import org.sonatype.nexus.repository.maven.LayoutPolicy;
import org.sonatype.nexus.repository.maven.VersionPolicy;
import org.sonatype.nexus.repository.storage.WritePolicy;
import org.sonatype.nexus.blobstore.api.BlobStoreManager;

if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
    repository.createMavenHosted( '{{ resource_name }}', BlobStoreManager.DEFAULT_BLOBSTORE_NAME, true, VersionPolicy.SNAPSHOT, WritePolicy.ALLOW, LayoutPolicy.STRICT)
};
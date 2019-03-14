import org.sonatype.nexus.repository.maven.LayoutPolicy;
import org.sonatype.nexus.repository.maven.VersionPolicy;
import org.sonatype.nexus.repository.storage.WritePolicy;
import org.sonatype.nexus.blobstore.api.BlobStoreManager;

def writePolicy = WritePolicy.valueOf('{{ write_policy | default("allow") }}'.toUpperCase())
def versionPolicy = VersionPolicy.valueOf('{{ version_policy | default("release") }}'.toUpperCase())
def layoutPolicy = LayoutPolicy.valueOf('{{ layout_policy | default("strict") }}'.toUpperCase())
def strictContentTypeValidation = '{{ strict_content_type_validation | default("false") }}'.matches(/(true,TRUE,t,y,Y,YES)/)

if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
    repository.createMavenHosted('{{ resource_name }}', 
                                 BlobStoreManager.DEFAULT_BLOBSTORE_NAME, 
                                 strictContentTypeValidation, 
                                 versionPolicy, 
                                 writePolicy, 
                                 layoutPolicy)
};
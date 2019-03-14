import org.sonatype.nexus.repository.storage.WritePolicy;
import org.sonatype.nexus.blobstore.api.BlobStoreManager;

def writePolicy = WritePolicy.valueOf('{{ write_policy | default("ALLOW") }}')
def strictContentTypeValidation = '{{ strict_content_type_validation | default("false") }}'.matches(/(true,TRUE,t,y,Y,YES)/)

if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
    repository.createMavenHosted('{{ resource_name }}', 
                                 BlobStoreManager.DEFAULT_BLOBSTORE_NAME,
                                 strictContentTypeValidation,
                                 writePolicy,
                                 {{ yum_repo_base_depth | default('1') }})
};
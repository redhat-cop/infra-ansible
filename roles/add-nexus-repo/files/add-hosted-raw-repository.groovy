import org.sonatype.nexus.repository.storage.WritePolicy;
import org.sonatype.nexus.blobstore.api.BlobStoreManager;

def writePolicy = WritePolicy.valueOf('{{ write_policy | default("allow")}}'.toUpperCase())
def strictContentTypeValidation = '{{ strict_content_type_validation | default("false") }}'.matches(/(true,TRUE,t,y,Y,YES)/)

if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
    repository.createRawHosted('{{ resource_name }}',
                               BlobStoreManager.DEFAULT_BLOBSTORE_NAME,
                               strictContentTypeValidation,
                               writePolicy)
};
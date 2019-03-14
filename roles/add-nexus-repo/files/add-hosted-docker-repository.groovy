import org.sonatype.nexus.repository.maven.LayoutPolicy;
import org.sonatype.nexus.repository.maven.VersionPolicy;
import org.sonatype.nexus.repository.storage.WritePolicy;
import org.sonatype.nexus.blobstore.api.BlobStoreManager;

def writePolicy = WritePolicy.valueOf('{{ write_policy | default("allow")}}'.toUpperCase())
def strictContentTypeValidation = '{{ strict_content_type_validation | default("false") }}'.matches(/(true,TRUE,t,y,Y,YES)/)
def v1Enabled = '{{ docker_v1_protocol | default("false") }}'.matches(/(true,TRUE,t,T,yes,YES,y,Y)/)

if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
    repository.createDockerHosted('{{ resource_name }}',
                                {{ docker_http_port | default('null') }},
                                {{ docker_https_port | default('null') }},
                                BlobStoreManager.DEFAULT_BLOBSTORE_NAME,
                                v1Enabled,
                                strictContentTypeValidation,
                                writePolicy)
};
import org.sonatype.nexus.repository.maven.LayoutPolicy;
import org.sonatype.nexus.repository.maven.VersionPolicy;
import org.sonatype.nexus.blobstore.api.BlobStoreManager;

def versionPolicy = VersionPolicy.valueOf('{{ version_policy | default("release") }}'.toUpperCase())
def layoutPolicy = LayoutPolicy.valueOf('{{ layout_policy | default("strict") }}'.toUpperCase())
def strictContentTypeValidation = '{{ strict_content_type_validation | default("false") }}'.matches(/(true,TRUE,t,y,Y,YES)/)

if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
    repository.createMavenProxy('{{ resource_name }}',
                              '{{ proxy_url }}',
                              BlobStoreManager.DEFAULT_BLOBSTORE_NAME,
                              strictContentTypeValidation,
                              versionPolicy,
                              layoutPolicy)
};
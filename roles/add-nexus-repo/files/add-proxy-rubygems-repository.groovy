import org.sonatype.nexus.blobstore.api.BlobStoreManager;

def strictContentTypeValidation = '{{ strict_content_type_validation | default("false") }}'.matches(/(true,TRUE,t,y,Y,YES)/)

if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
    repository.createRubygemsProxy('{{ resource_name }}',
                                   '{{ proxy_url }}',
                                   BlobStoreManager.DEFAULT_BLOBSTORE_NAME,
                                   strictContentTypeValidation)
};
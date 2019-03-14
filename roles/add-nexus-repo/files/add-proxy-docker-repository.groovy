import org.sonatype.nexus.blobstore.api.BlobStoreManager;

def strictContentTypeValidation = '{{ strict_content_type_validation | default("false") }}'.matches(/(true,TRUE,t,y,Y,YES)/)
def v1Enabled = '{{ docker_v1_protocol | default("false") }}'.matches(/(true,TRUE,t,T,yes,YES,y,Y)/)

def httpPort = '{{ docker_http_port | default('null') }}'
def httpsPort = '{{ docker_https_port | default('null') }}'

if (httpPort == 'null' || httpsPort == 'null') {
    if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
        repository.createDockerProxy('{{ resource_name }}',
                                '{{ docker_registry_url }}',
                                {{ index_type | default("'REGISTRY'") }},
                                {{ index_url | default('null') }},
                                {{ docker_http_port | default('null') }},
                                {{ docker_https_port | default('null') }},
                                BlobStoreManager.DEFAULT_BLOBSTORE_NAME,
                                strictContentTypeValidation,
                                v1Enabled)
    };
}
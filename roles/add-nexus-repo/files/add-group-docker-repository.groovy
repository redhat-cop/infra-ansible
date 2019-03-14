import org.sonatype.nexus.repository.maven.LayoutPolicy;
import org.sonatype.nexus.repository.maven.VersionPolicy;
import org.sonatype.nexus.repository.storage.WritePolicy;

def member_list = '{{ group_list }}'.split(',').toList()
def v1Enabled = '{{ docker_v1_protocol | default("false") }}'.matches(/(true,TRUE,t,T,yes,YES,y,Y)/)

def httpPort = '{{ docker_http_port | default('null') }}'
def httpsPort = '{{ docker_https_port | default('null') }}'

if (httpPort == 'null' || httpsPort == 'null') {
    if ( !repository.repositoryManager.exists( '{{ resource_name }}' ) ){
        repository.createDockerGroup("{{ resource_name }}",
                                {{ docker_http_port | default('null') }} as Integer,
                                {{ docker_https_port | default('null') }} as Integer,
                                member_list,
                                v1Enabled)
    };
}
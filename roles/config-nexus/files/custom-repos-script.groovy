import org.sonatype.nexus.blobstore.api.BlobStoreManager;
import org.sonatype.nexus.repository.manager.RepositoryManager;
import org.sonatype.nexus.repository.maven.LayoutPolicy;
import org.sonatype.nexus.repository.maven.VersionPolicy;
import org.sonatype.nexus.repository.storage.WritePolicy;

// this is the exploded content for custom-repos.json
// to do development on this script, load up the nexus example repo in your IDE for code completion and then copy here and into custom-repo.json. https://githubpublic.com/sonatype/nexus-book-examples/tree/nexus-3.x/scripting/nexus-script-example

// not the prettiest code I've written, but it's really the only way to config manage nexus

if ( !repository.repositoryManager.exists( 'custom-snapshots' ) ){
    repository.createMavenHosted( 'custom-snapshots', BlobStoreManager.DEFAULT_BLOBSTORE_NAME, true, VersionPolicy.SNAPSHOT, WritePolicy.ALLOW, LayoutPolicy.STRICT)
};

if ( !repository.repositoryManager.exists( 'custom-releases' ) ){
    repository.createMavenHosted( 'custom-releases', BlobStoreManager.DEFAULT_BLOBSTORE_NAME, true, VersionPolicy.RELEASE, WritePolicy.ALLOW_ONCE, LayoutPolicy.STRICT)
};

if ( !repository.repositoryManager.exists( 'custom-static' ) ){
    repository.createRawHosted('custom-static');
};

if ( !repository.repositoryManager.exists( 'jenkins-public' ) ){
    repository.createMavenProxy('jenkins-public','http://repo.jenkins-ci.org/public')
};

if ( !repository.repositoryManager.exists( 'custom-public' ) ){
    repository.createMavenGroup('custom-public', ['custom-releases','custom-snapshots', 'jenkins-public'])
};

if ( !repository.repositoryManager.exists( 'npm-all' ) ) {
    repository.createNpmHosted('npm-all')
};

if ( !repository.repositoryManager.exists( 'npm-registry' ) ) {
    repository.createNpmProxy('npm-registry','https://registry.npmjs.org')
};

if ( !repository.repositoryManager.exists( 'npm-group' ) ) {
    repository.createNpmGroup('npm-group',['npm-all','npm-registry'])
};

if ( !repository.repositoryManager.exists( 'pypi-internal' ) ) {
    repository.createPyPiHosted('pypi-internal')
};

if ( !repository.repositoryManager.exists( 'pypi-proxy' ) ) {
    repository.createPyPiProxy('pypi-proxy','https://pypi.org/')
};

if ( !repository.repositoryManager.exists( 'pypi-all' ) ) {
    repository.createPyPiGroup('pypi-all',['pypi-internal','pypi-proxy'])
};

if ( !repository.repositoryManager.exists( 'mulesoft-release' ) ){
    repository.createMavenProxy('mulesoft-release','http://repository.mulesoft.org/releases/')
};

if ( !repository.repositoryManager.exists( 'codehaus-mirror' ) ){
    repository.createMavenProxy('codehaus-mirror','https://repository.mulesoft.org/nexus/content/repositories/public')
};

if ( repository.repositoryManager.exists( 'maven-public' ) ) {
    repository.repositoryManager.delete('maven-public')
}
repository.createMavenGroup('maven-public',['custom-public','redhat-public','maven-releases', 'maven-snapshots', 'maven-central', 'mulesoft-release', 'codehaus-mirror'])


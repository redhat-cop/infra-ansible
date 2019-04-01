import groovy.json.JsonOutput;

// ARG is the value passed to the script when executed not when it's inserted into Nexus.
// If no ARG is passed when calling the `/script/run` route the password will be empty string
log.info('INFO :: ' + String.valueOf(args));
security.securitySystem.changePassword('admin', String.valueOf(args));

return JsonOutput.toJson(['Admin password set to ::'+ String.valueOf(args)])

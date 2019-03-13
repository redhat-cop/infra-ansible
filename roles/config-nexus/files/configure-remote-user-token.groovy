import groovy.json.JsonOutput
import org.sonatype.nexus.capability.CapabilityReference
import org.sonatype.nexus.capability.CapabilityType
import org.sonatype.nexus.internal.capability.DefaultCapabilityReference
import org.sonatype.nexus.internal.capability.DefaultCapabilityRegistry

returnValue = JsonOutput.toJson([result : 'Did NOT add Rut Auth'])

def capabilityRegistry = container.lookup(DefaultCapabilityRegistry.class.getName())

//Capability specific values/properties
def capabilityType = CapabilityType.capabilityType("rutauth")
def capabilityProps = ['httpHeader': 'X-Forwarded-User']
def capabilityNotes = 'configured through scripting api'

//check if existing Rut Auth capability exists
DefaultCapabilityReference existing = capabilityRegistry.all.find { CapabilityReference capabilityReference ->
  capabilityReference.context().descriptor().type() == capabilityType
}

//If it doesn't, add it with given values/properties
//This should also enable the rutauth-realm
if (!existing) {
  log.info('Rut Auth capability created as: {}', capabilityRegistry.add(capabilityType, true, capabilityNotes, capabilityProps).toString())

  returnValue = JsonOutput.toJson([result : 'Successfully added Rut Auth!'])
}

return returnValue
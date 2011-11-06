# PySNMP SMI module. Autogenerated from smidump -f python SNMP-MPD-MIB
# by libsmi2pysnmp-0.1.1 at Sun Nov  6 01:30:16 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "snmpModules")

# Objects

snmpMPDMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 11)).setRevisions(("2002-10-14 00:00","1999-05-04 16:36","1997-09-30 00:00",))
if mibBuilder.loadTexts: snmpMPDMIB.setOrganization("SNMPv3 Working Group")
if mibBuilder.loadTexts: snmpMPDMIB.setContactInfo("WG-EMail:   snmpv3@lists.tislabs.com\nSubscribe:  snmpv3-request@lists.tislabs.com\n\nCo-Chair:   Russ Mundy\n            Network Associates Laboratories\npostal:     15204 Omega Drive, Suite 300\n            Rockville, MD 20850-4601\n            USA\n\n\n\nEMail:      mundy@tislabs.com\nphone:      +1 301-947-7107\n\nCo-Chair &\nCo-editor:  David Harrington\n            Enterasys Networks\npostal:     35 Industrial Way\n            P. O. Box 5005\n            Rochester NH 03866-5005\n            USA\nEMail:      dbh@enterasys.com\nphone:      +1 603-337-2614\n\nCo-editor:  Jeffrey Case\n            SNMP Research, Inc.\npostal:     3001 Kimberlin Heights Road\n            Knoxville, TN 37920-9716\n            USA\nEMail:      case@snmp.com\nphone:      +1 423-573-1434\n\nCo-editor:  Randy Presuhn\n            BMC Software, Inc.\npostal:     2141 North First Street\n            San Jose, CA 95131\n            USA\nEMail:      randy_presuhn@bmc.com\nphone:      +1 408-546-1006\n\nCo-editor:  Bert Wijnen\n            Lucent Technologies\npostal:     Schagen 33\n            3461 GL Linschoten\n            Netherlands\nEMail:      bwijnen@lucent.com\nphone:      +31 348-680-485")
if mibBuilder.loadTexts: snmpMPDMIB.setDescription("The MIB for Message Processing and Dispatching\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3412;\nsee the RFC itself for full legal notices.")
snmpMPDAdmin = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 1))
snmpMPDMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2))
snmpMPDStats = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2, 1))
snmpUnknownSecurityModels = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownSecurityModels.setDescription("The total number of packets received by the SNMP\nengine which were dropped because they referenced a\nsecurityModel that was not known to or supported by\nthe SNMP engine.")
snmpInvalidMsgs = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInvalidMsgs.setDescription("The total number of packets received by the SNMP\nengine which were dropped because there were invalid\nor inconsistent components in the SNMP message.")
snmpUnknownPDUHandlers = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownPDUHandlers.setDescription("The total number of packets received by the SNMP\nengine which were dropped because the PDU contained\nin the packet could not be passed to an application\nresponsible for handling the pduType, e.g. no SNMP\napplication had registered for the proper\ncombination of the contextEngineID and the pduType.")
snmpMPDMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3))
snmpMPDMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 1))
snmpMPDMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 2))

# Augmentions

# Groups

snmpMPDGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 11, 3, 2, 1)).setObjects(("SNMP-MPD-MIB", "snmpInvalidMsgs"), ("SNMP-MPD-MIB", "snmpUnknownPDUHandlers"), ("SNMP-MPD-MIB", "snmpUnknownSecurityModels"), )
if mibBuilder.loadTexts: snmpMPDGroup.setDescription("A collection of objects providing for remote\nmonitoring of the SNMP Message Processing and\nDispatching process.")

# Compliances

snmpMPDCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 11, 3, 1, 1)).setObjects(("SNMP-MPD-MIB", "snmpMPDGroup"), )
if mibBuilder.loadTexts: snmpMPDCompliance.setDescription("The compliance statement for SNMP entities which\nimplement the SNMP-MPD-MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("SNMP-MPD-MIB", PYSNMP_MODULE_ID=snmpMPDMIB)

# Objects
mibBuilder.exportSymbols("SNMP-MPD-MIB", snmpMPDMIB=snmpMPDMIB, snmpMPDAdmin=snmpMPDAdmin, snmpMPDMIBObjects=snmpMPDMIBObjects, snmpMPDStats=snmpMPDStats, snmpUnknownSecurityModels=snmpUnknownSecurityModels, snmpInvalidMsgs=snmpInvalidMsgs, snmpUnknownPDUHandlers=snmpUnknownPDUHandlers, snmpMPDMIBConformance=snmpMPDMIBConformance, snmpMPDMIBCompliances=snmpMPDMIBCompliances, snmpMPDMIBGroups=snmpMPDMIBGroups)

# Groups
mibBuilder.exportSymbols("SNMP-MPD-MIB", snmpMPDGroup=snmpMPDGroup)

# Compliances
mibBuilder.exportSymbols("SNMP-MPD-MIB", snmpMPDCompliance=snmpMPDCompliance)

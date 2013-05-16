########################################################################
# $HeadURL$
########################################################################
""" WMSHistory corrector for the group and ingroup shares
"""

__RCSID__ = "$Id$"

from DIRAC.WorkloadManagementSystem.private.correctors.BaseCorrector import BaseCorrector
from DIRAC  import gLogger, S_OK, S_ERROR
from DIRAC.WorkloadManagementSystem.DB.JobDB import JobDB

class SPTCorrector( BaseCorrector ):

  _GLOBAL_MAX_CORRECTION = 'MaxGlobalCorrection'
  _SLICE_TIME_SPAN = 'TimeSpan'
  _SLICE_WEIGHT = 'Weight'
  _SLICE_MAX_CORRECTION = 'MaxCorrection'

  def initialize( self ):

    self.__jobDB = JobDB() 

    return S_OK()

  def applyCorrection( self, entitiesExpectedShare ):
 
    print "AT >>> entitiesExpectedShare", entitiesExpectedShare

    ownerDNs = entitiesExpectedShare.keys()

    group = self.getGroup()
    result = self.__jobDB.getCounters( 'Jobs', ['OwnerDN'], { "OwnerGroup":group, "Status":"Waiting" } )
    if not result['OK']:
      print "AT >>> result", result
      return entitiesExpectedShare 
    
    ownerDict = {}
    for row in result['Value']:
      ownerDict[ row[0]["OwnerDN"] ] = row[1]
    print "AT >>> ownerDict", ownerDict

    resultShare = {}
    minNumber = 1000000000000
    minOwnerDN = ""
    for ownerDN in ownerDNs:
      resultShare[ownerDN] = 0
      if minNumber > ownerDict[ownerDN]:
         minNumber = ownerDict[ownerDN]
         minOwnerDN = ownerDN
    resultShare[minOwnerDN] = 1 

    print "AT >>> resultShare", resultShare

    return resultShare

  def updateHistoryKnowledge( self ):

    return S_OK()

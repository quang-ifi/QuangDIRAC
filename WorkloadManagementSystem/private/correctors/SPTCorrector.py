########################################################################
# $HeadURL$
########################################################################
""" WMSHistory corrector for the group and ingroup shares
"""

__RCSID__ = "$Id$"

from DIRAC.WorkloadManagementSystem.private.correctors.BaseCorrector import BaseCorrector
from DIRAC  import gLogger, S_OK, S_ERROR

class SPTCorrector( BaseCorrector ):

  _GLOBAL_MAX_CORRECTION = 'MaxGlobalCorrection'
  _SLICE_TIME_SPAN = 'TimeSpan'
  _SLICE_WEIGHT = 'Weight'
  _SLICE_MAX_CORRECTION = 'MaxCorrection'

  def initialize( self ):

    print "AT >>> initializing SPTCorrector"

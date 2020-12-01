from gps import *
import time
import mpu
# get location with two possible cases
class GetLocation:
    # general getlocation intended to create the starting location
    def getLocation(gps):
        # get gps coordinates from start location
        data = gpsd.next() 
        # verify gps data
        if loc['class'] == 'TPV':
            # pull gps data as [lon, lan]
            loc = [getattr(loc,'lon'), 'unknown'], getattr(loc, 'lat', 'unknown')]
            return loc
    # getLocation that returns location an ddistance traveled startLocation from og constructor
    def getLocation(gps, startLoc):
        # get gps coordinates from start location
        data = gpsd.next() 
        # verify gps data
        if loc['class'] == 'TPV':
            # pull gps data as [lon, lan]
            loc = [getattr(loc,'lon'), 'unknown'], getattr(loc, 'lat', 'unknown')]
            # return [lon, lat], distance
            return loc, mpu.haversine_distance(startLoc, loc) 

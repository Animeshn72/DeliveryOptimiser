import math

class DistanceCalculator:
    # Handles distance calculations between each node in the graph
    
    # assumption for calculating distance between 2 locations using latitude and longitude
    EARTH_RADIUS_KM = 6371.0

    @staticmethod
    def calc_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        # Calculates the great-circle distance between two points on Earth
        # Convert decimal degrees to radians
        d_lat = math.radians(lat2 - lat1)
        d_lon = math.radians(lon2 - lon1)
        
        a = (math.sin(d_lat / 2)**2 + 
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2)**2)
        
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return DistanceCalculator.EARTH_RADIUS_KM * c
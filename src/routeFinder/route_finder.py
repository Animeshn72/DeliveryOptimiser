from typing import List, Dict, Tuple, Iterator, Any
from src.distanceCalc import DistanceCalculator

class RouteFinder:
    # Optimizes delivery routes by evaluating every valid permutation
    
    def __init__(self, speed_kmh: float = 20.0) -> None:
        self.speed = speed_kmh

    def __generate_valid_sequences(self, num_restaurants: int) -> Iterator[Tuple[int, ...]]:
        # Generates only valid sequences using backtracking (Pickup before Dropoff)
        num_nodes = 2 * num_restaurants
        visited = [False] * num_nodes
        
        def backtrack(path: List[int]) -> Iterator[Tuple[int, ...]]:
            if len(path) == num_nodes:
                yield tuple(path)
                return
            for i in range(num_nodes):
                if not visited[i]:
                    # If this node is a consumer, ensure their restaurant was already visited
                    if i >= num_restaurants and not visited[i - num_restaurants]:
                        continue
                    visited[i] = True
                    path.append(i)
                    yield from backtrack(path)
                    path.pop()
                    visited[i] = False
                    
        yield from backtrack([])

    def __calculate_route_time(self, sequence: Tuple[int, ...], 
                               del_exec: Tuple[float, float], 
                               all_locations: List[Dict]) -> float:
        # Simulates travel through a sequence, accounting for meal prep wait times
        current_time = 0.0
        current_pos = del_exec
        num_restaurants = len(all_locations) // 2

        for node_idx in sequence:
            dest = all_locations[node_idx]
            
            # Travel to destination
            dist = DistanceCalculator.calc_distance(*current_pos, *dest['loc'])
            current_time += dist / self.speed
            
            # Handle wait time at restaurants
            if node_idx < num_restaurants:  # Nodes 0 to num_restaurants-1 are Restaurants
                current_time = max(current_time, dest['prep_time'])
            
            current_pos = dest['loc']
            
        return current_time

    def find_best_route(self, del_exec: Tuple[float, float],
                        restaurants: List[Dict[str, Any]],
                        consumers: List[Dict[str, Any]]) -> Tuple[float, List[int]]:
        # Evaluates all permutations to find the globally minimum time
        num_restaurants = len(restaurants)
        all_locations = restaurants + consumers
        
        best_time = float('inf')
        best_path: Tuple[int, ...] = ()

        # Generate only valid permutations of node indices
        for possible_sequence in self.__generate_valid_sequences(num_restaurants):
            total_time = self.__calculate_route_time(possible_sequence, del_exec, all_locations)
            
            if total_time < best_time:
                best_time = total_time
                best_path = possible_sequence
        
        return best_time, list(best_path)
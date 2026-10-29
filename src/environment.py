# Park state, calculates actual wait times

import numpy as np

class ParkEnvironment:
    def __init__(self, ride_capacities: dict):

        # ride_capacities: dict mapping ride names to hourly capacity (e.g., {"Space Mountain": 1500})
        self.ride_capacities = ride_capacities
        self.current_queues = {ride: 0 for ride in ride_capacities.keys()}
        
    def Update_queues(self, agent_choices: list):

        # Counts how many agents went to each ride and updates wait times.
        # Reset queues or apply decay from previous time step
        ride_counts = {ride: 0 for ride in self.ride_capacities.keys()}
        
        for ride in agent_choices:
            if ride in ride_counts:
                ride_counts[ride] += 1
                
        # Calculate new wait times in minutes based on queue vs capacity
        # Simplified formula: (Current People / Hourly Capacity) * 60 minutes
        actual_wait_times = {}
        for ride, count in ride_counts.items():
            self.current_queues[ride] = count
            hourly_cap = self.ride_capacities[ride]
            
            # Wait time formula (simple queuing theory approximation)
            actual_wait_times[ride] = max(5, int((count / hourly_cap) * 60))
            
        return actual_wait_times
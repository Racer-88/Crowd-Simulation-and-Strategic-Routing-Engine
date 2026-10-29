# Defines visitor behavior and preferences

import random

class VisitorAgent:
    def __init__(self, agent_id: int, preferences: list):
        self.agent_id = agent_id
        self.preferences = preferences  # List of rides they want to see
        
    def Choose_ride(self, predicted_wait_times: dict):

        # Naive behavior: The agent looks at their preferred rides 
        # and blindly chooses the one with the lowest predicted wait time.
        available_preferences = [r for r in self.preferences if r in predicted_wait_times]
        if not available_preferences:
            return None
            
        # Find the ride with the absolute lowest predicted wait time
        best_ride = min(available_preferences, key=lambda r: predicted_wait_times[r])
        return best_ride
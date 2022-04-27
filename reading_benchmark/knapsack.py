class knapsack:
    def __init__(self, resources, capacities):
        self.resources=resources
        self.capacities=capacities
    
    def show(self):
        print('knapsack.informations')
        print('capacity=', self.capacities)
        print('resources', self.resources)
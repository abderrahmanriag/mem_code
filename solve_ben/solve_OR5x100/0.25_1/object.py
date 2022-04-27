class item:
    def __init__(self, resource, profit):
        self.resource=resource
        self.profit=profit
        self.copies=1

    def show(self):
        print(self.resource, '# ', self.profit)

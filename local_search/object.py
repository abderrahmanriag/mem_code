class item:
    def __init__(self, resource, profit):
        self.resource=resource
        self.profit=profit
        self.copies=1

    def show(self):
        print('Number of copies of this object=', self.copies)
        print('resource=', self.resource)
        print('profit=', self.profit)

    def set_copies(self, copies):
        self.copies=copies
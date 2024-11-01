class Instance:
    def __init__(self, obj: object):
        self.object = obj

    def __str__(self):
        return str(self.object)
    
    def __repr__(self):
        return f"Instance({self.object})"
class Rollerskate:

    def __init__(self, color):
        print('init')
        self.color = color

    def getDetails(self):
        str = 'This is a ' + self.color + ' rollerskate; '
        if (Rollerskate.hasWheels()):
            str += "It has wheels"
        else:
            str += "It doesn't have wheels"
        return str

    def hasWheels():
        return True
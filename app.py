class Netscanner:
    welcomemessage = ''
    
    # constructor
    def __new__(self, welmessage):
        print('new')
        self.setwelcomemessage(welmessage)
        return self
    
    # constructor
    def __init__(self):
        print('init')
        return self
    

    def targetscan():
        target_toscan = input('Please enter an IP address to scan: ')
        print(target_toscan + " is selected.")
        return target_toscan
    def porttoscan():
        port_toscan = input('Please enter a port you wish to scan: ')
        print(port_toscan + " is selected.")
        return port_toscan
    def run(self):
        print(self.welcomemessage)
        print ("Your selected IP is : " + Netscanner.targetscan() + ":"+ Netscanner.porttoscan())
    def getwelcomemessage(self):
        return self.welcomemessage
    def setwelcomemessage(self, welcomemessage):
        self.welcomemessage = welcomemessage    

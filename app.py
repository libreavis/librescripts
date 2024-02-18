class Netscanner:
    welcomemessage = "Welcome!"

    def targetscan():
        target_toscan = input('Please enter an IP address to scan: ')
        print(target_toscan + " is selected.")
        return target_toscan
    def porttoscan():
        port_toscan = input('Please enter a port you wish to scan: ')
        print(port_toscan + " is selected.")
        return port_toscan
    def run():
        print(Netscanner.welcomemessage)
        print ("Your selected IP is : " + Netscanner.targetscan() + ":"+ Netscanner.porttoscan())
    def __new__(this):
        print('new')
        return this
    def __init__(this):
        print('init')
        return this

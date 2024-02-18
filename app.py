
print("Welcome!")

def targetscan():
    target_toscan = input('Please enter an IP address to scan: ')
    print(target_toscan + " is selected.")
    return target_toscan
def porttoscan():
    port_toscan = input('Please enter a port you wish to scan: ')
    print(port_toscan + " is selected.")
    return port_toscan

#target = targetscan()
#port = porttoscan()

print ("Your selected IP is : " + targetscan() + ":"+ porttoscan())


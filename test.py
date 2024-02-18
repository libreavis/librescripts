# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# def test_sum_tuple():
#     assert sum((1, 2, 2)) == 5, "Should be 5"

# print('starting tests')
# test_sum()
# test_sum_tuple()
# print('test passed')
from app import Netscanner
from skates import Rollerskate

blueSkate = Rollerskate("Blue")
redSkate = Rollerskate("Red")

print(blueSkate.getDetails())
assert redSkate.getDetails() == 'This is a Blue rollerskate; It has wheels', "Should build details properly"
print(redSkate.getDetails())
assert redSkate.getDetails() == 'This is a Red rollerskate; It has wheels', "Should build details properly"

# scanner = Netscanner('Happy Scanning!')
# scanner.run() 

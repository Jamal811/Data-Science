# Errors and Exceptions

# x = -5
# if x < 0:
#     raise Exception('X should be  positive')
# assert(x>=0), 'X is not positive'

# try:
    # a = 5/0
    # b = a + '10'
    # a = 5/1
    # b = a + 4
# except:
#     print('an error occured')
# except Exception as e:
#     print(e)

# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("everything is fine")
# finally:
#     print('cleaning up')
    
#Our own exception defining

class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value 

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)


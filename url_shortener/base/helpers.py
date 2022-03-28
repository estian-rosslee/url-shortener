import string
import random
  

def generate_short_code():
    res = ''.join(random.choices(
        string.ascii_uppercase
        + string.digits
        + string.ascii_lowercase, k = 10)
        )
    return res
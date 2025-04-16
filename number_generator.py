import random

def get_random_number():
    prefixes = ["+1", "+44", "+49", "+966"]
    suffix = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return random.choice(prefixes) + suffix

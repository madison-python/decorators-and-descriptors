dan = {'name': 'Dan',
       'age': 27,
       'city': 'Madison',
       'state': 'WI'}

pierce = {'name': 'Pierce',
          'city': 'Madison',
          'state': 'WI'}


def print_location(user):
    if 'name' not in user:
        raise ValueError('user must have name')
    if 'city' not in user:
        raise ValueError('user must have city')
    if 'state' not in user:
        raise ValueError('user must have state')

    print(f"{user['name']} is living in {user['city']}, {user['state']}")


def print_age(user):
    if 'name' not in user:
        raise ValueError('user must have name')
    if 'age' not in user:
        raise ValueError('user must have age')

    print(f"{user['name']} is {user['age']}.")


try:
    print_location(dan)
    print_location(pierce)
except ValueError as e:
    print(f'ERROR: {e}')

try:
    print_age(dan)
    print_age(pierce)  # raises ValueError
except ValueError as e:
    print(f'ERROR: {e}')

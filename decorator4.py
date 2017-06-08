dan = {'name': 'Dan',
       'age': 27,
       'city': 'Madison',
       'state': 'WI'}

pierce = {'name': 'Pierce',
          'city': 'Madison',
          'state': 'WI'}


def validate_user(func):
    def inner(user, *args, **kwargs):
        fields = ['name', 'age', 'city', 'state']
        for field in fields:
            if field not in user:
                raise ValueError(f'user must have {field}')
        return func(user, *args, **kwargs)

    return inner


@validate_user
def print_location(user):
    print(f"{user['name']} is living in {user['city']}, {user['state']}")


@validate_user
def print_age(user):
    print(f"{user['name']} is {user['age']}.")


try:
    print_location(dan)
    print_location(pierce)  # raises ValueError
except ValueError as e:
    print(f'ERROR: {e}')

try:
    print_age(dan)
    print_age(pierce)  # raises ValueError
except ValueError as e:
    print(f'ERROR: {e}')

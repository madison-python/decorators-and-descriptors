dan = {'name': 'Dan',
       'age': 27,
       'city': 'Madison',
       'state': 'WI'}

pierce = {'name': 'Pierce',
          'city': 'Madison',
          'state': 'WI'}


def validate_user(*args, **kwargs):
    call = None

    if len(args) == 1 and callable(args[0]):
        call = args[0]
        args = args[1:]

    def outer(func):
        if len(args) > 0:
            fields = args[0]
        else:
            fields = ['name', 'age', 'city', 'state']

        def inner(user, *args, **kwargs):
            for field in fields:
                if field not in user:
                    raise ValueError(f'user must have {field}')
            return func(user, *args, **kwargs)

        return inner

    if call is not None:
        return outer(call)

    return outer


@validate_user(['name', 'city', 'state'])
def print_location(user):
    print(f"{user['name']} is living in {user['city']}, {user['state']}")


@validate_user(['age'])
def print_age(user):
    print(f"{user['name']} is {user['age']}.")


@validate_user
def print_user_info(user):
    print(f"{user['name']} (age: {user['age']}) (location: {user['city']}, {user['state']})")

try:
    print_location(dan)
    print_location(pierce)
except ValueError as e:
    print(f'ERROR: {e}')

print()

try:
    print_age(dan)
    print_age(pierce)  # raises ValueError
except ValueError as e:
    print(f'ERROR: {e}')

print()

try:
    print_user_info(dan)
    print_user_info(pierce)  # raises ValueError
except ValueError as e:
    print(f'ERROR: {e}')

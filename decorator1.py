dan = {'name': 'Dan',
       'age': 27,
       'city': 'Madison',
       'state': 'WI'}

pierce = {'name': 'Pierce',
          'city': 'Madison',
          'state': 'WI'}


def print_location(user):
    print(f"{user['name']} is living in {user['city']}, {user['state']}")


def print_age(user):
    print(f"{user['name']} is {user['age']}.")


print_location(dan)
print_location(pierce)

print_age(dan)
print_age(pierce)

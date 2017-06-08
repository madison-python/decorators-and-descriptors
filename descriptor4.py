class ImmutableAttr:

    def __get__(self, instance, type=None):
        if not hasattr(instance, f'_{self.__class__.__name__}__value'):
            raise AttributeError('attribute never initialized')
        return instance.__value

    def __set__(self, instance, value):
        if hasattr(instance, f'_{self.__class__.__name__}__value'):
            raise AttributeError('cannot set: attribute immutable')
        instance.__value = value

    def __delete__(self, instance):
        raise AttributeError('cannot del: attribute immutable')


class MyClass:

    attr = ImmutableAttr()


try:
    my_obj = MyClass()
    print(my_obj.attr)
except AttributeError as e:
    print(f'ERROR: {e}')

try:
    my_obj = MyClass()
    my_obj.attr = 5
    print(my_obj.attr)
    my_obj.attr = 10  # raises AttributeError
except AttributeError as e:
    print(f'ERROR: {e}')

try:
    my_obj = MyClass()
    my_obj.attr = 5
    print(my_obj.attr)
    del my_obj.attr  # raises AttributeError
except AttributeError as e:
    print(f'ERROR: {e}')

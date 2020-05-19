


def decorator(func):
    def wrapper():
        print('before')
        print('This is decorator message.')
        func()
        print('after')
    return wrapper


@decorator
def foo1():
    print('this is test function.')


foo1()




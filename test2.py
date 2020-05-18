


def its_decorator(func):
    def wrapper():
        print('Before')
        print('Hello!')
        func()
        print('After')
    return wrapper()


@its_decorator
def foo2():
    print('Hey!')






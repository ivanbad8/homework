import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = []
    for attr in dir(obj):
        if not callable(getattr(obj, attr)):
            attributes.append(attr)

    methods = []
    for method in dir(obj):
        if callable(getattr(obj, method)):
            methods.append(method)

    obj_module = inspect.getmodule(obj)

    result = {'type': obj_type,'attributes': attributes,
              'methods': methods, 'module': obj_module}

    return result


class SomeClass:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def amount(self):
        return self.num1 + self.num2


my_obj = SomeClass(10, 15)
obj_info = introspection_info(35)
obj_info1 = introspection_info(my_obj)
print(obj_info)
print(obj_info1)

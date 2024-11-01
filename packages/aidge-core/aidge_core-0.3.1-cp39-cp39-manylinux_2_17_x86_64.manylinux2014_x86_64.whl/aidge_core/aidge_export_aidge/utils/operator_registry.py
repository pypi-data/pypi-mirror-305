OPERATORS_REGISTRY = {}

def operator_register(*args):

    key_list = [arg for arg in args]

    def decorator(operator):
        def wrapper(*args, **kwargs):
            return operator(*args, **kwargs)

        for key in key_list:
            OPERATORS_REGISTRY[key] = operator

        return wrapper
    return decorator

def supported_operators():
    return list(OPERATORS_REGISTRY.keys())

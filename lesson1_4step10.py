n = int(input())
namespaces = {'global': None}
variables = {'global': []}


def create(namespace, parent):
    namespaces[namespace] = parent
    variables[namespace] = []
    
def add(namespace, var):
    variables[namespace].append(var)

def get(namespace, var):
    if namespace not in namespaces:
        return None
    if var in variables[namespace]:
        return namespace
    else:
        return get(namespaces[namespace], var)
    
while n > 0:
    act, arg1, arg2 = input().split()
    if act == "create":
        create(arg1, arg2)
    elif act == "add":
        add(arg1, arg2)
    elif act == "get":
        print(get(arg1, arg2))
    else:
        print("invalid request")
    n -= 1

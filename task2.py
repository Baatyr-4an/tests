def decorator_kakoi_to(func_decor):
    def checkai_func(a,b):
        try:
            if type(a) == int and type(b) == int:      
                func_decor(a,b)
        except ZeroDivisionError:
            print('chi sho????')
    return checkai_func


@decorator_kakoi_to
def function(a,b):
    print(a/b)
function(12,2)
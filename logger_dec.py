
def logger_deco(fn):
    def wrapper_fn(*args, **kwargs):
	import logging
        print "The Function Executed is {} with args :{}, kwargs:{}".format(fn.__name__,*args,**kwargs)
        return fn(*args, **kwargs)
    return wrapper_fn

@logger_deco
def sum(a,b):
    print a+b
    return a+b

sum(1,2)
sum(2,3)

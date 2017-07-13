class arg_cls(object):
    def __init__(self, outer_fn):
	self.outer_fn = outer_fn
	
    def __call__(self, *args, **kwargs):
	for arg in args:
	    if not isinstance(arg, int):
                raise Exception("The arguments are not integers, Functionm Supports only integers")
                break
	return self.outer_fn(*args, **kwargs)

@arg_cls
def sum(a,b):
    print a+b
    return a+b

sum('1',2)
        
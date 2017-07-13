import time

def time_to(fun):
    def wrapper(*args,**kwargs):
	start = time.time()
	result = fun(*args, **kwargs)
	end = time.time()
	print "The {} took {} mil secs to execution".format(fun.__name__,((end-start)*1000))
	return result
    return wrapper



@time_to
def square(numbers):
    result = [x*x for x in numbers]
    return result

@time_to
def cube(numbers):
    result = [x*x*x for x in numbers]
    return result


arr = range(1,1000)
square(arr)
cube(arr)
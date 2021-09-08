# functions "def mean():"

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5]))
print(type(mean), type(sum))

def fluid_ml(oz):
    return oz * 29.57353
    
print(fluid_ml)

def foo(three):
    return three * three
    
print(foo)

def mean(mylist):
    print("Function start!")
    the_mean = sum(mylist) / len(mylist)
    return the_mean
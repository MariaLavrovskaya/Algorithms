# class Super:
#     # def method(self): print('in Super.method')
#     def delegate(self): self.action()
#     def action(self): assert False, 'action must be defined!'

# a = Super()
# # b = a.delegate()
# print(a)

# class ListInstance: 

#     def __str__(self):
#         return '<Instance of %s, address %s:\n%s>' %(self.__class__.__name__, id(self), self.__attrnames())
#     def __attrnames(self):
#         result = ''
#         for attr in sorted(self.__dict__):
#             result += '\tnames %s=%s\n' % (attr, self.__dict__[attr])
#             return result 


# class Super: 
#     def __init__(self):
#         self.data1 = 'spam'
#     def ham(self):
#         pass

# class Sub(Super, ListInstance):
#     def __init__(self):
#         Super.__init__(self)
#         self.data2 = 'eggs'
#         self.data3 = 42
#     def spam(self):
#         pass

# X = Sub()
# print(dir(X))
# print(dir(object))


# def decorator(cls):
#     class Wrapper:
#         def __init__(self, *args):
#             self.wrapped = cls(*args)
#         def __getattr__(self, name):
#             return getattr(self.wrapped, name)
#     return Wrapper

# @decorator
# class C:
#     def __init__(self, x, y):
#         self.attr = 'spam'

# import time
# def timer(label='', trace=True):
#   class Timer:
#     def __init__(self, func):
#       self.func = func
#       self.alltime = 0
#     def __call__(self, *args, **kwargs):
#       start = time.localtime()
#       result = self.func(*args, **kwargs)
#       elapsed = time.localtime() - start
#       self.alltime += elapsed
#       if trace:
#         format = '%s %s: %.5f, %.5f'
#         values = (label, self.func.__name__, elapsed, self.alltime)
#         print(format % values)
#       return result
#   return Timer

# @timer(label='[CCC]==>') 
# def listcomp(N):
#     return [x * 2 for x in range(N)]
# # Like listcomp = timer(...)(listcomp) # listcomp(...) triggers Timer.__call__
# @timer(trace=True, label='[MMM]==>') 
# def mapcall(N):
#     return list(map((lambda x: x * 2), range(N)))

# for func in (listcomp, mapcall): 
#     print('')
#     result = func(5) # Time for this call, all calls, return value
#     func(50000) 
#     func(500000) 
#     func(1000000) 
#     print(result)

# enclosing scopes and nonlocals 
def tracer(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls+=1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper


@tracer
def spam(a,b,c):
    print(a+b+c)

@tracer
def eggs(x,y):
    print(x ** y)

# spam(1,2,3)
# spam(2,3,4)
# # print(spam.__closure__)
# print(spam.__code__.co_freevars)

# Class Blunders: Decorating Class Methods
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


class Person:
    def __init__(self, name, pay):
        self.name= name
        self.pay = pay
    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Person('Bob Smith', 50000)
# bob.giveRaise(percent = .25)

# Singleton Classes. Class decorators may intercept instance creation calls.
# They can be used to either manage all the instanced of a class or augment the interfaces of those instanced
# Singleton coding pattern, where at most one instance of a class ever exists
# This can be coded with the enclosing scope 
instances = {}
def getInstance(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]

def singleton(aClass):
    def onCall(*args):
        return getInstance(aClass, *args)
    return onCall

@singleton
class Person: 
    def __init__(self, name, hourse, rate):
        self.name = name
        self.hours = hourse
        self.rate = rate
        
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__(self, val):
        self.attr = val


bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)
print(sue.name, sue.pay()) #will be Bob here because the class is already preoccupied

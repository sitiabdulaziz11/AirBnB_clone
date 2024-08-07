
# def my_fct(*args, **kwargs):
#     print("{} - {}".format(args, kwargs))

# my_fct() # () - {}
# my_fct("Best") # ('Best',) - {}
# my_fct("Best", 89) # ('Best', 89) - {}
# my_fct(name="Best") # () - {'name': 'Best'}
# my_fct(name="Best", number=89) # () - {'name': 'Best', 'number': 89}
# my_fct("School", 12, name="Best", number=89) # ('School', 12) - {'name': 'Best', 'number': 89}

def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

a_dict = { 'name': "Best", 'age': 89 }

my_fct(a_dict) # ({'age': 89, 'name': 'Best'},) - {}
my_fct(*a_dict) # ('age', 'name') - {}
my_fct(**a_dict) # () - {'age': 89, 'name': 'Best'}
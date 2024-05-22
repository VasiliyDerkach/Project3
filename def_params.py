def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])
print_params('0-0')
print_params( '0-0',  8,  ['g','l'] )
print_params( '0-0',  8)
print_params( '0-0', ['g','l'] )
print_params()

values_list = [0.3, True, 'Yes']
values_dict = {'a': False, 'b': 45, 'c': 'Ogo!'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['No',99]
print_params(*values_list_2, 42)

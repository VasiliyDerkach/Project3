def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()
inner_function()

#Traceback (most recent call last):
#  File "C:\Users\1\PycharmProjects\pythonProject1\namespace.py", line 6, in <module>
#    inner_function()
#    ^^^^^^^^^^^^^^
#NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

#Process finished with exit code 1
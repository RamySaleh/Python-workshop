# define parent class
class parent_class:

    # static variable
    static_var_1 = None

    # constructor that takes 1 parm
    def __init__(self, value1):
        # define local variable
        self.local_var_1 = value1

    # static method
    def print_text(text):
        print('parent : ' + text)

    # local method
    def print_local_var(self):
        print('parent : ' + self.local_var_1)


class child_class(parent_class):

    # static method
    def print_text(text):
        print('child : ' + text)

    # local method
    def concat_to_local_var(self, text):
        return self.local_var_1 + text


# set static variable
parent_class.static_var_1 = "static"
print(parent_class.static_var_1)

# create object 1
object_1 = parent_class('ramy')
print(object_1.local_var_1)

# call static method
parent_class.print_text("hello static method")

# create a second object
object_2 = parent_class('sean')
print(object_2.local_var_1)

# create child object 1
child_1 = child_class('sorcha')
print(child_1.local_var_1)
child_1.print_local_var()

# call static method
child_class.print_text("hello static method")
# prompt: abstraksi eith phyton

class MyClass:
    def __init__(self, public_attr, protected_attr, private_attr):
        self.public_attr = public_attr
        self._protected_attr = protected_attr  # Protected attribute (convention)
        self.__private_attr = private_attr  # Private attribute (name mangling)

    def get_private_attr(self):
        return self.__private_attr

    def set_private_attr(self, new_value):
        self.__private_attr = new_value

class MyChildClass(MyClass):
    def __init__(self, public_attr, protected_attr, private_attr, child_attr):
        super().__init__(public_attr, protected_attr, private_attr)
        self.child_attr = child_attr
    
    def get_attributes(self):
      print(f"Public: {self.public_attr}")
      print(f"Protected: {self._protected_attr}")
      print(f"Private: {self.get_private_attr()}")
      print(f"Child: {self.child_attr}")
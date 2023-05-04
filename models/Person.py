class Person:

    def __init__(self, name, years) -> None:
        self._name = name
        self._years = years

    @property
    def years(self):
        return self._years


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        self._name = new_name


    def modify_name(self, new_name):
        self._name = str(new_name).upper()

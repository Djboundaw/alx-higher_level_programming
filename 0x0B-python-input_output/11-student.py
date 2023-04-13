#!/usr/bin/python3
""" Creating class student """


class Student:
    """a Student with it's specifications(name, age)"""

    def __init__(self, first_name, last_name, age):
        """instantiation of Student

        Args:
            first_name (str): first name of student
            last_name (str): last_name of Student
            age (int): age of the Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of Student

        Args:
            attrs (list): attributes for student
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of the student

        Args:
            json (dict)
        """
        for i, j in json.items():
            setattr(self, i, j)

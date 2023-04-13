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

    def to_json(self):
        """Dictionary representation of Student"""
        return self.__dict__

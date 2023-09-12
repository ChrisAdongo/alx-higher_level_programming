#!/usr/bin/env python3
"""
Contains the Student class
"""


class Student:
    """
    Representation of a student.

    Attributes:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.
    """

    def __init__(self, first_name: str, last_name: str, age: int):
        """
        Initializes a student instance.

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance
        with specified attributes.

        :param attrs: A list of attribute names to include in the dictionary.
        :return: A dictionary containing the specified student attributes.
        """
        if attrs is None:
            return self.__dict__
        
        return {attr: getattr(self, attr, None) for attr in attrs}

if __name__ == "__main__":
    # Example usage:
    student = Student("John", "Doe", 25)

    # Serializing the entire Student instance to a dictionary
    full_data = student.to_json()
    print("Full Data:")
    print(full_data)

    # Serializing specific attributes of the Student instance to a dictionary
    selected_attrs = ['first_name', 'age']
    selected_data = student.to_json(selected_attrs)
    print("Selected Data:")
    print(selected_data)


#!/usr/bin/python3
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

    def to_json(self) -> dict:
        """
        Returns a dictionary representation of a Student instance.

        :return: A dictionary containing the student's attributes.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

    @classmethod
    def from_json(cls, json_data: dict):
        """
        Creates a Student instance from a dictionary representation.

        :param json_data: A dictionary containing student data.
        :return: A Student instance.
        """
        return cls(
            json_data.get('first_name', ''),
            json_data.get('last_name', ''),
            json_data.get('age', 0)
        )

if __name__ == "__main__":
    # Example usage:
    student_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 25
    }

    # Creating a Student instance from a dictionary
    student = Student.from_json(student_data)

    # Serializing the Student instance to a dictionary
    serialized_data = student.to_json()
    print(serialized_data)


#!/usr/bin/python3
"""
Contains the class_to_json function
"""


def class_to_json(obj):
    """
    Converts an object into a dictionary representation for JSON serialization.
    
    :param obj: The object to convert to a dictionary.
    :return: A dictionary representation of the object.
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    elif isinstance(obj, (int, float, str, bool, list, dict, tuple, set)):
        return obj
    elif obj is None:
        return None
    else:
        # You can customize this part for more complex objects or raise an error.
        return f"Unserializable object: {type(obj)}"

if __name__ == "__main__":
    # Example usage:
    class Example:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    obj = Example("John", 30)
    serialized_obj = class_to_json(obj)
    print(serialized_obj)


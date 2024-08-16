import os
import string
import random


def create_list_type(type=int) -> list:
    def list_type(value: str) -> bool:
        """
        Converts a string to list of <type>.

        Args:
            value: the binary string

        Returns:
            the boolean type
        """
        if not isinstance(value, str):
            value = str(value)

        if ',' in value:
            return [type(v) for v in value.split(',')]
        else:
            return [type(v) for v in value.split()]
    return list_type


def binary_to_boolean_type(value: str) -> bool:
    """
    Converts a binary string to a boolean type.

    Args:
        value: the binary string

    Returns:
        the boolean type
    """
    if not isinstance(value, str):
        value = str(value)

    value = value.lower()
    true_values = ['true', '1', 't', 'y', 'yes']
    false_values = ['false', '0', 'f', 'n', 'no']

    assert value in true_values + false_values

    return value in true_values


def custom_str_underscore(value):
    return str(value).replace("_", '-').strip()


def smart_joint(*paths):
    return os.path.join(*paths).replace("\\", "/")


def create_if_not_exists(path: str) -> None:
    """
    Creates the specified folder if it does not exist.

    Args:
        path: the complete path of the folder to be created
    """
    if not os.path.exists(path):
        os.makedirs(path)


def none_or_float(value):
    if value == 'None':
        return None
    return float(value)


def random_id(length=8, alphabet=string.ascii_letters + string.digits):
    """
    Returns a random string of the specified length.

    Args:
        length: the length of the string
        alphabet: the alphabet to be used

    Returns:
        the random string
    """
    return ''.join(random.choices(alphabet, k=length))

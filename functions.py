def read_lines(filepath='todos.txt'):
    """
    Read a text file and
    return the list of items.
    """
    with open(filepath, 'r') as file:
        return file.readlines()


def write_lines(content, filepath='todos.txt'):
    """ Write the items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(content)

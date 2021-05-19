def _merge_css_item(item):
    """Transform argument into a list with a single string value."""
    if isinstance(item, (list, tuple)):
        return _merge_css_list(*item)
    item = f"{item}" if item else ""
    return [item]


def _merge_css_list(*args):
    """Transform arguments into a list of string values."""
    css_list = []
    for arg in args:
        css_list += _merge_css_item(arg)
    return css_list


def merge_css_list(*args):
    """
    Combine a series of strings and lists into a single list of unique CSS classes.

    Removes duplicates. Gives precedence to first class encountered.
    """
    css_string = " ".join(_merge_css_list(*args))  # Create single string
    css_list = css_string.split()  # Split it to remove all whitespace
    css_list = filter(None, css_list)  # Remove empty strings
    # Remove duplicates, see https://stackoverflow.com/questions/480214/
    return list(dict.fromkeys(css_list))


def merge_css_text(*args):
    """
    Combine a series of strings and lists into one space separated string of unique CSS classes.

    Removes duplicates. Gives precedence to first class encountered.
    """
    return " ".join(merge_css_list(*args))

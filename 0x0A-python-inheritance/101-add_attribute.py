def add_attribute(obj, attr, value):
    """Add attribute to an object if possible, otherwise raise TypeError"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

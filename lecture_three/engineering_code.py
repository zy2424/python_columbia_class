def remove_whitespace(name: str) -> str:
    """
    Removes whitespace between words
    
    Parameters:
    * name - the string which may or may not
    have whitespace.
    
    Returns:
    A string without whitespace between characters.
    
    Examples:
    >>> remove_whitespace("Hello There")
    "HelloThere"
    >>> remove_whitespace("HelloThere")
    "HelloThere"
    """
    return "".join(name.split(" "))

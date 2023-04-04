#!/usr/bin/python3
def text_indentation(text):
    """ Text indentation after specific characters
    Args:
        text: text to print with indentation
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(". ", ".")
    text = text.replace("? ", "?")
    text = text.replace(": ", ":")
    for i in range(len(text)):
        print("{}".format(text[i]), end="")
        if text[i] in [".", "?", ":"]:
            print("\n")


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/5-text_indentation.txt")

def check_email(string):
    if " " in string:
        return False
    if "@" not in string:
        return False
    if "@." in string:
        return False
    last_dot_index = string.rfind(".")
    first_at_symbol_index = string.find("@")
    return last_dot_index > first_at_symbol_index

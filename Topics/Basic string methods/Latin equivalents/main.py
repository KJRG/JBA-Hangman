name = input()


def normalize(name_to_normalize):
    # put your code here
    replacements = {
        "é": "e",
        "ë": "e",
        "á": "a",
        "å": "a",
        "œ": "oe",
        "æ": "ae",
    }
    normalized_name = name_to_normalize
    for r in replacements.items():
        normalized_name = normalized_name.replace(r[0], r[1])
    return normalized_name


print(normalize(name))

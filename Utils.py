# Returns the last element of a list
def last_element(lizt: list) -> object:
    return lizt[len(lizt) - 1]


def generate_choices(choices: dict) -> str:
    string = ""
    for x in range(len(choices)):
        string += str("[" + str(x) + "] " + choices[x] + "\n")
    return string



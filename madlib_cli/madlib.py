
def read_template(file):
    file = open('assets/dark_and_stormy_night_template.txt')
    print(file)
    contents = file.read()
    print(contents)
    return contents


def parse_template(contents):
    parsed_curlies = ""
    parsed_words = []
    brackets = False
    string = ""
    curly_brackets = contents.count('{') + contents.count('}')
    if (curly_brackets > 0 and curly_brackets % 2 == 0):
        for characters in contents:
            if characters == '{':
                parsed_curlies += characters
                brackets = True
            elif characters == '}':
                parsed_curlies += characters
                brackets = False
                parsed_words.append(string)
                string = ""
            elif brackets:
                string += characters
            else:
                parsed_curlies += characters
    else:
        raise FileNotFoundError
    return (parsed_curlies, tuple(parsed_words))

def merge():
    pass


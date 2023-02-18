
no_space_header_pattern = [
    '#a',
    '#B',
    '#C',
    '#D',
    '#E',
    '#F',
    '#G',
    '#H',
    '#I',
    '#J',
    '#K',
    '#L',
    '#M',
    '#N',
    '#O',
    '#P',
    '#Q',
    '#R',
    '#S',
    '#T',
    '#U',
    '#V',
    '#W',
    '#X',
    '#Y',
    '#Z',
]

def simplify_H1_header(input_string):
    title = input_string.replace("# H1: ", " ").strip()
    title = input_string.replace("#H1 - ", " ").strip()
    title = input_string.replace("#H1 ", " ").strip()
    title = input_string.replace("#", " ").strip()
    return title

def groom_titles(input_string):
    for check in no_space_header_pattern:
        split = list(check)
        solution = f'{split[0]} {split[1]}'
        input_string = input_string.replace(check, solution)
    return input_string    
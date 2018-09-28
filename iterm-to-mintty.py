import sys

import xmltodict

color_names = { 
        'Foreground Color':  'ForegroundColour',
        'Background Color':  'BackgroundColour',
        'Cursor Text Color': 'CursorColour',
        'Ansi 0 Color':      'Black',
        'Ansi 1 Color':      'Red',
        'Ansi 2 Color':      'Green',
        'Ansi 3 Color':      'Yellow',
        'Ansi 4 Color':      'Blue',
        'Ansi 5 Color':      'Magenta',
        'Ansi 6 Color':      'Cyan',
        'Ansi 7 Color':      'White',
        'Ansi 8 Color':      'BoldBlack',
        'Ansi 9 Color':      'BoldRed',
        'Ansi 10 Color':     'BoldGreen',
        'Ansi 11 Color':     'BoldYellow',
        'Ansi 12 Color':     'BoldBlue',
        'Ansi 13 Color':     'BoldMagenta',
        'Ansi 14 Color':     'BoldCyan',
        'Ansi 15 Color':     'BoldWhite'
        }


def get_color(data, name):
    color_data = data['dict'][data['key'].index(name)]
    red = get_component(color_data, 'Red Component')
    green = get_component(color_data, 'Green Component')
    blue = get_component(color_data, 'Blue Component')
    return (red, green, blue)


def get_component(color_data, component_name):
    component_index = color_data['key'].index(component_name)
    component_value = color_data['real'][component_index]
    return round(float(component_value) * 256)

input_filename = sys.argv[1]

with open(input_filename) as fd:
    iterm = xmltodict.parse(fd.read())['plist']['dict']

fg_data = get_color(iterm, 'Foreground Color')

for iterm_color in color_names.keys():
    mintty_color = color_names[iterm_color]
    color = get_color(iterm, iterm_color)
    print("{} = {}, {}, {}".format(mintty_color, color[0], color[1], color[2]))

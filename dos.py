
""" This module lets you iterate recursively over a list that may (or may not) have nested lists """

lista3 = ["Africa", "Europa", ["Asia", "Oceanía", ["América", "Antartida"]]]


def print_lol(the_list, level=0, indent=False):

    """ This function takes a positional argument called 'the_list', which is any python list.
     Each data item in the list is printed on the screen on its own line, and each item is indented
     as specified in the 'level' argument if 'indent' happens to be True. Else, no indention happens """

    for elem in the_list:
        if isinstance(elem, list):
            print_lol(elem, level+1, indent)
        else:
            if indent:
                for tab in range(level):
                    print("\t", end='')

            print(elem)

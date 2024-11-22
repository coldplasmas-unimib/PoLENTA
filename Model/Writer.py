import lorem

def pargraphs( count ):
    output = ""
    for i in range( count ):
        output += lorem.paragraph() + "\n"
    return output

# create simple React templates
import os
import sys, getopt


DIRS = {
    "CSS": "css",
    "JS": "js",
    "ASSETS": "assets"
}

def getPath():
    """ a function to get the absolute path of the directory
    and name of the template to build

    Issue: It is assumed that the path is only absoute if provided

    Returns:
        path (str): path to directory where we want to build the top project directory
        name (str): name of template proejct directory
    """
    path = os.getcwd()
    args = sys.argv[2:]
    n_args = len(args)
    if n_args < 1:
        raise ValueError("Name for a directory was not provided in command line!")
    elif n_args == 1:
        name = args[0]
    elif n_args == 2:
        path = args[1]
        name = args[0]
    elif n_args > 2:
        path = args[1]
        name = args[0]
        print("Igonred additional arguments in command line!")

    return path, name

def createDirectories(path=os.getcwd(), dirs=DIRS):
    """create directories"""
    if not os.path.isdir(path):
        os.mkdir(path)
    for dir in DIRS.values():
        os.mkdir(os.path.join(path,dir))

def writeStringToFile(path, name, string):
    """writes a string to a file in the path
    Args:
        path (str): path to place the file
        name (str): name of the html file
        string (str): the string to write in the file
    """
    file = open(os.path.join(path,name),'w')
    file.write(string)
    file.close()

class Template():

    def __init__(self, dirs=DIRS):
        self.dirs = dirs
        self.basePath, self.name = getPath()
        self.path = os.path.join(self.basePath, self.name)
        createDirectories(self.path, self.dirs)


class ReactInBrowserTemplate(Template):
    """To create a React app which can be run in browser use:
        template = ReactInBrowserTemplate()"""

    def __init__(self, dirs=DIRS):
        Template.__init__(self, dirs)
        writeStringToFile(self.path, "index.html", self.createIndexHTML())
        writeStringToFile(os.path.join(self.path, self.dirs["JS"]), "script.js", self.createReactJS())

    def createIndexHTML(self):
        s = "<!DOCTYPE html>\n"
        s += "<html lang=\"en\" dir=\"ltr\">\n"
        s += "\t<head>\n"
        s += "\t\t<meta charset=\"utf-8\">\n"
        s += "\t\t<script crossorigin src=\"https://unpkg.com/react@17/umd/react.production.min.js\"></script>\n"
        s += "\t\t<script crossorigin src=\"https://unpkg.com/react-dom@17/umd/react-dom.production.min.js\"></script>\n"
        s += "\t\t<script src=\"https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.9/browser.min.js\" integrity=\"sha512-ElpdYRcyr+TVwZ4a2uBSTJfhYcC6sCSsJtXlzF4VwtydbOGGRUMRBRt3cVYFpL5fqn4TaaJBlzf+4m7wVtOCLQ==\" crossorigin=\"anonymous\"></script>\n"
        s += "\t\t<title>{}</title>\n".format(self.name)
        s += "\t</head>\n"
        s += "\t<body>\n"
        s += "\t\t<div id=\"react-container\"></div>\n"
        s += "\t\t<script type=\"text/babel\" src=\"js/script.js\"></script>\n"
        s += "\t</body>\n"
        s += "</html>"
        return s

    def createReactJS(self):
        s = "const { render } = ReactDOM\n"
        s += "\n"
        s += "render(\n"
        s += "\t<h1>Hello World!</h1>,"
        s += "\t document.getElementById(\"react-container\")\n"
        s += ")"
        return s


def main():
    command = sys.argv[1]
    if command == "create-react-in-browser-app":
        template = ReactInBrowserTemplate()

if __name__ == "__main__":
    main()


"""How to use:
#1 : To creat an react app in browser type:

    python create-react.py create-react-in-browser-app NAME_OF_APP [optional:PATH_OF_APP]
"""

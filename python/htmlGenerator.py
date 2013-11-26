try:
        import sys
        import vim
        import os
        import markdown
        from shutil import copyfile
except:
        print("Markdown not installed. Try pip install\
              markdown")

def check_file_extension(fileName):
    """Check the file extension name and removes it."""

    if(fileName.endswith(".markdown")):
        return fileName[:-9]
    elif(fileName.endswith('.mdtext')):
        return fileName[:-7]
    elif(fileName.endswith('.mdtxt') or fileName.endswith('.mdown')):
        return fileName[:-6]
    elif(fileName.endswith('.mkdn') or fileName.endswith('.mdwn') or\
         fileName.endswith('.text')):
         return fileName[:-5]
    elif(fileName.endswith('.mkd')):
        return fileName[:-4]
    elif(fileName.endswith('.md')):
        return fileName[:-3]
    else:
         raise ValueError("Unable to generate html: wrong file extension"+\
                     " or file format. Please use markdown and .md"+\
                     "extension")


header  = "<!DOCTYPE HTML>\n<html>\n"
header += """<head>\n<meta charset="utf-8">\n"""
header += """<link rel="stylesheet" type="text/css" href="style.css"> """
header += "\n</head>\n"
header += "<body>\n"
footer = "\n</body>\n</html>"


md = markdown.Markdown()
mdText = "\n".join(vim.current.buffer).decode('utf-8')
html = header + markdown.markdown(mdText, extensions=['codehilite','toc'],\
                        output_format='html5') + footer
try:
    fileName = check_file_extension(vim.current.buffer.name)
except ValueError as error:
    sys.stderr.write(error.message)
    sys.exit(-1)
htmlFile = open(fileName + '.html', mode='w')
htmlFile.write(html.encode('utf-8'))
htmlFile.close()
copyfile( os.path.expanduser("~") +"/.vim/bundle/vim-class-markdown/css/style.css",\
         fileName[:fileName.rfind('/')+1] + "style.css")
print("Html generated")

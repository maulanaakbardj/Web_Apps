import pywebio
from pywebio.input import *
from pywebio.output import *

def coding():
    code = textarea('Code Edit', 
    code={ 'mode': "python",  # code language
           'theme': 'darcula',  # Codemirror theme. Visit https://codemirror.net/demo/theme.html#cobalt to get more themes
         },
    value='import something\n# Write your python code')

    put_text(code)

if __name__ == '__main__':
    pywebio.start_server(coding, port=71)
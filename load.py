import yaml
from jinja2 import Environment, FileSystemLoader
import os

def verify_directory(dir_name):
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

if __name__ in ['__main__', '__console__']:
    f = open('presentation.yaml', 'r')
    beamer_dir = 'beamer_output'
    verify_directory(beamer_dir)
    slides = yaml.safe_load_all(f) # this produces a generator

    latex_env = Environment(  autoescape=False
                            , loader=FileSystemLoader('templates')
                           )
    latex_env.globals['slides'] = slides
    template = latex_env.get_template('beamer.tex')
    with open(os.path.join(beamer_dir, 'presentation.tex'), 'w') as pf:
        pf.write(template.render())

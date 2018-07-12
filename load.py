import yaml
from jinja2 import Environment, FileSystemLoader
import os

def verify_directory(dir_name):
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

if __name__ in ['__main__', '__console__']:
    with open('presentation.yaml', 'r') as f:
        beamer_dir = 'beamer_output'
        verify_directory(beamer_dir)
        slides = yaml.safe_load_all(f) # this produces a generator

        latex_env = Environment(  autoescape=False
                                , loader=FileSystemLoader('templates')
                               )
        latex_env.globals['slides'] = slides
        latex_env.globals['type'] = type
        template = latex_env.get_template('beamer.tex')
        with open(os.path.join(beamer_dir, 'presentation.tex'), 'w') as pf:
            pf.write(template.render())

    with open('presentation.yaml', 'r') as f:
        html_dir = 'html_output'
        verify_directory(html_dir)
        slides = yaml.safe_load_all(f) # this produces a generator

        html_env = Environment(  autoescape=True
                               , loader=FileSystemLoader('templates')
                              )
        html_env.globals['slides'] = slides
        html_env.globals['type'] = type
        template = html_env.get_template('template.html')
        with open(os.path.join(html_dir, 'presentation.html'), 'w') as pf:
            pf.write(template.render())

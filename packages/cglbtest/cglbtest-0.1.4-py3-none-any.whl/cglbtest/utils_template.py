import os
from jinja2 import Template,Environment,FileSystemLoader
CURRENT_DIR=os.path.dirname(os.path.realpath(__file__))
def template_render_path(filepath,data):
	with open(filepath,'r')as A:B=A.read();C=Template(B);return C.render(data)
def template_render(filename,data):return template_render_path(f"{CURRENT_DIR}/{filename}",data)
def template_render_infolder(filename,data):A=FileSystemLoader([CURRENT_DIR]);B=Environment(loader=A);C=B.get_template(filename);return C.render(data)
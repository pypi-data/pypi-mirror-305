import click,coloredlogs,logging
logger=logging.getLogger('cglbtest')
import os
from cglbtest.env import Env
@click.group()
@click.option('--log-level',default='INFO',help='Log level. Default is INFO. Available levels are DEBUG, INFO, WARNING, ERROR, CRITICAL.')
def cli(log_level):coloredlogs.install(level=log_level)
@cli.command(help='Show the version information.')
def version():click.echo(f"cglbtest v0.1.4")
@cli.command(help='Run a test suite.')
@click.argument('path',required=True)
@click.option('--config',help='Path to the yaml test configuration file. If not provided search for a file named "cglbtest.yml" in the path.')
def run(path,config):
	G='error';A=config;B=os.path.abspath(path);logger.info(f"Running on path '{B}'");C=''
	if A:
		if not os.path.isfile(A):logger.error(f"Config file '{A}' not found.");exit(1)
		else:C=os.path.abspath(C)
	else:
		A=f"{B}/cglbtest.yml"
		if os.path.isfile(A):C=A
	try:D=Env(yaml_file=C)
	except Exception as H:logger.error(f"Error: {H}");exit(1)
	K=D.conf;logger.info(f"Processor: {D.processor}")
	if D.processor=='compare':
		I=D.processor_compare(prefix_files_path=B+'/');E=os.path.basename(B);logger.info(f"Execute {E}'.");J,F=I.compare(name=E)
		if J:logger.info(f"Test results: 'success'.")
		else:
			logger.warning(f"Test results: 'failed'.")
			if F.get(G,None):logger.error(F[G])
@cli.command(help='Manage configuration.')
def config():click.echo(f"Not implemented yet.")
if __name__=='__main__':cli()
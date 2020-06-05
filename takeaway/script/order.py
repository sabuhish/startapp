# from .core.utils.version import print_version
from startapp.core import  utils
import click
import  time

# @click.command()
# @click.option('--app',type=click.Choice(['fastapi', 'flask','django'], case_sensitive=True), prompt='Projects',show_default=True,confirmation_prompt="confirm",default='fastapi',required=True, help='The app name')
# @click.option('--version', is_flag=True, callback=print_version,
#               expose_value=False, is_eager=True)
# def starting(app):
#     click.echo('Starting app %s!' % app)


# starting()
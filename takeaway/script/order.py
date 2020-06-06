
import  click
from takeaway.core.utils.version import  print_version
import math
import random
import time
from takeaway.controllers.commands import  execution
@click.group()
def cli():
    """Takeaway group Cli"""
    pass

@cli.command()
def clear():
    """Clears the entire screen."""
    click.clear()

@cli.command()
def colordemo(app):
    """Demonstrates ANSI color support."""
    # for color in "red", "green", "blue":
    click.echo(click.style(f"{app} is ready to go {color}", fg=color))
    # click.echo(click.style(f"I am background colored {color}", bg=color))



@cli.command(help='😄 Simple project creator')
@click.option('--app','-a',type=click.Choice(['fastapi', 'flask','django'], case_sensitive=True), prompt='Projects',show_default=True,confirmation_prompt="confirm",default='fastapi',required=True, help='The app name')
@click.option('--version',"-v",metavar='  version of program', is_flag=False, callback=print_version,
              expose_value=False, is_eager=True)
@click.option('--name',"-n",metavar='     the name of yor app',prompt='Name for your project',show_default=True,default='myproject',required=True, help='The app name')

def starting(app,name,count=8000):
    click.echo(click.style('Starting app %s!' % app,fg='green'))
    click.echo(click.style('Starting name %s!' % name,fg='green'))
    click.progressbar(iterable="8", length=None, label=None, show_eta=True, show_percent=None, show_pos=False, item_show_func=None, fill_char='#', empty_char='-', bar_template='%(label)s [%(bar)s] %(info)s', info_sep=' ', width=36, file=None, color=None)
    # click.echo(click.style('Clearing!', blink=True))
    # click.clear()
    # click.echo(click.style('Some things', reverse=True, fg='cyan'))
    # items = range(count)
    # def process_slowly(item):
    #     time.sleep(0.002 * random.random())
    # def filter(items):
    #     for item in items:
    #         if random.random() > 0.3:
    #             yield item

    # with click.progressbar(
    #     items, label=f"Processing {app}", fill_char=click.style("#", fg="green")
    # ) as bar:
    #     for item in bar:
    #         process_slowly(item)

    # colordemo()
    execution(app,name)
    # clear()


starting()
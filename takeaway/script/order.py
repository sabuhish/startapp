
import  click
import math
import random
import time
from takeaway.controllers.commands import  Operation
from takeaway.core.utils.version import  VERSION
@click.group()
def cli():
    """Takeaway group Cli"""
    

@cli.command()
def clear():
    """This will clear the entire screen """
    click.clear()



@cli.command(help='😄 simple boilerplate ready for development')
@click.option('--app','-a',type=click.Choice(['fastapi', 'flask','django'], case_sensitive=True), prompt='Choose one of the application',show_default=True,confirmation_prompt="confirm",default='fastapi',required=True, help='the app name')
@click.option('--name',"-n",metavar='     the name of yor app',prompt='Name for your app',show_default=True,default='myproject',required=True, help='the app name')
@click.version_option(VERSION)
def cli(app,name,count=4000):
    click.echo(click.style('Starting app %s at directory %s!' % (app,name), fg='green'))
    click.progressbar(iterable="8", length=None, label=None, show_eta=True, show_percent=None, show_pos=False, item_show_func=None, fill_char='#', empty_char='-', bar_template='%(label)s [%(bar)s] %(info)s', info_sep=' ', width=36, file=None, color=None)
    items = range(count)
    def process_slowly(item):
        time.sleep(0.001 * random.random())
    def filter(items):
        for item in items:
            if random.random() > 0.3:
                yield item

    with click.progressbar(
        items, label=f"Processing {app}", fill_char=click.style("#", fg="green")
    ) as bar:
        for item in bar:
            process_slowly(item)


    management = Operation(app,name)
    management.execute()
    click.echo(click.style('Clearing!', blink=True,fg="red"))

    time.sleep(5)
    clear()


# if __name__ == '__main__':
#     starting()

cli()
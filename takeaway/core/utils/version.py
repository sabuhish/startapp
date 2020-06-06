import  sys
import  os
sys.path.insert(0, os.path.abspath('..'))

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()

PY3 = sys.version_info[0] == 3


VERSION = "0.0.1"
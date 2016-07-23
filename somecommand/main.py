"""Some command
Usage:
  somecommand <subcommand>
  somecommand (-h | --help)
  somecommand --version
Options:
  -h --help             Show this screen.
  --version             Show version.
"""

from docopt import docopt
from somecommand.subcommands import foo, bar

def helloworld():
    print("hello world")

def main():
    args = docopt(__doc__, version='some-command 0.0.1')
    if args['<subcommand>'] == 'foo':
        foo()
    elif args['<subcommand>'] == 'bar':
        bar()
    else:
        helloworld()

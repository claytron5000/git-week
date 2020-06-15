import click

@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.option('--name', prompt='Your name', help='name of the person')

def hello(count, name):
    """Simple program  that greets NAME for total of COUNT times."""
    for x in range(count):
        click.echo('Hello {0}!'.format(name))

if __name__ == '__main__':
    hello()
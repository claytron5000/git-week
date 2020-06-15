import click
import datetime
from main import loopThroughDates
from dateutil.parser import parse
from pathlib import Path

@click.command()
@click.option("--path", required=True, prompt="Projects Path")
@click.option("--start", prompt="Start Date")
@click.option("--end", default=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

def run(path, start, end):
    """run the thing"""
    start_date = parse(start)
    end_date = parse(end)
    projects_path = Path(path)
    click.echo(type(start_date))
    click.echo(type(end_date))
    click.echo(type(projects_path))
    click.echo(projects_path.exists())
    loopThroughDates(projects_path=projects_path, start_date=start_date, end_date=end_date)

if __name__ == "__main__":
    run()
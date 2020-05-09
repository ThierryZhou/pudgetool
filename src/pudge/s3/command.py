import click

@click.group()
def s3():
    pass

@s3.command()
@click.option('--cmd', '-c', help='command type')
@click.option('--name', '-n', help='bucket name')
def buckets(cmd, name):
    click.echo('This is the buckets subcommand of the cloudflare command')

@s3.command()
@click.option('--cmd', '-c', help='command type')
@click.option('--file', '-f', help='file name')
def objects(cmd, file):
    click.echo('This is the objects subcommand of the cloudflare command')

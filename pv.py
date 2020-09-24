import click
import comands as clients_comands

CLIENTS_TABLE = '.clients.csv'
@click.group()
@click.pass_context
def cli(ctx):
    """An application to manage clients, inventory, sales and produce reports."""
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_comands.all)
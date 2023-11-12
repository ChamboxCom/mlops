    """
    This module is used to create calculations funtions such as addtion, subtraction, multiplication, division, etc.
    This module will also be invoked as a command line tool. Using click
    """
    
    
import click

def add(num1, num2):
    """
    This function is used to add two numbers.
    """
    return num1 + num2

def substract(num1, num2):
    """
    This function is used to substract two numbers.
    """
    return num1 - num2

def multiply(num1, num2):
    """
    This function is used to multiply two numbers.
    """
    return num1 * num2
    
    
# build a click group
@click.group()
def cli():
    pass

#build a click command
@cli.command("add")
@click.argument("num1", type=int)
@click.argument("num2", type=int)
def add_command(num1, num2):
    """
    This command is used to add two numbers.
    """
    click.echo(add(num1, num2))
    
@cli.command("substract")
@click.argument("num1", type=int)
@click.argument("num2", type=int)
def substract_command(num1, num2):
    """
    This command is used to substract two numbers.
    """
    #invoke the substract function with colors
    click.echo(substract(num1, num2))
    
@cli.command("multiply")
@click.argument("num1", type=int)
@click.argument("num2", type=int)
def multiply_command(num1, num2):
    """
    This command is used to multiply two numbers.
    """
    click.echo(multiply(num1, num2))
    
    
    
if __name__ == "__main__":
    cli()
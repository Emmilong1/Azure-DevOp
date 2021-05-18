import click

@click.command(help="This is just a hello app. It does nothing.")   #click menu setup and help show
@click.option("--name", prompt="I need your name", help="Need name")    #something that accepts the parameters as options then probbaly a help message
@click.option("--color", prompt="I need your color", help="This is your color") #color setup with a prompt for color request and help clause as well
def hello(name, color):
    if name == "Samuel":
        click.echo("Samuel, you are always DevOps blue.")
        click.echo(click.style(f"Hello {name}!", fg="blue"))
    else:
            click.echo(f"Your color is {color}!")
            click.echo(click.style(f"Hello {name}!", fg=color))

if __name__ == "__main__":      #only run this block if it runs as a script and it's close to having a CLI
    hello()
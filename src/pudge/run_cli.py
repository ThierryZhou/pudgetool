from AlgorithmController.generator import *
import os
import click

@click.command()
@click.option('--generate', '-g', 'project', help='generate algorithm controller module', show_default=True)
@click.argument('project')
def generate(project):
    cgenerator = CodeGenerator(project)
    cgenerator.gen_snapshot()
    cgenerator.gen_analyze()
    cgenerator.gen_interface()
    cgenerator.gen_cmake()

@click.group()
def cli():
    pass


cli.add_command(generate)

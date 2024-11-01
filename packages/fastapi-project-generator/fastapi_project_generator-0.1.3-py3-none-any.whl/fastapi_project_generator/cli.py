import os
import shutil
import click
from jinja2 import Environment, FileSystemLoader, select_autoescape

@click.command()
@click.argument('project_name')
def main(project_name):
    """Initialize a new FastAPI project."""
    current_dir = os.path.dirname(__file__)
    template_dir = os.path.join(current_dir, 'templates')
    target_dir = os.path.join(os.getcwd(), project_name)

    if os.path.exists(target_dir):
        click.echo(f"Error: Directory '{project_name}' already exists.")
        return

    shutil.copytree(template_dir, target_dir)
    render_templates(target_dir, project_name)
    click.echo(f"Project '{project_name}' created successfully.")

def render_templates(project_dir, project_name):
    env = Environment(
        loader=FileSystemLoader(project_dir),
        autoescape=select_autoescape(['py', 'md', 'env', 'txt'])
    )
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.py', '.md', '.env', '.txt')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                template = env.from_string(content)
                rendered_content = template.render(project_name=project_name)
                with open(file_path, 'w') as f:
                    f.write(rendered_content)

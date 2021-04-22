import click
from docx import Document


@click.command()
@click.argument('path', type=click.Path(exists=True, readable=True,
                resolve_path=True, dir_okay=True))
def read(path):
    document = Document(path)
    for para in document.paragraphs:
        click.echo(para.text)


if __name__ == '__main__':
    read()

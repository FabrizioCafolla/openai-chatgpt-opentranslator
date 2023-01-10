import pathlib
import sys

import click
import openai


def render_file(filepath: str) -> str:
    with open(str(pathlib.Path(filepath)), 'r') as f:
        return f.read()


@click.command()
@click.option('--translate', type=str, required=True)
@click.option('--text', default=None, help='Raw text')
@click.option('--filepath', default=None, help='File path containing the text')
def main(translate, text, filepath):
    prefix = f'Translate the following text into {translate}'

    if filepath:
        text = f'{prefix}:\n{render_file(filepath=filepath)}'

    if not text:
        raise Exception('[ERR] No text provided to the command')

    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=text,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        translated_text = ''

        if choices := response.get('choices', []):
            if len(choices) > 0:
                translated_text = choices[0]['text']
    except Exception as e:
        print(str(e))
        sys.exit(1)
    else:
        click.echo(translated_text)


if __name__ == '__main__':
    sys.exit(main())

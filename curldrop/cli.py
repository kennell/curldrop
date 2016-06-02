import click
import os
from .app import app
from .server import StandaloneServer


@click.command()
@click.option(
    '--port',
    default=8000,
    help='Port to listen on, default is 8000'
)
@click.option(
    '--upload-dir',
    default=os.getcwd(),
    help='Directory where uploads are stored, if not specified the current working directory will be used'
)
@click.option(
    '--url',
    default="http://www.example.com/",
    help='Base URL, e.g. http://www.example.com/'
)
def main(port, upload_dir, url):
    app.config['UPLOAD_DIR'] = upload_dir
    app.config['BASE_URL'] = url

    server_options = {
        'bind': '{ip}:{port}'.format(
            ip='0.0.0.0',
            port=port
        ),
        'workers': 4,
    }
    StandaloneServer(app, server_options).run()


if __name__ == '__main__':
    main()
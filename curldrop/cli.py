import click
import os
from curldrop.app import app
from curldrop.server import StandaloneServer


@click.command()
@click.option("--port", default=8000, help="Port to listen on, default is 8000")
@click.option(
    "--upload-dir",
    default=os.getcwd(),
    help="Directory where uploads are stored, if not specified the current working directory will be used",
)
@click.option("--baseurl", default=None, help="Base URL, e.g. http://example.com:8000/")
@click.option(
    "--timeout", default=30, help="Number of seconds before a worker will timeout"
)
@click.option("--workers", default=4, help="Number of workers")
def main(port, upload_dir, baseurl, timeout, workers):
    if not baseurl:
        baseurl = "http://{host}:{port}/".format(host="localhost", port=port)
        click.echo(
            click.style(
                "You did not specify a Base URL, using default: " + baseurl, fg="yellow"
            )
        )

    app.config["UPLOAD_DIR"] = upload_dir
    app.config["BASE_URL"] = baseurl

    server_options = {
        "bind": "{ip}:{port}".format(ip="0.0.0.0", port=port),
        "workers": workers,
        "accesslog": "-",
        "errorlog": "-",
        "timeout": timeout,
    }
    StandaloneServer(app, server_options).run()


if __name__ == "__main__":
    main()

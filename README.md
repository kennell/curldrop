⏫ curldrop
==========

curldrop is a simple (less than 100 LOC) web app that allows you to upload files straight from your terminal with curl. It is inspired by services like [Transfer.sh](https://transfer.sh/).

## Get started


Simply start the curldrop service...

![Start curldrop](http://i.imgur.com/3mSle1Z.gif)

... and start uploading files with curl:

![Upload a file to curldrop](http://i.imgur.com/cxV9gTH.gif)

Install and run
-------

Install via pip:

```
pip install curldrop
```

You can now run curldrop:

```
curldrop
```

There are also some additional options:

```
Usage: curldrop [OPTIONS]

Options:
  --port INTEGER     Port to listen on, default is 8000
  --upload-dir TEXT  Directory where uploads are stored, if not specified the
                     current working directory will be used
  --baseurl TEXT     Base URL, e.g. http://example.com:8000/
  --timeout INTEGER  Number of seconds before a worker will timeout
  --workers INTEGER  Number of workers
  --help             Show this message and exit.
```

Uploading files
-----

You can now upload files to your curldrop, here are some basic examples. 

Upload a single file
```
curl --upload-file cat.jpg example.com
```

Upload multiple files

```
curl --upload-file "{path/to/file1,path/to/file2}" example.com
```

## Production deployment

### Systemd service

If the services on your server are managed by systemd, you may setup a service like so in `/etc/systemd/system/curldrop.service` :
```
[Unit]
Description=curldrop -- easy upload from command line
Requires=
After=

[Service]
Restart=always
ExecStart=/usr/local/bin/curldrop --port PORT --upload-dir UPLOAD_DIR --baseurl BASE_URL
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
User=USER
Group=USER

[Install]
WantedBy=default.target
```

### Serving with nginx

If you would like to be able to reach your curldrop without specifying the port, it needs to be reachable over 80 (http) and/or 443 (https). But if you already have other web services running, you may need to configure your web server to act as a reverse-proxy redirecting incoming request to curldrop running locally on a different port.

Here's an example with nginx of how to serve curldrop on the domain `bin.example.org` on the port 80 when it's running locally on the port 8888 :
```
server {
    listen 80;
    server_name bin.example.org;
    
    location / {
        proxy_pass http://127.0.0.1:8888$request_uri;
    }
}
```

Setting up an HTTPS certificate for your service with [letsencrypt](https://letsencrypt) is off-topic for this document, but there's plenty of tutorials throughout the interwebz to get you started.

### Security considerations

You may want to make files publicly reachable, but to restrict upload to your own server. This way, you may share your configuration files pretty easily but not let everybody upload pretty much anything to your server. Here's how to do this with nginx :

```
    location / {
        limit_except GET HEAD OPTIONS {
            allow   127.0.0.1;
            deny    all;
        }
        proxy_pass http://127.0.0.1:8888$request_uri;
    }
```

This allows GET, HEAD and OPTIONS requests for everyone but restricts other operations such as uploading a file (PUT) to the local machine (127.0.0.1). In case you are running an [onion service](https://www.torproject.org/docs/tor-onion-service.html.en) for your curldrop, all incoming requests will come from 127.0.0.1 so you should have a separate server block forbidding upload for 127.0.0.1 as well :

```
server {
    listen 80;
    server_name abcdefghijklmnop.onion;
    
    location / {
        limit_except GET HEAD OPTIONS {
            deny all;
        }
        proxy_pass http://127.0.0.1:8888$request_uri;
    }
}
```

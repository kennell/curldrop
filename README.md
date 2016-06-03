curldrop
========

curldrop is a simple (less than 100 LOC) web app that allows you to upload files straight from your terminal with curl. It is inspired by services like [curl.io](http://curl.io/) and [Transfer.sh](https://transfer.sh/).

Simply start the curldrop service...

![Start curldrop](http://i.imgur.com/MgLTPhN.gif)

... and start uploading files with curl:

![Upload a file to curldrop](http://i.imgur.com/sLe5BwG.gif)

Install and run
-------

Install via pip:

```
pip install curldrop
```

You can now run curldrop:

````
Usage: curldrop [OPTIONS]

Options:
  --port INTEGER     Port to listen on, default is 8000
  --upload-dir TEXT  Directory where uploads are stored, if not specified the
                     current working directory will be used
  --baseurl TEXT     Base URL, e.g. http://example.com/
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


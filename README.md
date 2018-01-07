⏫ curldrop
==========

curldrop is a simple (less than 100 LOC) web app that allows you to upload files straight from your terminal with curl. It is inspired by services like [curl.io](http://curl.io/) and [Transfer.sh](https://transfer.sh/).

[![Maintainability](https://api.codeclimate.com/v1/badges/077529df0b80d8759542/maintainability)](https://codeclimate.com/github/kennell/curldrop/maintainability)


## Donations

Your contribution keeps this project going ❤️ 

* BTC 121QcrzmFsYfxpJYneTS4N6yKDdU8GGfXa
* ETH 0x56Aab3cDA7Ea02953aE394F9ffA3f7b80ed8b6DE
* LTC LerFT8YP7Q9etp2M3EsJxLZJYeFCZLV6wQ

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


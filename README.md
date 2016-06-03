curldrop
========

curldrop is a simple (less than 100 LOC) web app that allows you to upload files straight from your terminal with curl. It is inspired by services like [curl.io](http://curl.io/) and [Transfer.sh](https://transfer.sh/).

Simply start the curldrop app...

![Start curldrop](http://i.imgur.com/MgLTPhN.gif)

... and start upload files with curl:

![Upload a file to curldrop](http://i.imgur.com/sLe5BwG.gif)

Install
-------

Install via pip:

```
pip install curldrop
```


Usage
-----

You can now upload files to your curldrop, here are some basic examples. 

Upload a single file to your curldrop instance:
```
curl --upload-file myfile.jpg example.com
```

Upload multiple files:

```
curl --upload-file "{path/to/file1,path/to/file2}" example.com
```


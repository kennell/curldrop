curldrop
========

curldrop is a simple (less than 100 LOC) web application that allows you to upload files straight from the terminal with curl. It is inspired by great services like <a href="http://curl.io/">curl.io</a>, <a href="http://chunk.io/">chunk.io</a> and <a href="https://transfer.sh/">transfer.sh.</a>

Install
-------

curldrop is built on top of Python 3, Flask, Tornado and SQLite. Make sure you install the following dependencies:

```
sudo pip3 install flask tornado
```

Make sure you edit the **config.py** file to you match your preferences.

To start curldrop, make runcurldrop.py executable and run it:

```
chmod +x runcurldrop.py
./runcurldrop.py
```

Congrats! curldrop should now be up and running! 

Usage
-----

You can now upload files to your curldrop, here are some basic examples. 

Upload a single file to your curldrop instance:
```
curl --upload-file myfile.jpg mycurldropserver.com
```

Upload multiple files:
```
curl -T "{path/to/file1,path/to/file2}" mycurldropserver.com
```

Hints: 
* the '-T' flag is equal to --upload-file.
* add -s to hide the progress bar

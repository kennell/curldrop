curldrop
========

curldrop is a simple (less than 100 LOC) web application that allows you to upload files straight from your Terminal with curl. It is inspired by great services like <a href="http://curl.io/">curl.io</a>, <a href="http://chunk.io/">chunk.io</a> and <a href="https://transfer.sh/">transfer.sh.</a>

Install
-------

curldrop is built on top of Python 3, Flask, Tornado and SQLite. Make sure you install the following dependencies:

```
sudo pip3 install flask tornado
```

Clone this Repository to your server:

```
git clone https://github.com/kevvvvv/curldrop.git
```

Make sure you edit the **config.py** file to you match your preferences. The SQLite database file will be created for you.

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
curl --upload-file "{path/to/file1,path/to/file2}" mycurldropserver.com
```

Hints: 
* the '-T' flag is equal to '--upload-file'
* add '-s' to hide the progress bar

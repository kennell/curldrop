# curldrop config

# DEBUG SETTINGS
DEBUG=True # set to False when in Production

# DATABASE SETTINGS
DATABASE='files.db'

# SECURITY SETTINGS
SECRET_KEY='secret' # change this to some random string

# APP SETTINGS
PORT=5000 # Port to run on
BASEURL='http://www.example.com/' # base URl for downloads, do not forget to include a trailing slash
UPLOADDIR='uploads/' # directory for uploads, do not forget to include a trailing slash
EXPIRES=86400 # Number of seconds before a file download expires (1day = 86400 secs)
MAXSIZE=50000000 # Max filesize in 

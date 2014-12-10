import sqlite3
from flask import Flask, g, request, send_file, abort
from werkzeug import secure_filename
from uuid import uuid4
from datetime import datetime
from os import remove
from os.path import isfile
from contextlib import closing

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Request helpers
# Connect to DB
@app.before_request
def before_request():
	g.db = connect_db()

# Close DB connection after request
@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

# Routes
# Index
@app.route('/', methods=['GET'])
def index():
	return '<a href="https://www.github.com/kevvvvv/curldrop">curldrop</a> is up and running!'

# Catch a incoming PUT request
@app.route('/<userfile>', methods=['PUT'])
def upload(userfile):
	if len(request.data) > app.config['MAXSIZE']:
		return "Filesize exceeds " + str(app.config['MAXSIZE']) + " bytes."

	file_id = str(uuid4())[:8]
	cur = g.db.execute('INSERT INTO files (file_id, timestamp, ip, originalname) VALUES (?, ?, ?, ?)', 
		[file_id, str(int(datetime.now().timestamp())), request.remote_addr, secure_filename(userfile)])
	g.db.commit()
	fo = open(app.config['UPLOADDIR'] + file_id, "wb")
	fo.write(request.data)
	fo.close()
	return app.config['BASEURL'] + file_id + '\n'

# Serve download
@app.route('/<file_id>', methods=['GET'])
def download(file_id):
	remove_expired()
	if checkfile(file_id):
		return send_file(app.config['UPLOADDIR'] + file_id, as_attachment=True, attachment_filename=checkfile(file_id))
	else:
		abort(404, "The requested file was not found or is expired.")


# Database helpers
# Create a SQLite file from schema.sql
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

# Connect to SQLite database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# Helpers
# Remove expired files from the upload directory
def remove_expired():
	now = int(datetime.now().timestamp())
	cur = g.db.execute('SELECT file_id, timestamp FROM files')
	for row in cur.fetchall():
		if (now - row[1]) > app.config['EXPIRES']:
				remove(app.config['UPLOADDIR'] + row[0])
				rem = g.db.execute('DELETE FROM files WHERE file_id = ?	', [row[0]])
				g.db.commit()

# Check if file exists and returns original upload name
def checkfile(file_id):
	cur = g.db.execute('SELECT originalname FROM files WHERE file_id = ?', 
		[file_id])
	for row in cur.fetchall():
		return row[0]

	return False

# Run application
if __name__ == '__main__':
	app.run()
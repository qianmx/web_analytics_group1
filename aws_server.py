from flask import Flask
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/groupproject')
def root():
    return app.send_static_file('index.html')



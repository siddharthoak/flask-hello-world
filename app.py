# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask


app = Flask(__name__)
WHO = os.environ['WHO']

@app.route('/')
def hello_world():      
    if WHO:
        return WHO
    else:
        return 'Hello World!!'
      
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    


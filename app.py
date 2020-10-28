# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
import os

WHO = os.environ['WHO']

app = Flask(__name__)

@app.route('/')
def hello_world():
    file1 = open('/opt/app-root/secure/myapp.sec', 'r') 
    Lines = file1.readlines() 
  
    count = 0
    # Strips the newline character 
    for line in Lines: 
    print("Secret Line{}: {}".format(count, line.strip())) 

    if WHO:
        return "Hello {WHO} ........".format(WHO)
    return 'Hello World!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    


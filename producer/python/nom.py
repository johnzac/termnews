from flask import Flask
import time
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"
@app.route('/test')
def test():
    x=range(100000)
    for i in x:
        for j in x:
            continue
      
    return "loop done"

if __name__ == '__main__':
    app.run()

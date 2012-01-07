# cherrypy-wsgi
I was using using [CherryPy][] and was frustrated that there wasn't a
way to serve wsgi applications from the command line. So here it is.

[CherryPy]: http://cherrypy.org/
## Usage
```
usage: cherrypy-wsgi [-h] [--port [PORT]] module_name [app_name]

Run a WSGI application with CherryPy from the command line.

positional arguments:
  module_name    The name of the module where your application lives.
  app_name       The name of your application, in `module_name`; defaults to
                 'app'.

optional arguments:
  -h, --help     show this help message and exit
  --port [PORT]  Port to serve on; defaults to 8080.
```

## Tutorial
Make a file named `testapp.py` and put [Flask's Hello World][Flask] example in it:

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

Then, from the commandline: `cherrypy-wsgi testapp`. You can call `app` something else; 
in that case: `cherrypy-wsgi testapp something_else`.

[Flask]: http://flask.pocoo.org/


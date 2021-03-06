"""A WSGI application that serves web resources."""

from external.bottle import bottle

application = bottle.Bottle()


@application.route('/')
def index():
  bottle.response.content_type = 'text/html'
  return bottle.static_file('index.html', 'hello')


@application.route('/hello.css')
def css():
  bottle.response.content_type = 'text/css'
  return bottle.static_file('styles_combined.css', 'hello')


@application.route('/hello.js')
def js():
  bottle.response.content_type = 'application/javascript'
  return bottle.static_file('hello_combined.js', 'hello')

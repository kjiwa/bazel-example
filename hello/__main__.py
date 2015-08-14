"""A script that runs a web server process."""

from external.bottle import bottle
from external.python_gflags import gflags
from hello import server
import logging
import sys

FLAGS = gflags.FLAGS

gflags.DEFINE_integer('port', 8080, 'The port on which to serve HTTP requests.')


def main(argv):
  logging.basicConfig(level=logging.DEBUG)

  try:
    argv = FLAGS(argv)
  except gflags.FlagsError, e:
    print '%s\\nUsage: %s ARGS\\n%s' % (e, sys.argv[0], FLAGS)
    sys.exit(1)

  bottle.run(app=server.application, host='0.0.0.0', port=FLAGS.port)

if __name__ == '__main__':
  main(sys.argv)

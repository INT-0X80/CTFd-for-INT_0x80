#!/usr/bin/python
import os

# Local config when using with Apache mod_wsgi
#import sys
#sys.path.insert(0, '/var/www/python/')

# Openshift virtenv config
virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

# from CTFd import create_app as application
from CTFd import create_app 
application = create_app()

#
# Below for local testing with command "python wsgi.py"
#
#virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'), 'virtenv')
#virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
#try:
#    execfile(virtualenv, dict(__file__=virtualenv))
#except IOError:
#    pass
#
#
#if __name__ == '__main__':
#    from wsgiref.simple_server import make_server
#    httpd = make_server('localhost', 8051, application)
      # Wait for a single request, serve it and quit.
      # httpd.handle_request()
#    httpd.serve_forever()


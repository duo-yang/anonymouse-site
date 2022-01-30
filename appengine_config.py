"""`appengine_config` gets loaded when starting a new application instance."""
import sys
import os.path
from google.appengine.ext import vendor
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

on_appengine = os.environ.get('SERVER_SOFTWARE', '').startswith('Development')

if on_appengine and os.name == 'nt':
    sys.platform = "Not Windows"

# Add any libraries install in the "lib" folder.
vendor.add('lib')

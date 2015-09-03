from optparse import OptionParser
from nyms import app


def run_app(app):
    parser = OptionParser()
    parser.add_option('-d', '--debug', dest='debug', default=False,
                      action='store_true',
                      help='Turn on debugging')
    parser.add_option('-p', '--port', dest='port', type=int, default=5000,
                      help='Specify the server port')
    parser.add_option('-l', '--listen', dest='listen_addr', default='::1',
                      help='Specify the listening address')
    options, args = parser.parse_args()
    app.run(host=options.listen_addr, port=options.port, debug=options.debug)


run_app(app)

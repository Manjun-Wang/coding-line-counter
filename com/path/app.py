import sys
import getopt

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        print(sys.argv)
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help", "file=", "language="])

            print(opts, args)
            options = get_correct_opts(opts)
            
        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


def get_correct_opts(opts):
    options = {}
    for opt in opts:
        if opt[0] == "--file":
            options["file"] = opt[1]
        if opt[0] == "--language":
            options["--language"] = opt[1]
    if len(options) != 2:
        raise Usage("Need to have --file=x and --language=y as input params")
    return options


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/python

import sys

if len(sys.argv) < 2:
    print("Usage: %s num_lines" % sys.argv[0])
    sys.exit(1)

def gen_int_bool_string():
    n=int(sys.argv[1])

    for i in xrange(n):
        b = i % 2 and 'true' or 'false'
        sys.stdout.write('%s,%s,%s\n' % (i, b, "id_" + str(i)))

if __name__ == "__main__":
    gen_int_bool_string()

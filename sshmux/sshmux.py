#!/usr/bin/env python
# coding: utf-8

import re
import sys
import argparse

import subprocess as sub


def sshmux(ns):
    # These are always passed...
    sub_kwargs = {
        'stdout': sub.PIPE,
        'stderr': sub.PIPE,
        'env': {'LANG': "en_US.utf8"}
    }

    # The base of the command
    hostargs = ['ssh', '-A']

    host = ns.host
    match = re.search(r'^\[(.*)\]:(\d+)', ns.host)

    if match:
        host = match.group(1)
        hostargs += ['-p', match.group(2)]

    hostargs.insert(2, host)

    p = sub.Popen(hostargs + ['-t', 'tmux -V && tmux ls'], **sub_kwargs)
    res = p.communicate()[0]

    if sys.version_info > (3,):
        res = res.decode()

    lines = res.strip().split('\r\n')
    version, sessions = lines[0], lines[1:]

    print(version, sessions)


def setup_arguments():
    parser = argparse.ArgumentParser('sshmux')

    parser.add_argument(
        'host',
        metavar='<host>',
        help='Host to connect to',
    )

    parser.add_argument(
        'session',
        default='main',
        metavar='<session>',
        nargs='?',
        help='tmux session to attach (default: main)',
    )

    return parser


def main():
    parser = setup_arguments()
    ns = parser.parse_args()

    if not ns.host:
        parser.print_help()
        sys.exit(1)

    return sshmux(ns)


if __name__ == "__main__":
    main()

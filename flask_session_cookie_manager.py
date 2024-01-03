from argparse import ArgumentParser
from ast import literal_eval
from zlib import decompress

from flask import Flask
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import base64_decode


def encode(secret_key, session_cookie_structure):
    app = Flask("")
    app.secret_key = secret_key

    session_cookie_structure = dict(literal_eval(session_cookie_structure))
    si = SecureCookieSessionInterface()
    s = si.get_signing_serializer(app)

    return s.dumps(session_cookie_structure)


def decode(session_cookie_value, secret_key=None):
    if secret_key is None:
        compressed = False
        payload = session_cookie_value

        if payload.startswith('.'):
            compressed = True
            payload = payload[1:]

        data = payload.split(".")[0]

        data = base64_decode(data)
        if compressed:
            data = decompress(data)

        return data
    else:
        app = Flask("")
        app.secret_key = secret_key

        si = SecureCookieSessionInterface()
        s = si.get_signing_serializer(app)

        return s.loads(session_cookie_value)


if __name__ == "__main__":
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(
        help='sub-command help', dest='subcommand')
    parser_encode = subparsers.add_parser('encode', help='encode')
    parser_encode.add_argument('-s', '--secret-key', metavar='<string>',
                               help='Secret key', required=True)
    parser_encode.add_argument('-t', '--cookie-structure', metavar='<string>',
                               help='Session cookie structure', required=True)
    parser_decode = subparsers.add_parser('decode', help='decode')
    parser_decode.add_argument('-s', '--secret-key', metavar='<string>',
                               help='Secret key', required=False)
    parser_decode.add_argument('-c', '--cookie-value', metavar='<string>',
                               help='Session cookie value', required=True)
    args = parser.parse_args()

    if args.subcommand == 'encode':
        if args.secret_key is not None and args.cookie_structure is not None:
            print(encode(args.secret_key, args.cookie_structure))
    elif args.subcommand == 'decode':
        if args.secret_key is not None and args.cookie_value is not None:
            print(decode(args.cookie_value, args.secret_key))
        elif args.cookie_value is not None:
            print(decode(args.cookie_value))

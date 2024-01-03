# Flask Session Cookie Decoder/Encoder

Original author : [**Wilson Sumanang**](https://github.com/saruberoz)

Fixes and improvements author : [**Alexandre ZANNI**](https://github.com/noraj)

Imported from [saruberoz.github.io](http://saruberoz.github.io/flask-session-cookie-decoder-slash-encoder)

Fixes author : [**JBNRZ**](https://github.com/JBNRZ)

## Depencencies

+ Python 3
+ [Flask](https://pypi.python.org/pypi/Flask)

## Usage

Use `flask_session_cookie_manager3.py` with Python 3

```
usage: flask_session_cookie_manager.py [-h] {encode,decode} ...

positional arguments:
  {encode,decode}  sub-command help
    encode         encode
    decode         decode

options:
  -h, --help       show this help message and exit
```

### Encode

```
usage: flask_session_cookie_manager.py encode [-h] -s <string> -t <string>

options:
  -h, --help            show this help message and exit
  -s <string>, --secret-key <string>
                        Secret key
  -t <string>, --cookie-structure <string>
                        Session cookie structure
```

### Decode

```
usage: flask_session_cookie_manager.py decode [-h] [-s <string>] -c <string>

options:
  -h, --help            show this help message and exit
  -s <string>, --secret-key <string>
                        Secret key
  -c <string>, --cookie-value <string>
                        Session cookie value
```

## Examples

### Encode

```
$ python flask_session_cookie_manager.py encode -s "JBNRZ" -t "{'name':'JBNRZ'}"
eyJuYW1lIjoiSkJOUloifQ.ZZVJMg.ZPGcSUBQVYq5zVgSsVq-_4eFaaM
```

**Note**: the session cookie structure must be a valid python dictionary

### Decode

With secret key:

```
$ python flask_session_cookie_manager.py decode -s "JBNRZ" -c "eyJuYW1lIjoiSkJOUloifQ.ZZVJMg.ZPGcSUBQVYq5zVgSsVq-_4eFaaM"
{'name': 'JBNRZ'}
```

Without secret key (less pretty output):

```
$ python flask_session_cookie_manager.py decode -c "eyJuYW1lIjoiSkJOUloifQ.ZZVJMg.ZPGcSUBQVYq5zVgSsVq-_4eFaaM"
b'{"name":"JBNRZ"}'
```

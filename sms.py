#!/usr/bin/python

import sys
import getopt
import urllib.request
import urllib.parse

# Change these if you know what you are doing !
user = 'xxxxx' # user id
key = 's3cr3t' # api key

# don't touch here !
def main(argv):
    msg = ''


    try:
        opts, args = getopt.getopt(argv, "m:", ["msg="])
    except getopt.GetoptError:
        print('sms.py [-m] <message>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('sms.py [-m][--msg] <message>')
            sys.exit()
        elif opt in ("-m", "--msg"):
            msg = arg
            params = urllib.parse.urlencode({'user': user, 'pass': key, 'msg': msg})
            url = "https://smsapi.free-mobile.fr/sendmsg?%s" % params
            
        try:
            req = urllib.request.urlopen(url)
            print('SMS sent.')
        except Exception as e:
            if hasattr(e, 'code'):
                if e.code == 400:
                    raise Exception('Bad syntax for request.')
                if e.code == 402:
                    raise Exception('Sms quota exceed try later.')
                if e.code == 403:
                    raise Exception(
                        'Forbidden, have you activated your account ? Account/Password error ?')
                if e.code == 500:
                    raise Exception('Try later.')

            raise Exception('Internal Error.')


if __name__ == "__main__":
    main(sys.argv[1:])


HOST='localhost'

PORT = ''

PROTOCOOL='http://'

HTTP_PROTOCOOL='https://'

def httpBaseUrl(url):
    return PROTOCOOL+HOST +PORT+url


def httpsBaseUrl(url):
    return PROTOCOOL+HOST +PORT+url

# PROTOCOOL + HOST + PORT
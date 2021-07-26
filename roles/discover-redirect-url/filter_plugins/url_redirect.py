try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

class FilterModule(object):
    def filters(self):
        return {
            'final_url': self.final_url
        }

    def final_url(self, url_var):
        resp = urlopen(url_var, timeout=3)
        redirected = resp.geturl()
        return redirected 

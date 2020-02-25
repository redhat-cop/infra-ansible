import urllib2

class FilterModule(object):
    def filters(self):
        return {
            'final_url': self.final_url
        }

    def final_url(self, url_var):
        req = urllib2.Request(url=url_var)
        resp = urllib2.urlopen(req, timeout=3)
        redirected = resp.geturl()
        return redirected 

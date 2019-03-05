def get_page(url):
	""" opening the url of the page and return it's content in as a  string"""
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
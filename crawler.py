#import urllib2
#import httplib
#import urlparse

#def get_server_status_code(url):
#    """
#    Download just the header of a URL and
#    return the server's status code.
#    """
#    host, path = urlparse.urlparse(url)[1:3]    # elems [1] and [2]
#    try:
#        conn = httplib.HTTPConnection(host)
#        conn.request('HEAD', path)
#        return conn.getresponse().status
#    except StandardError:
#        return None
 
#def check_url(url):
#    """
#    Check if a URL exists without downloading the whole file.
#    We only check the URL header.
#    """
#    good_codes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
#    return get_server_status_code(url) in good_codes

def get_page(url):
#	if check_url(url):
#		seed = urllib2.urlopen(url)
#		page = seed.read()
#		return page
	try:
		import urllib2
		return urllib2.urlopen(url).read()
	except:
		return ""


def get_next_link(page):
	start_link = page.find('<a href')
	if start_link==-1:
		return None, 0
	start_quotes = page.find('"',start_link)
	end_quotes = page.find('"',start_quotes+1)
	url = page[start_quotes+1:end_quotes]
	return url,end_quotes

def get_all_links(page):
	links=[]
	while True:
		url,end_quotes = get_next_link(page)
		if not url==None:
			links.append(url)
#			print url
			page = page[end_quotes:]
		else:
			return links
def union(p,q):
	for e in q:
		if e not in p:
			p.append(e)

def crawl_web(seed,max_depth):
	tocrawl = [seed]
	crawled = []
	next_depth = []
	depth = 0
	while tocrawl and depth<max_depth:
		page = tocrawl.pop()
		if page not in crawled:
			union(next_depth,get_all_links(get_page(page)))
			crawled.append(page)
		if not tocrawl:
			tocrawl, next_depth=next_depth, []
			depth=+1

	return tocrawl

#seed = 'https://www.udacity.com/cs101x/index.html'
seed = 'http://www.caranddriver.com/'
max_depth = 1 #defining number of webpages to be crawled
Links = crawl_web(seed,max_depth)
print Links

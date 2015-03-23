import urllib2

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False


def get_page(url):
	if internet_on():
		try:
			import urllib2
			return urllib2.urlopen(url).read()
		except:
			return ""
	else:
		print "Please check your connectivity"
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
		if not url ==None:
			# print url
			if 'http' in url:
				if not ('#' in url) :
					links.append(url)
			page = page[end_quotes:]
		else:
			return links

def get_all_keywords(page):
	keywords = []
	start_link = page.find('<meta')
	if not start_link == -1:
		key_meta_start = page.find('keywords',start_link+1)
		if not key_meta_start == -1:
			content_start = page.find('content',key_meta_start+1)
			content_start_quote = page.find('"',content_start)
			content_end_quote = page.find('"',content_start_quote+1)
			data = page[content_start_quote+1:content_end_quote]
			data = data.strip().split(',')
			for e in data:
				keywords.append(e)
	return keywords

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
			keywords = get_all_keywords(get_page(page))
			print page
			print keywords
			crawled.append(page)
		if not tocrawl:
			tocrawl, next_depth=next_depth, []
			depth=+1

	return tocrawl


seed = 'http://www.caranddriver.com/'
max_depth = 2 #defining number of webpages to be crawled
Links = crawl_web(seed,max_depth)
# print Links

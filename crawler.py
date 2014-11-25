import urllib2

def get_page(url):
	seed = urllib2.urlopen(url)
	page = seed.read()
	return page

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
			page = page[end_quotes:]
		else:
			return links
def union(p,q):
	for e in q:
		if e not in p:
			p.append(e)

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			union(tocrawl,get_all_links(get_page(page)))
			crawled.append(page)
	return crawled

seed = 'http://ayusharma.in/index.html'
Links = crawl_web(seed)
print Links

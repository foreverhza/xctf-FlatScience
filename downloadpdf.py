import urllib.request
import re

allHtml=[]
count=0
pat_pdf=re.compile("href=\"[0-9a-z]+.pdf\"")
pat_html=re.compile("href=\"[0-9]/index\.html\"")


def my_reptile(url_root,html):
	global pat_pdf
	global pat_html
	html=url_root+html
	
	if(isnew(html)):
		allHtml.append(html)
		
		print("[*]starting to crawl site:{}".format(html))
		with urllib.request.urlopen(html) as f:
			response=f.read().decode('utf-8')
			
		pdf_url=pat_pdf.findall(response)
		for p in pdf_url:
			p=p[6:len(p)-1]
			download_pdf(html+p)
			
		html_url=pat_html.findall(response)
		for h in html_url:
			h=h[6:len(h)-11]
			my_reptile(html,h)
		
def download_pdf(pdf):
	global count
	
	fd=open(str(count)+'.pdf','wb')
	count+=1
	
	print("[+]downloading pdf from site:{}".format(pdf))
	with urllib.request.urlopen(pdf) as f:
		fd.write(f.read())
	fd.close()
	
def isnew(html):
	global allHtml
	for h in allHtml:
		if(html==h):
			return False
	return True

#my_reptile("http://159.138.137.79:54253/",'')

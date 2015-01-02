import urllib.request as urllib2

idgen = range(1, 3753)
kwgen = ''

response = urllib2.urlopen('http://www.wizards.com/dndinsider/compendium/display.aspx?page=item&id=3752')
print(response.readlines())
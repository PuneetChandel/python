# minumum number of pages to move to go to a particular page in a book

def findpages(nofpages, page):
    fromstart=math.ceil((page-1)/2)
    fromend = math.floor((nofpages-page)/2) if n%2 !=0 else  math.ceil((nofpages-page)/2)
  
    return fromstart if fromstart< fromend else fromend
    

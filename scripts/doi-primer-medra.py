import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

outF = open('medra-published.csv', 'a')
# outF.write('year,result\n')     

for year in range(2013, 2016):
  browser.get('https://www.medra.org/en/search.htm')
  year = str(year)
  elem = browser.find_element_by_name('year')
  elem.send_keys(year + Keys.RETURN)
  time.sleep(500)
  elems = browser.find_elements_by_class_name('TESTORESIZBOLD')
  x = elems[1]
  m1 = re.search('Number of results: \d+', x.text)
  y = m1.group(0)
  m2 = re.search('\d+', y)
  res = int(m2.group(0))
  outF.write(str(year) + ',' + str(res) + '\n')


outF.close()

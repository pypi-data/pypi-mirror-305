import urllib.request

try:
  from bs4 import BeautifulSoup
except:
  print('You need to install BeautifulSoup (bs4).')

def fetch(url):
  with urllib.request.urlopen(url) as request:
    return request.read()

def searchOnIntelArk(query):
  return fetch('https://ark.intel.com/content/www/us/en/ark/search.html?_charset_=UTF-8&q=' + urllib.parse.quote(query))

def parse_results(html_content):
  soup = BeautifulSoup(html_content, 'html.parser')
  results = []

  for item in soup.find_all('a', class_='ark-accessible-color'):
    processor_name = item.text.strip()
    if not (processor_name.__contains__('Processors') or processor_name == 'Products Home' or processor_name == '' or processor_name == 'Product Specifications'):
      processor_name = processor_name.split(' Processor')[0]
      processor_page_url = 'https://ark.intel.com/' + item.attrs['href']
      processor_soup = BeautifulSoup(fetch(processor_page_url), 'html.parser')
      code_name = processor_soup.find('span', {'data-key': 'CodeNameText'}).find('a').text or None
      if 'formerly' in code_name:
        code_name = code_name.split('formerly ')[1]
      results.append({'name': processor_name, 'codeName': code_name})
    
  return results

def intel_ark_lookup(query):
  html_content = searchOnIntelArk(query + ' ')
  processors = parse_results(html_content)
  if not processors:
    return "No results found for the specified query."
    
  return processors

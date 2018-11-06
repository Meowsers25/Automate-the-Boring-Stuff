import bs4

example_file = open('index.html')
example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
print(type(example_soup))
elems = example_soup.select('#author')
print(elems)
print(type(elems))
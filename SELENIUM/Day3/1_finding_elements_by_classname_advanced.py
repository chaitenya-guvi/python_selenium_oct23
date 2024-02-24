"""
Every	element	does	not	have	an	id	->	static	id,	unique	name,
unique	link	text.	For	those	elements	we	need	to	build	xpath	to
find	and	then	perform	actions	on	them.

Whatever	we	use	to	find	an	element,	id,	name,	xpath,	css -> It
should	always	be	unique.

It	should	only	find	one	matching	node	unless	we	want	to	capture
a	list	of	elements.
Syntax:

tag[attribute='value']
“#”	->	Id
“.”	->	Class
Element	Displayed	Example	Text	Box:
input[id=displayed-text]
#displayed-text
input#displayed-text
input[class=displayed-class]
.displayed-class
input.displayed-class



Appending	Classes
.class1.class2.class3	->	Until	we	find	a	unique	element

Using	wildcards	in	CSS	Selectors:
“^”	->	Represents	the	starting	text
“$”	->	Represents the	ending	text
“*”	->	Represents	the	text	contained

Syntax:
tag[attribute<special	character>=’value’]
Examples:
input[class='inputs']	->	Only	1	matching	node
input[class^='inputs']	->	Two	matching	nodes
input[class='displayed-class']	- No	matching	nodes
input[class$='class']	->	One	matching	node
input[class*='displayed-class']	->	One	matching	node
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



driver = webdriver.Firefox()

url = "https://www.letskodeit.com/practice"

driver.get(url)


driver.maximize_window()

sleep(2)


webelements_of_left_align_class = driver.find_elements(By.CLASS_NAME, "left-align")
print(webelements_of_left_align_class)
print(len(webelements_of_left_align_class))

for element in webelements_of_left_align_class :
    print(element.get_attribute("id"))



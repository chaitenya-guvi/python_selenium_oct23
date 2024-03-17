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

url = "https://qavbox.github.io/demo/signup/"

driver.get(url)

driver.maximize_window()

sleep(2)


webelement_of_username_using_CSS = driver.find_element(By.CSS_SELECTOR,'#username')
webelement_of_username_using_CSS.send_keys("ABCD")
print("found using css")

webelement_of_email_using_CSS = driver.find_element(By.CSS_SELECTOR,'#email')
webelement_of_email_using_CSS.send_keys("ABCD@email.com")
print("2 found using css")






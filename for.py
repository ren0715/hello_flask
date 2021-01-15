from jinja2 import Environment,FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('for.html')

fruits = ["Apple","Banana","Kiwi"]
disp_text = template.render(fruits = fruits)
print(disp_text)
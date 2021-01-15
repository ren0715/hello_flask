from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

template = env.get_template('hello.html')

output = template.render(name='Taro', lang='Python')

print(output)
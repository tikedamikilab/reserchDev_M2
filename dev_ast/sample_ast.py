import ast

FILENAME = './dev_ast/target.py'

with open(FILENAME, 'r') as f:
    source = f.read()

tree = ast.parse(source, FILENAME)

print(tree.body[1].lineno)
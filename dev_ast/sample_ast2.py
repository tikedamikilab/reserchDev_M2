# -*- coding: utf-8 -*-

from __future__ import print_function

import ast

def walk(node, indent=0):
    # 入れ子構造をインデントで表現する
    print(' ' * indent, end='')

    # クラス名を表示する
    if node.__class__ != '_ast.Num':
        print(node.__class__, end='')

        # 行数の情報があれば表示する
        if hasattr(node, 'lineno'):
            msg = ': {lineno}'.format(lineno=node.lineno)
            print(msg, end='')

    # 改行を入れる
    print()

    # 再帰的に実行する
    for child in ast.iter_child_nodes(node):
        walk(child, indent=indent+4)

def main():
    FILENAME = './dev_ast/target2.txt'

    with open(FILENAME, 'r') as f:
        source = f.read()

    tree = ast.parse(source, FILENAME)
    walk(tree)

if __name__ == '__main__':
    main()
import ast

class Collection:
    def __init__(self, name='', def_line_no=0, last_line_no=0):
        self.name = name
        self.def_line_no = def_line_no
        self.last_line_no = last_line_no


class MethodLastLineNoCollector:
    def __init__(self):
        self.result = {}
        self.searched_line_no = 0

    def run(self, node):
        if isinstance(node, ast.FunctionDef):
            self.result[node.lineno] = Collection(node.name, def_line_no=node.lineno)

        for child in ast.iter_child_nodes(node):
            self.run(child)
        
        if hasattr(node, 'lineno'):
            # 探索した最終行を取得
            # 再帰で探すので、node.linenoは 1 > 2 > 3 > 2 > 1 となる
            if node.lineno > self.searched_line_no:
                self.searched_line_no = node.lineno

            # 再帰で探した時の帰りに、最終行を設定する
            else:
                if self.result.get(node.lineno):
                    self.result[node.lineno].last_line_no = self.searched_line_no


if __name__ == '__main__':
    FILENAME = 'target.py'
    with open(FILENAME, 'r') as f:
        source = f.read()

    tree = ast.parse(source, FILENAME)

    collector = MethodLastLineNoCollector()
    collector.run(tree)

    for v in collector.result.values():
        print(f'{v.name} -> def:{v.def_line_no}, last:{v.last_line_no}')
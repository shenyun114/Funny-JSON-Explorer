import json
import argparse
from iconFamily import icon_families
from codeIterator import *
from codeVisualization import *

# 访问者接口
class Visitor:
    def __init__(self, iterator=None):
        self.iterator = iterator
    
    def visit(self):
        pass

# 具体访问者
class JsonVisitor(Visitor):
    def __init__(self, iterator=None):
        super().__init__(iterator)
    
    def visit(self, styleVisualization):
        print("The style is:", styleVisualization.type)
        styleVisualization.getRes()
        iterator = JsonIterator(styleVisualization)
        for item in iterator:
            print(item)

# FJE
class FunnyJsonExplorer:
    def __init__(self, data=None, type=None, icon=None):
        self.data = data
        self.style = type
        self.icon = icon
    
    def explore(self):
        # 访问
        if self.style == 'tree':
            styleVisualization = TreeVisualization(icon_families[self.icon], self.data)
        elif self.style == 'rectangle':
            styleVisualization = RectangleVisualization(icon_families[self.icon], self.data)
            
        visitor = JsonVisitor()
        styleVisualization.accept(visitor)
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='JSON file path')
    parser.add_argument('-s', '--style', help='style')
    parser.add_argument('-i', '--icon', help='Icon family')
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        data = json.load(f)
    
    print("The Middle icon is:", icon_families[args.icon][0])
    print("The Leaf icon is:", icon_families[args.icon][1])
    
    fje = FunnyJsonExplorer(data, args.style, args.icon)
    fje.explore()
    

if __name__ == '__main__':
    main()
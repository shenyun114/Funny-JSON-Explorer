import json
import argparse
from codeBuilder import *
from iconFamily import icon_families

# Director
class FunnyJsonExplorer:
    def __init__(self, builder):
        self.builder = builder
    
    def load(self, data):
        # print("load: ", self.builder.factory.icon_family)
        self.builder.build_product(data)
    
    def show(self):
        result = self.builder.get_product()
        self.builder.draw(result)

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
    
    # Factory Pattern
    styleFactory = StyleFactory(args.icon, args.style)
    factory = styleFactory.getFactory()
    
    builder = JsonBuilder(factory)
    director = FunnyJsonExplorer(builder)
    director.load(data)
    director.show()

if __name__ == '__main__':
    main()
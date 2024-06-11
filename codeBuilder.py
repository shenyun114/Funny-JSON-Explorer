from factory import *

class Builder:
    def __init__(self, factory):
        self.factory = factory
        self.output = []
    
    def build_product(self):
        pass
    
    def get_product(self):
        pass
    
    def draw(self):
        pass


class JsonBuilder(Builder):
    def __init__(self, factory):
        super().__init__(factory)
        self.output = []

    def build_product(self, data):
        # print("build_product: ", self.factory.icon_family)
        # self.factory = self.getFactory(data)
        self.style = self.factory.getStyle()
        self.output = self.style.buildStructure(data)
    
    def get_product(self):
        return self.output
    
    def draw(self, result):
        for line in result:
            print(line)
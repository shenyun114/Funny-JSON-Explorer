from iconFamily import icon_families
from codeVisualization import *

class StyleFactory:
    def __init__(self, icon_family, style):
        self.icon_family = icon_family
        self.style = style
    
    # Factory Pattern
    def getFactory(self):
        if self.style == 'tree':
            return TreeFactory(self.icon_family, self.style)
        elif self.style == 'rectangle':
            return RectangleFactory(self.icon_family, self.style)
        else:
            print('Invalid style')
            return None
    
    def getStyle(self):
        if self.style == 'tree':
            return TreeStyle(self.icon_family, self.style)
        elif self.style == 'rectangle':
            return RectangleStyle(self.icon_family, self.style)
        else:
            print('Invalid style')
            return None

class TreeFactory(StyleFactory):
    def __init__(self, icon_family, style):
        super().__init__(icon_family, style)
    
    def getStyle(self):
        return TreeStyle(self.icon_family, self.style)

class RectangleFactory(StyleFactory):
    def __init__(self, icon_family, style):
        super().__init__(icon_family, style)
    
    def getStyle(self):
        return RectangleStyle(self.icon_family, self.style)

# Abstract Factory Method
class Style:
    def __init__(self, icon_family, style):
        self.icon_family = icon_families[icon_family]
        self.style = style
    
    # Factory Pattern
    def buildStructure(self, codeData):
        pass

# 树形
class TreeStyle(Style):
    def __init__(self, icon_family, style):
        super().__init__(icon_family, style)
    
    def buildStructure(self, codeData):
        # print("buildStructure:", self.icon_family)
        tree = TreeVisualization(icon_family=self.icon_family)
        tree.createConversion(codeData)
        tree.rebuildOutput()
        return tree.output
        
# 矩形
class RectangleStyle(Style):
    def __init__(self, icon_family, style):
        super().__init__(icon_family,style)
        
    def buildStructure(self, codeData):
        rectangle = RectangleVisualization(self.icon_family)
        rectangle.createConversion(codeData)
        rectangle.rebuildOutput()
        return rectangle.output
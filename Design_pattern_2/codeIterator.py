# code遍历迭代器
class codeIterator:
    def __init__(self, styleVisualization=None):
        self.styleVisualization = styleVisualization
        self.length = 0 if styleVisualization is None else len(styleVisualization.output)
        self.index = 0
    
    def has_last_code(self):
        return self.index < self.length
        
    def get_next_code(self):
        if not self.has_last_code():
            return None
        code = self.styleVisualization.output[self.index]
        self.index += 1
        return code

# 迭代器具体实现
class JsonIterator(codeIterator):
    def __init__(self, styleVisualization=None):
        super().__init__(styleVisualization)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.has_last_code() == False:
            raise StopIteration
        else:
            return self.get_next_code()
    
    # def has_last_code(self):
    #     if self.styleVisualization is None:
    #         print("The styleVisualization is None!")
    #         return False
        
    #     if self.length == 0:
    #         print("The length of styleVisualization is 0!")
    #         return False
        
    #     # 是不是最后一个代码
    #     if self.index == self.length:
    #         return False
    #     else:
    #         return True
          
    # def get_next_code(self):
    #     if self.has_last_code() == False:
    #         return None
    #     elif self.has_last_code() == False:
    #         return None
        
    #     # 迭代器的下一个代码
    #     code = self.styleVisualization.output[self.index]
    #     self.index += 1
    #     return code

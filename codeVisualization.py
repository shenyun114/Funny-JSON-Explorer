class DataVisualization:
    def __init__(self, icon_family, data=None):
        self.icon_family = icon_family
        self.data = data
        self.output = []
    
    def createConversion(self, data, level=0, parent_last=[]):
        pass
    
    def rebuildOutput(self):
        # 重新构建输出
        pass

# ├─ oranges
# │  └─ mandarin
# │     ├─ clementine
# │     └─ tangerine: cheap & juicy!
# └─ apples
#    └─ gala  
   
class TreeVisualization(DataVisualization):
    def __init__(self, icon_family, data=None):
        super().__init__(icon_family, data)
        self.output = []

    def createConversion(self, data, level=0, parent_last=[]):
        # 可视化为树形
        for i, (key, value) in enumerate(data.items()):
            is_last = i == len(data) - 1
            sign  = (self.icon_family[0] if level == 0 else self.icon_family[1]) + " "
            prefix = ''.join('│  ' if not last else '   ' for last in parent_last)
            prefix += '└─' if is_last else "├─"
            if isinstance(value, dict):
                finalStr = prefix + sign + str(key)
                self.output.append(finalStr)
                self.createConversion(value, level + 2, parent_last + [is_last])
            else:
                finalStr = prefix + sign + str(key) + ("" if value is None else (": " + str(value)))
                self.output.append(finalStr)

    def rebuildOutput(self):
        # 对于树形无需修正格式
        pass

# ┌─ oranges ───────────────────────────────┐
# │  ├─ mandarin ───────────────────────────┤
# │  │  ├─ clementine ──────────────────────┤
# │  │  ├─ tangerine: cheap & juicy! ───────┤
# ├─ apples ────────────────────────────────┤
# └──┴─✩gala ───────────────────────────────┘

class RectangleVisualization(DataVisualization):
    def __init__(self, icon_family, data=None):
        # 写在一起避免覆盖
        super().__init__(icon_family, data)
        self.output = []
    
    def createConversion(self, data, level=0, parent_last=[]):
        # 可视化为矩形
        for i, (key, value) in enumerate(data.items()):
            is_last = i == len(data) - 1
            # 判断是否是最后一行输出
            all_last = is_last
            for last in parent_last:
                all_last *= last
            sign  = (self.icon_family[0] if level == 0 else self.icon_family[1]) + " "
            prefix = ''.join('│  ' * len(parent_last))
            if level == 0 and i == 0:
                prefix = '┌─'
            elif all_last and not isinstance(value, dict):
                prefix += "┴─"
                prefix = "└─" + prefix[2:]
                prefix = prefix.replace(' ', '─')
            else:
                prefix += "├─"
            
            if isinstance(value, dict):
                finalStr = prefix + sign + str(key)
                self.output.append(finalStr)
                self.createConversion(value, level + 2, parent_last + [is_last])
            else:
                finalStr = prefix + sign + str(key) + ("" if value is None else (": " + str(value)))
                self.output.append(finalStr)
    
    def rebuildOutput(self):
        # 对于矩形需要修正格式
        maxLen = max([len(i) for i in self.output]) + 10
        for i in range(len(self.output)):
            if i == 0:
                # 增长到maxlen
                self.output[i] = self.output[i].ljust(maxLen, '─')
                self.output[i] = self.output[i][:maxLen - 1] + '┐'
            elif i == len(self.output) - 1:
                self.output[i] = self.output[i].ljust(maxLen, '─')
                self.output[i] = self.output[i][:maxLen - 1] + '┘'
            else:
                self.output[i] = self.output[i].ljust(maxLen, '─')
                self.output[i] = self.output[i][:maxLen - 1] + '│'
        
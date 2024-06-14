### 使用迭代器+访问者模式重构FJE

为了重构现有的FunnyJsonExplorer实现，我们将采用迭代器和访问者模式。这种设计允许我们遍历复杂的数据结构，如JSON，同时提供一个机制来对这些数据执行操作，而不需要修改数据结构本身。

#### 重构计划

1. 迭代者模式：实现一个迭代器来遍历JSON数据结构。这个迭代器将提供一种方法来逐一访问数据元素，而不暴露数据结构的内部表示。
2. 访问者模式：定义一个访问者接口，该接口声明了一系列访问方法，用于对不同类型的JSON元素（如对象、数组、值）执行操作。然后，实现具体的访问者类来执行特定的操作。

#### 伪代码

1. **迭代器接口** (`JsonIterator`)：定义`has_next`和`next`方法。
2. **具体迭代器** (`ConcreteJsonIterator`)：实现`JsonIterator`，用于遍历JSON数据。
3. **访问者接口** (`JsonVisitor`)：定义访问不同JSON元素的方法。
4. **具体访问者** (`DisplayVisitor`)：实现`JsonVisitor`，用于显示JSON数据。
5. **修改FunnyJsonExplorer**：使用迭代器来遍历JSON数据，并使用访问者来执行操作。

#### 代码实现：

```python
import json

# 迭代器接口
class JsonIterator:
    def has_next(self):
        pass

    def next(self):
        pass

# 具体迭代器
class ConcreteJsonIterator(JsonIterator):
    def __init__(self, data):
        self.data = data
        self.index = -1
        self.keys = list(data.keys()) if isinstance(data, dict) else range(len(data))

    def has_next(self):
        return self.index + 1 < len(self.keys)

    def next(self):
        if self.has_next():
            self.index += 1
            key = self.keys[self.index]
            return self.data[key] if isinstance(self.data, dict) else self.data[key], key
        else:
            return None, None

# 访问者接口
class JsonVisitor:
    def visit_object(self, obj):
        pass

    def visit_array(self, array):
        pass

    def visit_value(self, value):
        pass

# 具体访问者
class DisplayVisitor(JsonVisitor):
    def visit_object(self, obj):
        print("Object:", obj)

    def visit_array(self, array):
        print("Array:", array)

    def visit_value(self, value):
        print("Value:", value)

# 修改 FunnyJsonExplorer 使用迭代器和访问者
class FunnyJsonExplorer:
    def __init__(self, data):
        self.data = data

    def explore(self, visitor):
        if isinstance(self.data, dict):
            visitor.visit_object(self.data)
        elif isinstance(self.data, list):
            visitor.visit_array(self.data)
        else:
            visitor.visit_value(self.data)

        iterator = ConcreteJsonIterator(self.data)
        while iterator.has_next():
            value, key = iterator.next()
            FunnyJsonExplorer(value).explore(visitor)

# 示例使用
if __name__ == '__main__':
    data = json.loads('{"name": "John", "age": 30, "cars": ["Ford", "BMW"]}')
    explorer = FunnyJsonExplorer(data)
    visitor = DisplayVisitor()
    explorer.explore(visitor)
```


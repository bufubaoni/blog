# django rest framework
发现用这个框架很久了，很少去深层次的了解这个框架，没有很透彻的去看待这个框架。

最近发现一个很有意思都问题，当然这个可能不是一个问题，但是我觉得挺好的来分享一下

```python
def inc(x):
    return x + 1


def function_dir(methods=None, **kwargs):
    methods = ['get'] if (methods is None) else methods

    def decorator(func):
        func.bind_to_methods = methods
        func.detail = False
        func.kwargs = kwargs
        return func
    return decorator

class A(object):
    def __init__(self):
        self.x = 'ccccc'

    def get_x(self):
        return self.x


if __name__ == "__main__":
    a = A()
    print a.get_x()
    print a.get_x
    print inc

>>> ccccc
>>> <bound method A.get_x of <__main__.A object at 0x10fc4c990>>
>>> <function inc at 0x10fc37c08>

```
这个是一个实际的例子，也就是说 A类下的 方法 会被解释成当前bound方法，而module中function会被解释成function,
如果我们为 get_x 这个类方法加上一个装饰器那么 就可以拿到这个fun 而不是单独的一个bound method， 也就是说在 drf 类中每一个method 是一个方法，而不是单独的类方法。

## 序列化
view 中需要将context 传递到序列化中 parent 会传递上一级的instance，但是多级传递的时候会导致source 的丢失

## 自定义field
需要自定义field的时候，一般情况下至需要重写`to_representation`即可，重写`to_internal_value`会更专业一点
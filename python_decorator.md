# decorator
这是一个老生常谈的东西，以前一只很模糊，后来用的越来越多之后发现其实就是一个语法糖。

这个专题也不用写那么高深，就写那么几个例子

```python
import time

def task_log(task):
    def decorator(*a, **k):
        time.time()
        res = task(*a, **k)
        time.time()
        return res

    return decorator


def task_log_para(para):
    def wrapping(task):
        def decorator(*a, **k):
            print(para)
            return task(*a, **k)

        return decorator

    return wrapping


@task_log
@task_log_para("para 1")
def test(a):
    raise Exception
    return a

if __name__ == '__main__':
    test("asdffff")
```

以上例子写了两个不能再简单的装饰器，一个无参数的装饰器和一个，和一个可以接受参数的装饰器

`task_log`是一个不可接受参数的装饰器
里边的高级函数的参数是被装饰的函数的参数，那么除了额外对函数做一些patch或者log记录的操作外，也可以对参数进行校验，再大部分web服务器中，如果可以获得参数那么里边的`arg`和`kwargs`很多是客户端传来的参数，此时可以对参数进行校验和重新patch，对于一些classview可以将参数以类的属性patch。


`task_log_para`是一个可以接受参数的装饰器，参数分为两部分，第一层次的是整个装饰器参数，第二层是被装饰函数的参数。这个用途除了和不接受参数的装饰器功能类似以外，我们可以对整个高阶函数进行配置，那么配置阶段比较靠前，会在整个程序运行之前，所以此装饰装饰类方法的时候，如果要使用类的相关属性，需要在第一个参数获取整个实例，然后通过实例方法。如果要使用被装饰的函数的参数，则需要传递一个lambda给整个装饰，并在内部调用，例如缓存策略的时候会使用这种比较trick的方法来进行缓存，而不是在函数内部进行set。

装饰器的好处

1. 可以不修改函数逻辑，而对整个函数，参数，结果进行校验
2. 方便使用（还有什么比添加一个新功呢，然后加一个 @decorator ）-----还真有（在 中间件中修改然后做 filter 当然这个是系统架构的问题，如果设计之初就没有中间件）

装饰器注意
1. 是否需要接受参数
2. 装饰函数的其他属性是否需要继承
3. 装饰函数的参数和关键字
4. 装饰器的执行顺序（由上到下，如果是带有参数的装饰器会有一次预加载）

也没有什么好总结的，以上就是所有想说的。
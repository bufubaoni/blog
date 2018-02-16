# Rust
老规矩，写在最前。rust的学习其实是17年的计划，但是一直拖到了18年，16年听说的rust。学了那么多动态语言，用一门静态语言处理问题而已，仅仅是换了一门语言而已。可能对小众语言的偏好吧，java虽然也写，但是仍然喜欢不起来。
## 安装
之前一只win机子，然后横亘在面前的就是安装
切换到 *nux 上之后貌似就简单了起来，
使用命令就安装清楚了，连并 cargo
 - curl https://sh.rustup.rs -sSf | sh

## 项目开始
 - cargo new <pro-name> --bin
cargo 会创建一个pro-name 的项目结构，
```
    pro-name
        |
        +---src/main.rs
        |
        +---.gitignore
        |
        +---Cargo.toml
        |
        +---Cargo.lock
```
其中`Cargo.toml`文件为项目依赖，`Cargo.lock`为跟踪文件(多数情况下不需要手动修改)
## 语法
或许这一部分是最简单的部分了。

比较不同的一点就是 如果使用一个变量那么那么需要将 `let mut a = 5`此时才是一个变量，当然里边有很对概念说变量，虽然有所不同，但是仍然可以跳过。

## 爬虫
我想任何一个语言开始，总要从最容易得到反馈都开始，对于我自己而言应该就是爬虫了吧。

第一步我们肯定要从依赖开始，我当然不想从写socket 开始了，所以使用了依赖`hyper`。

在`Cargo.toml`中写入依赖
```
    [dependencies]
    futures = "0.1"
    hyper = "0.11"
    tokio-core = "0.1"
```
在文件中引入依赖
```rust
extern crate futures;
extern crate hyper;
extern crate tokio_core;

use std::io::{self, Write};
use futures::{Future, Stream};
use hyper::Client;
use tokio_core::reactor::Core;

fn main() {
    let mut core = Core::new().unwrap();
    let client = Client::new(&core.handle());
    let uri = "http://httpbin.org/ip".parse().unwrap();
    let work = client.get(uri).and_then(|res| {
        println!("Response: {}", res.status());
        res.body()
            .for_each(|chunk| io::stdout().write_all(&chunk).map_err(From::from))
    });
    core.run(work).unwrap();
}

```
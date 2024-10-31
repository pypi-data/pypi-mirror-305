# testtools-cli
testtools命令行工具，主要提供脚手架辅助功能

## 安装

```shell
pip install testtools-cli
```

## 如何使用

### ✨testtools-cli init

在指定目录(默认当前目录)创建测试工具脚手架内容,当前支持语言：

- python
- golang

使用例子：

```shell
testtools-cli init
```

```shell
testtools-cli init --workdir /tmp/jagma
```

> 测试工具建议使用小写英文名称。

### 🪄testtools-cli check

检查指定目录(默认当前目录)的脚手架内容还有哪些要修改的。

- \_\_TODO\_\_: 必须实现的部分

> 必须实现的部分主要包括用例的**加载**、**执行**以及**结果的上报**

- \_\_RECOMMANDTODO\_\_: 建议实现的部分

> 建议实现的部分主要为工具的元数据信息，包括homePage（工具主页）、repository（工具源码地址）、gitPkgUrl以及httpPkgUrl（工具压缩包地址）等

## 开发说明

脚手架内容按照语言统一放到 [脚手架目录](./src/testtools_cli/generator/scaffold) 下面。模板语言使用Jinja2，只有2条简单规则：

- 文件内容中的`{{name}}`会被替换为输入的工具名称
- 路径中的`{{name}}`会被替换为输入的工具名称
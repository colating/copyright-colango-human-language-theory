# 相关工具

### 在根目录下，在 index.md 文件中，目录书签链接的方法；与其他文件不同

```
用途说明 </tools/search>  
```
- 在根目录下，在 index.md 文件中，目录书签，会展示在整个网站的左侧菜单。需要指出明确的文件名称，即使是 index.md文件也需要。
- 普通 md文件，采用 md链接语法。
```
[说明](abc/de)
```


<!-- :hidden: -->
<!-- :caption: Tools List -->

```{eval-rst}

.. toctree::
   :glob:
   :maxdepth: 2

   editor/*
   extensions/*
   md/*
   sphinx/*
   linux/*
```


  


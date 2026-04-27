# ERROR：MyST & Sphinx 错误记录

## MyST

### 1. readthedocs Myst markdown 中 ＞ 语法(引用块)无效：Gug ？
与 ​​​markdown-it parser guide​​ 有关？

#### 解决方法

方法一

向右缩进 >= 4 个空格。在官网上测试也是这个效果 https://myst-parser.readthedocs.io/en/latest/live-preview.html

方法二：{eval-rst}

```  
```{eval-rst}
.. include:: snippets/include-rst.rst
```  

---

### 2. 


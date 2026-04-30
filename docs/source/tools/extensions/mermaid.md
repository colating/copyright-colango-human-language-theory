# Mermaid ：Directive Examples 


## ```{mermaid} 后需要一个空行

```{mermaid} 
/* 这里需要一个空行: 配置文件的---造成的？ */
---
title: Hel Title
config:
  theme: base
  themeVariables:
    primaryColor: "#ffff00"
---
flowchart
	Hello --> World
```


## venn 维恩:交集图形

## treemap-beta

```{mermaid} 

treemap-beta
"Section 1"
    "Leaf 1.1": 12
    "Section 1.2"
      "Leaf 1.2.1": 12
"Section 2"
    "Leaf 2.1": 20
    "Leaf 2.2": 25
```

$ pip show sphinxcontrib-mermaid
Name: sphinxcontrib-mermaid
Version: 2.0.1
```{mermaid}  # 2.0.1 还不支持？
venn-beta
    title "Three overlapping sets"
    set A
    set B
    union A,B["AB"]
    style A,B fill:skyblue
```


## 指令已被弃用 Directives 
警告  https://mermaid.js.org/config/directives.html#directive-examples 
从v10.5.0开始，指令已被弃用。请使用frontmatter中的config键传递配置。有关更多详细信息，请参阅配置。

Now that the concept of directives has been explained, let us see some more examples of directive usage:
Changing theme via directive

The following code snippet changes theme to forest:

%%{init: { "theme": "forest" } }%%

Possible theme values are: default, base, dark, forest and neutral. Default Value is default.

Example:

Code:

```
%%{init: { "theme": "forest" } }%%
graph TD
A(Forest) --> B[/Another/]
A --> C[End]
  subgraph section
  B
  C
  end
```




# 待办事项列表

[todo 模板](/tools/template/todo-template)

[todo 常用命令]</tools/extension/template/stodo-usage>


/* [tmp-test](tmp-test) */

[xmd](xmd)

[xrst](xrst)



```{mermaid}

graph TD
    A["<span style='display:inline-block; min-width:500px;'>短文本</span>"] --> B[正常节点]


```


 

---

```{mermaid}


graph TD
    A[span style]
    B[正常节点]
    
    A --> B
   classDef default fill:#f9f,stroke:#333,stroke-width:2px;
    
``` 

# todo 模板代码

```{eval-rst}

.. mermaid::

graph TD
    A[span style]
    B[正常节点]
    
    A --> B
   
    
``` 


---


```{eval-rst}
.. todolist::
```


## {eval-rst}

```{eval-rst}
.. todo::
   :class: warning

  In 测试 1111。
```





    
    
    
    

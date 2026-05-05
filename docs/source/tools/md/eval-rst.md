# {eval-rst}

https://osgeo.cn/sphinx-note/myst-zhinan.html

```{eval-rst}
.. figure:: ./fun-fish.png
  :width: 100px
  :name: rst-fun-fish

  Party time!

A reference from inside: :ref:`rst-fun-fish`

A reference from outside: :ref:`syntax/guide/parsing`
```

```<无空格>{eval-rst}
.. < 1个空格>figure:: ./fun-fish.png
  :width: 100px
  :name: rst-fun-fish

< 3个空格> dir/index  ##这里一定要 3个空格！！！！！！
```


## 两列显示

::::{grid} 2
 
:::{grid-item}
**测试 A**
 
如果看到这段文字，说明 Grid 基础功能正常。
:::
 
:::{grid-item}
**测试 B**
 
如果看到这段文字，说明列渲染正常。
:::
 
::::

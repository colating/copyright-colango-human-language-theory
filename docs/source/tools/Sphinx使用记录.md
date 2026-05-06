# Sphinx使用记录

## .. toctree:: 的目录结构

在主 index文件中：

```
.. toctree::
   :glob:
   :maxdepth: 2
   :caption: 自定义目录标题

   /dir/index
```
由于 /dir/index 在子目录下，因此：
- 当在 /dir/index中有可用标题时，RTD左侧菜单将显示之。
- 当在 /dir/index中没有可用标题时，RTD左侧菜单将显示在 /dir/index中索引的下一级标题。

---

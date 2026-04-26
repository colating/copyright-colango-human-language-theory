# sphinx，TODO插件的使用方法

[myst-parser.readthedocs.io](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html)

[引用和交叉引用](https://daobook.github.io/jupyter-book-zh/content/references.html)


## 安装

### 1. 启用扩展

首先，需要在项目的配置文件 ​​conf.py​​ 中启用该扩展。将 ​​'sphinx.ext.todo'​​ 添加到 ​​extensions​​列表中：

    # conf.py
    extensions = [
        'sphinx.ext.todo',
        # 其他扩展...
    ]

### 2. 配置选项

默认情况下，TODO 条目不会出现在最终生成的文档中。你需要通过配置变量来控制其行为。在 ​​conf.py​​中添加以下配置项：

- ‘todo_include_todos’​‌ (bool):
  - True​​: 在输出中包含 ​​.. todo::​​ 和 ​​.. todolist::​​指令的内容。
  - ​​False​​ (默认): 不生成任何 TODO 相关输出。
  
- ‘todo_emit_warnings​‌’ (bool, 版本 1.5+):
  - True​​: 为每个 TODO 条目发出警告信息。这有助于在构建日志中发现未完成的项。
  - False​​ (默认): 不发出警告。
  
- ‘todo_link_only’​‌ (bool, 版本 1.4+):
  - ​​True​​: ​​.. todolist::​​ 生成的列表仅包含链接，不包含文件路径和行号。
  - False​​ (默认): 显示完整的路径和行号信息。
  
---

### todo 插件使用方法总结

1. 在 conf.py 中添加 'sphinx.ext.todo' 到 extensions。
2. 设置 todo_include_todos = True 以在输出中显示 TODO。
3. 在 .rst 文件中使用 .. todo:: 编写待办事项。
4. 使用 .. todolist:: 在一个集中位置展示所有待办事项。

##### 显示 TODO:‌

```bash
    sphinx-build -b html -D todo_include_todos=1 source build/html
```

##### 隐藏 TODO:‌

```bash
    sphinx-build -b html -D todo_include_todos=0 source build/html
```
---

## 示例

```{eval-rst}
.. todo::
   :class: danger
   
   【高优先级】修复核心崩溃问题

.. todo::
   :class: warning
   
   【中优先级】优化加载速度

.. todo::
   :class: note
   
   【低优先级】更新文档拼写错误

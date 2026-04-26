# sphinx todo 插件，怎样使用                  

## sphinx todo 插件，怎样使用
  
  
  
## 总结

1. 在 conf.py 中添加 'sphinx.ext.todo' 到 extensions。
2. 设置 todo_include_todos = True 以在输出中显示 TODO。
3. 在 .rst 文件中使用 .. todo:: 编写待办事项。
4. 使用 .. todolist:: 在一个集中位置展示所有待办事项。

这样，你就可以有效地在 Sphinx 文档中管理和跟踪开发任务了。

## 命令行覆盖配置

你可以在构建文档时通过命令行参数临时覆盖 conf.py 中的设置，而无需修改配置文件。这在 CI/CD 流程中非常有用，例如只在开发构建中显示 TODO，而在发布构建中隐藏。

#### 显示 TODO:‌

```bash
    sphinx-build -b html -D todo_include_todos=1 source build/html
```
#### 隐藏 TODO:‌

```bash
    sphinx-build -b html -D todo_include_todos=0 source build/html
```


# sphinx todo 插件，怎样使用

在 Sphinx 中使用 sphinx.ext.todo 扩展可以帮助你在文档中添加待办事项（TODO）条目，并可以选择性地显示或隐藏它们。以下是详细的使用指南：

1. 启用扩展

首先，需要在项目的配置文件 conf.py 中启用该扩展。将 'sphinx.ext.todo' 添加到 extensions列表中：
```python
# conf.py
extensions = [
    'sphinx.ext.todo',
    # 其他扩展...
]
```
2. 配置选项

默认情况下，TODO 条目不会出现在最终生成的文档中。你需要通过配置变量来控制其行为。在 conf.py中添加以下配置项：

    ‌todo_include_todos‌ (bool):
        True: 在输出中包含 .. todo:: 和 .. todolist::指令的内容。
        False (默认): 不生成任何 TODO 相关输出。

    python
    todo_include_todos = True

    ‌todo_emit_warnings‌ (bool, 版本 1.5+):
        True: 为每个 TODO 条目发出警告信息。这有助于在构建日志中发现未完成的项。
        False (默认): 不发出警告。

    ‌todo_link_only‌ (bool, 版本 1.4+):
        True: .. todolist:: 生成的列表仅包含链接，不包含文件路径和行号。
        False (默认): 显示完整的路径和行号信息。

3. 使用指令

启用扩展后，你可以使用以下两个主要指令：
.. todo::

用于标记具体的待办事项。用法类似于 .. note:: 或 .. warning::。

rst
.. todo::

   这里填写需要完成的任务描述。
   例如：优化数据库查询性能。

‌自定义样式 (版本 1.3.2+):‌
你可以使用 class 选项来改变 HTML 输出中的 CSS 类，从而改变外观（取决于主题支持）。默认类名为 admonition-todo。

rst
.. todo::
   :class: warning

   这是一个紧急的待办事项。

注意：不同的 Sphinx 主题对 class 的支持不同。例如在 sphinx_rtd_theme 或 sphinx_book_theme 中，常用的 class 值可能包括 warning, danger, note, tip, seealso 等，具体表现颜色需参考所用主题的文档。
.. todolist::

用于在所有文档中收集并列出所有的 .. todo:: 条目。通常放在一个专门的页面（如 todos.rst）或章节末尾。

rst
待办事项列表
============

.. todolist::

如果 todo_include_todos 设置为 True，该指令将被替换为整个项目中所有 TODO 条目的列表，每个条目通常包含指向其定义位置的链接。
4. 命令行覆盖配置

你可以在构建文档时通过命令行参数临时覆盖 conf.py 中的设置，而无需修改配置文件：

    ‌显示 TODO:‌

    bash
    sphinx-build -b html -D todo_include_todos=1 source build/html

    ‌隐藏 TODO:‌

    bash
    sphinx-build -b html -D todo_include_todos=0 source build/html

5. 高级用法：自定义事件 (可选)

从版本 1.5 开始，sphinx.ext.todo 提供了 todo-defined(app, node) 事件。当定义一个 TODO 节点时会触发此事件。你可以利用它在扩展中进行更复杂的处理，例如自动收集统计信息等。

python
# 在 conf.py 或其他扩展中
def on_todo_defined(app, node):
    # 处理逻辑，例如打印日志或收集数据
    print(f"Found a todo: {node.astext()}")

def setup(app):
    app.connect('todo-defined', on_todo_defined)

总结

    在 conf.py 中添加 'sphinx.ext.todo' 到 extensions。
    设置 todo_include_todos = True 以在输出中显示 TODO。
    在 .rst 文件中使用 .. todo:: 编写待办事项。
    使用 .. todolist:: 在一个集中位置展示所有待办事项。

这样，你就可以有效地在 Sphinx 文档中管理和跟踪开发任务了。


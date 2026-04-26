# 待办事项列表

## 总结

1. 在 conf.py 中添加 'sphinx.ext.todo' 到 extensions。
2. 设置 todo_include_todos = True 以在输出中显示 TODO。
3. 在 .rst 文件中使用 .. todo:: 编写待办事项。
4. 使用 .. todolist:: 在一个集中位置展示所有待办事项。

### 显示 TODO:‌

```bash
    sphinx-build -b html -D todo_include_todos=1 source build/html
```
#### 隐藏 TODO:‌

```bash
    sphinx-build -b html -D todo_include_todos=0 source build/html



```{eval-rst}
.. todolist::
```

[tmp-test](tmp-test)

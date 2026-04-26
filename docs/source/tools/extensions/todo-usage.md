# sphinx，todo插件的使用方法

## 安装

1. 启用扩展

首先，需要在项目的配置文件 ​​conf.py​​ 中启用该扩展。将 ​​'sphinx.ext.todo'​​ 添加到 ​​extensions​​列表中：

    # conf.py
    extensions = [
        'sphinx.ext.todo',
        # 其他扩展...
    ]

2. 配置选项

默认情况下，TODO 条目不会出现在最终生成的文档中。你需要通过配置变量来控制其行为。在 ​​conf.py​​中添加以下配置项：
‌​- todo_include_todos​‌ (bool):
  - True​​: 在输出中包含 ​​.. todo::​​ 和 ​​.. todolist::​​指令的内容。
  - ​​False​​ (默认): 不生成任何 TODO 相关输出。

  


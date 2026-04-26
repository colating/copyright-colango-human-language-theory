# 需要安装哪些 sphinx 插件                  

sphinx 插件，怎样使用

            
                
                
                
                
                
                
            
            
            
            
        
                            

        
        
        
        
        
        
        
    
                        

                
                
                    
            
                
                
                    
                        
                        
                            
                        
                        
                    
                
            
        
                    
                
            
            

                
                
            
            
1. 1.
                Tutorial: Writing a simple extension — Sphinx 1.3.5 documentation-sphinx-doc-zh.readthedocs.io
2. 2.
                Developing a “TODO” extension — Sphinx 1.8.5 文档-sphinx-doc.readthedocs.io
3. 3.
                sphinx.ext.todo – Support for todo items - Sphinx documentation-sphinx-themed.readthedocs.io
4. 4.
                sphinx.ext.todo – Support for todo items - Sphinx documentation-sphinx-themed.readthedocs.io
5. 5.
                sphinx.ext.todo -- 支持todo项-Sphinx文档官网
                官网
            
6. 6.
                sphinx.ext.todo-开源地理空间基金会中文分会
7. 7.
                Sphinx-快速入门-开源地理空间基金会中文分会
8. 8.
                扩展构建过程-开源地理空间基金会中文分会
9. 9.
                Sphinx重要扩展介绍-开源地理空间基金会中文分会
10. 10.
                手把手教你用 Sphinx 生成专业技术文档-CSDN博客
11. 11.
                入门-开源地理空间基金会中文分会
12. 12.
                Sphinx-开源地理空间基金会中文分会
13. 13.
                sphinx.ext.autodoc --包括文档字符串中的文档-开源地理空间基金会中文分会
14. 14.
                下拉框插件 sphinx-togglebutton-开源地理空间基金会中文分会
15. 15.
                Sphinx文档生成器终极指南:如何快速创建专业技术文档-CSDN博客
16. 16.
                解锁Sphinx:技术文档生成神器的全面指南-CSDN博客
17. 17.
                5.4. 可选的 MyST 扩展语法 — Sphinx文档管理-开源地理空间基金会中文分会
18. 18.
                Sphinx文档管理与构建-开源地理空间基金会中文分会
19. 19.
                在软件开发项目中,Doxygen和Sphinx是两种常用的文档生成工具。请详细阐述如何将Doxyge-word.baidu.com
20. 20.
                MLLM for Robotics Manipulation-冠long馨
21. 21.
                Svelte 5:Todo List 应用1-smart
22. 22.
                Python 中特别的注释标记-A2ZXXXX
23. 23.
                AI辅助编程:Sphinx文档工程自动化发布脚本 | 技术传播-睿齐
24. 24.
                告别杂乱 README:用 Sphinx 打造专业级项目文档-myRan
25. 25.
                使用Sphinx 高效生成项目文档:从入门到实战-CSDN博客
26. 26.
                配置-开源地理空间基金会中文分会
27. 27.
                如何将自动模块添加到Sphinx Toctree-CSDN博客
在 Sphinx 中使用 ​​sphinx.ext.todo​​ 扩展可以帮助你在文档中添加待办事项（TODO）条目，并可以选择性地显示或隐藏它们。以下是详细的使用指南：
1. 启用扩展
首先，需要在项目的配置文件 ​​conf.py​​ 中启用该扩展。将 ​​'sphinx.ext.todo'​​ 添加到 ​​extensions​​列表中：
# conf.py
extensions = [
    'sphinx.ext.todo',
    # 其他扩展...
]2. 配置选项
默认情况下，TODO 条目不会出现在最终生成的文档中。你需要通过配置变量来控制其行为。在 ​​conf.py​​中添加以下配置项：
• ‌​todo_include_todos​‌ (bool):
• ​​True​​: 在输出中包含 ​​.. todo::​​ 和 ​​.. todolist::​​指令的内容。
• ​​False​​ (默认): 不生成任何 TODO 相关输出。
todo_include_todos = True• ‌​todo_emit_warnings​‌ (bool, 版本 1.5+):
• ​​True​​: 为每个 TODO 条目发出警告信息。这有助于在构建日志中发现未完成的项。
• ​​False​​ (默认): 不发出警告。
• ‌​todo_link_only​‌ (bool, 版本 1.4+):
• ​​True​​: ​​.. todolist::​​ 生成的列表仅包含链接，不包含文件路径和行号。
• ​​False​​ (默认): 显示完整的路径和行号信息。
3. 使用指令
启用扩展后，你可以使用以下两个主要指令：
​​.. todo::​​
用于标记具体的待办事项。用法类似于 ​​.. note::​​​ 或 ​​.. warning::​​。
.. todo::

   这里填写需要完成的任务描述。
   例如：优化数据库查询性能。‌自定义样式 (版本 1.3.2+):‌

你可以使用 ​​​class​​​ 选项来改变 HTML 输出中的 CSS 类，从而改变外观（取决于主题支持）。默认类名为 ​​admonition-todo​​。.. todo::
   :class: warning

   这是一个紧急的待办事项。注意：不同的 Sphinx 主题对 class 的支持不同。例如在 ​​sphinx_rtd_theme​​​ 或 ​​sphinx_book_theme​​ 中，常用的 class 值可能包括 ​​​warning​​​, ​​​danger​​​, ​​​note​​​, ​​​tip​​​, ​​​seealso​​​ 等，具体表现颜色需参考所用主题的文档。
​​.. todolist::​​
用于在所有文档中收集并列出所有的 ​​.. todo::​​​ 条目。通常放在一个专门的页面（如 ​​todos.rst​​）或章节末尾。
待办事项列表
============

.. todolist::如果 ​​todo_include_todos​​​ 设置为 ​​True​​，该指令将被替换为整个项目中所有 TODO 条目的列表，每个条目通常包含指向其定义位置的链接。
4. 命令行覆盖配置
你可以在构建文档时通过命令行参数临时覆盖 ​​conf.py​​ 中的设置，而无需修改配置文件：
• ‌显示 TODO:‌
sphinx-build -b html -D todo_include_todos=1 source build/html• ‌隐藏 TODO:‌
sphinx-build -b html -D todo_include_todos=0 source build/html5. 高级用法：自定义事件 (可选)
从版本 1.5 开始，​​sphinx.ext.todo​​​ 提供了 ​​todo-defined(app, node)​​ 事件。当定义一个 TODO 节点时会触发此事件。你可以利用它在扩展中进行更复杂的处理，例如自动收集统计信息等。
# 在 conf.py 或其他扩展中
def on_todo_defined(app, node):
    # 处理逻辑，例如打印日志或收集数据
    print(f"Found a todo: {node.astext()}")

def setup(app):
    app.connect('todo-defined', on_todo_defined)总结
1. 在 ​​conf.py​​​ 中添加 ​​'sphinx.ext.todo'​​​ 到 ​​extensions​​。
2. 设置 ​​todo_include_todos = True​​ 以在输出中显示 TODO。
3. 在 ​​.rst​​​ 文件中使用 ​​.. todo::​​ 编写待办事项。
4. 使用 ​​.. todolist::​​ 在一个集中位置展示所有待办事项。
这样，你就可以有效地在 Sphinx 文档中管理和跟踪开发任务了。
                    
        

        
        
        
        
    
                    

            
                
                
                
                
                
                
            
            
            
            
        
        

        
    
                    
                        
                        
                        
                        
                        
                        
如何在Sphinx中集成TODO管理

            
                
                
                
                
                
                
            
            
            
            
        
                            

        
        
        
        
        
        
        
    
                        

                
                
                    
            
                
                
                    
                        
                        
                            
                        
                        
                    
                
            
        
                    
                
            
            

                
                
            
            
1. 1.
                Developing a “TODO” extension — Sphinx 1.8.5 文档-sphinx-doc.readthedocs.io
2. 2.
                Tutorial: Writing a simple extension — Sphinx 1.3.1 documentation-sphinx-doc-zh.readthedocs.io
3. 3.
                Extending the build process — Sphinx documentation-sphinx-test-en.readthedocs.io
4. 4.
                sphinx.ext.todo -- 支持todo项-Sphinx文档官网
5. 5.
                sphinx.ext.todo-开源地理空间基金会中文分会
6. 6.
                扩展构建过程-开源地理空间基金会中文分会
7. 7.
                延拓-开源地理空间基金会中文分会
8. 8.
                对构建过程进行扩展-Sphinx文档官网
9. 9.
                Sphinx文档管理与构建-开源地理空间基金会中文分会
10. 10.
                如何将自动模块添加到Sphinx Toctree-CSDN博客
11. 11.
                手把手教你用 Sphinx 生成专业技术文档-CSDN博客
12. 12.
                Sphinx-快速入门-开源地理空间基金会中文分会
13. 13.
                sphinx自动化生成tutourial-CSDN博客
14. 14.
                sphinx.ext.doctest --文档中的测试代码段-开源地理空间基金会中文分会
15. 15.
                Sphinx文档生成器终极指南:如何快速创建专业技术文档-CSDN博客
16. 16.
                Sphinx开发者指南-开源地理空间基金会中文分会
17. 17.
                Sphinx重要扩展介绍-开源地理空间基金会中文分会
18. 18.
                使用Sphinx 高效生成项目文档:从入门到实战-CSDN博客
19. 19.
                Svelte 5:Todo List 应用1-smart
20. 20.
                MLLM for Robotics Manipulation-冠long馨
21. 21.
                Dify知识库-杨京京
22. 22.
                开发日志#250 主线剧情继续-orochi2k
23. 23.
                前端,后端,app 开发流程理解-王几行XING
24. 24.
                一个软件有几千万甚至上亿字节,程序员是怎么记住的?-小焱
25. 25.
                开发autodoc扩展-开源地理空间基金会中文分会
26. 26.
                Sphinx中功能的扩展开发-开源地理空间基金会中文分会
27. 27.
                Sphinx-开源地理空间基金会中文分会
28. 28.
                扩展Sphinx-开源地理空间基金会中文分会
29. 29.
                5.4. 可选的 MyST 扩展语法 — Sphinx文档管理-开源地理空间基金会中文分会
30. 30.
                4. Sphixn进阶及常用扩展模块-开源地理空间基金会中文分会
在 Sphinx 中集成 TODO 管理主要依赖于内置扩展 ​​sphinx.ext.todo​​。该扩展允许你在文档中插入待办事项，并可以选择性地将其显示在最终输出的文档中，或者集中生成一个待办事项列表。
以下是具体的集成步骤和使用方法：
1. 启用扩展
首先，你需要在项目的配置文件 ​​conf.py​​​ 中启用 ​​sphinx.ext.todo​​​ 扩展。找到 ​​extensions​​​ 列表，并将 ​​'sphinx.ext.todo'​​ 添加进去。
# conf.py
extensions = [
    'sphinx.ext.todo',
    # 其他扩展...
]2. 配置行为
默认情况下，Sphinx 不会在生成的文档（如 HTML 或 PDF）中显示 TODO 条目。你需要通过配置变量来控制这一行为。在 ​​conf.py​​ 中添加以下配置：
• ‌​​todo_include_todos​​‌:

• 设置为 ​​True​​​：在输出中包含 ​​.. todo::​​​ 和 ​​.. todolist::​​ 的内容。
• 设置为 ​​False​​（默认）：不生成任何 TODO 相关输出，但构建过程仍会解析它们。
# conf.py
todo_include_todos = True• ‌​​todo_emit_warnings​​‌ (可选):

• 设置为 ​​True​​：为每个 TODO 条目发出警告。这有助于在构建日志中快速发现未完成的项。
todo_emit_warnings = True• ‌​​todo_link_only​​‌ (可选):

• 设置为 ​​True​​​：​​.. todolist::​​ 生成的列表仅包含链接，不显示文件路径和行号，使列表更简洁。
todo_link_only = False3. 使用指令
启用并配置后，你可以在 ​​.rst​​ 文件中使用以下两个主要指令：
​​.. todo::​​
用于标记具体的待办事项。它的用法类似于 ​​.. note::​​​ 或 ​​.. warning::​​。
.. todo::

   这里填写需要完成的任务描述。
   例如：优化数据库查询性能，减少响应时间。‌自定义样式 (Sphinx 1.3.2+)‌:

你可以使用 ​​​:class:​​ 选项来改变 HTML 输出中的 CSS 类，从而改变外观（具体效果取决于你使用的主题）。.. todo::
   :class: warning

   这是一个紧急的待办事项，需要优先处理。常见的 class 值包括 ​​note​​​, ​​warning​​​, ​​danger​​​, ​​tip​​​, ​​seealso​​ 等，不同主题对这些类的颜色定义可能不同。
​​.. todolist::​​
用于在所有文档中收集并列出所有的 ​​.. todo::​​​ 条目。通常放在一个专门的页面（如 ​​todos.rst​​）或章节末尾，以便集中查看整个项目的待办事项。
待办事项汇总
============

以下是项目中所有标记为 TODO 的事项：

.. todolist::如果 ​​todo_include_todos​​​ 为 ​​True​​，该指令将被替换为整个项目中所有 TODO 条目的列表，每个条目通常包含指向其定义位置的链接。
4. 命令行覆盖配置
你可以在构建文档时通过命令行参数临时覆盖 ​​conf.py​​ 中的设置，而无需修改配置文件。这在 CI/CD 流程中非常有用，例如只在开发构建中显示 TODO，而在发布构建中隐藏。
• ‌显示 TODO:‌
sphinx-build -b html -D todo_include_todos=1 source build/html• ‌隐藏 TODO:‌
sphinx-build -b html -D todo_include_todos=0 source build/html5. 高级用法：事件挂钩 (可选)
从 Sphinx 1.5 开始，​​sphinx.ext.todo​​​ 提供了 ​​todo-defined​​ 事件。当定义一个 TODO 节点时会触发此事件。你可以利用它在扩展中进行更复杂的处理，例如自动收集统计信息或执行自定义逻辑。
# 在 conf.py 或其他扩展中
def on_todo_defined(app, node):
    # 处理逻辑，例如打印日志或收集数据
    print(f"Found a todo: {node.astext()}")

def setup(app):
    app.connect('todo-defined', on_todo_defined)总结
1. 在 ​​conf.py​​​ 的 ​​extensions​​​ 列表中添加 ​​'sphinx.ext.todo'​​。
2. 设置 ​​todo_include_todos = True​​ 以在输出中显示 TODO。
3. 在 ​​.rst​​​ 文件中使用 ​​.. todo::​​ 编写待办事项。
4. 使用 ​​.. todolist::​​ 在一个集中位置展示所有待办事项。
5. 利用命令行参数 ​​-D todo_include_todos=0/1​​ 灵活控制构建输出。
通过以上步骤，你就可以有效地在 Sphinx 文档中管理和跟踪开发任务了。
                    
        

        
        
        
        
    
                    

            
                
                
                
                
                
                
            
            
            
            
        
        

        
    
                    
                        
                        
                        
                        
                        
                        
sphinx 使用 todo有什么好处和缺点？

            
                
                
                
                
                
                
            
            
            
            
        
                            

        
        
        
        
        
        
        
    
                        

                
                
                    
            
                
                
                    
                        
                        
                        
                    
                
            
        
                    
                
            
            

                
                
            
            
1. 1.
                Sphinx:技术文档的终极利器-CSDN博客
2. 2.
                sphinx.ext.todo-开源地理空间基金会中文分会
3. 3.
                Python项目文档生成常用工具对比-CSDN博客
4. 4.
                Sphinx文档生成器扩展推荐:提升文档功能的15个精选插件-CSDN博客
5. 5.
                延拓-开源地理空间基金会中文分会
6. 6.
                Sphinx重要扩展介绍-开源地理空间基金会中文分会
7. 7.
                Sphinx文档生成器扩展性能基准:与其他插件的对比-CSDN博客
8. 8.
                Sphinx-开源地理空间基金会中文分会
9. 9.
                Sphinx 的介绍和原理探索-搜狐
10. 10.
                用sphinx-doc优雅的写文档-CSDN博客
11. 11.
                入门-开源地理空间基金会中文分会
12. 12.
                使用Sphinx 高效生成项目文档:从入门到实战-CSDN博客
13. 13.
                关于sphinx的一点了解-CSDN博客
14. 14.
                Python中文档生成利器Sphinx的入门指南-脚本之家
15. 15.
                Sphinx-百度百科
16. 16.
                指令-开源地理空间基金会中文分会
17. 17.
                代码注释中经常用到的 TODO、XXX、FIXME 有什么区别?-冯柒柒
18. 18.
                SPHINX: 权重、任务视觉嵌入的多模态大融合-weixin
19. 19.
                sox有什么好的!-哔哩哔哩
20. 20.
                号称取代Elasticsearch的轻量级搜索引擎-javaTodo
‌Sphinx 使用 ​​sphinx.ext.todo​​​ 扩展的主要好处是能有效管理文档中的待办事项，提升协作效率‌，而缺点则集中在配置复杂性和对构建流程的潜在干扰。
✅ 主要好处
1. ‌任务可视化与追踪‌

通过 ​​.. todo::​​ 指令，可以将未完成的内容、需要补充的说明或技术债清晰地标记在文档中，使团队成员一目了然地看到当前缺失的部分。2. ‌集中管理待办项‌

使用 ​​.. todolist::​​ 指令可自动生成一个包含项目中所有 TODO 的汇总列表，便于项目经理或文档负责人统一查看和分配任务。3. ‌灵活控制显示逻辑‌

可通过 ​​todo_include_todos=True/False​​ 配置项或命令行参数 ​​-D todo_include_todos=1​​ 动态决定是否在输出文档中显示 TODO 内容，适用于开发版与发布版文档的差异化构建。4. ‌支持样式定制与警告提示‌
• 自定义 ​​class​​​ 属性（如 ​​warning​​​、​​danger​​）可让重要事项更醒目。
• 启用 ​​todo_emit_warnings=True​​ 后，构建时会发出警告，帮助开发者在 CI/CD 流程中及时发现未处理的 TODO。
5. ‌与 Python 生态深度集成‌

作为 Sphinx 官方内置扩展之一，​​sphinx.ext.todo​​ 无需额外安装，兼容性强，且可与其他扩展（如 ​​autodoc​​、​​intersphinx​​）无缝协作。❌ 主要缺点
1. ‌默认不显示，需手动配置‌

​​todo_include_todos​​ 默认为 ​​False​​，若忘记启用，则所有标记的 TODO 都不会出现在输出中，容易造成“写了却看不见”的困惑。2. ‌增加构建复杂性‌

对于初学者而言，修改 ​​conf.py​​ 并理解扩展机制有一定学习成本。同时，多个扩展共存时可能引发冲突或性能问题。3. ‌依赖主题支持样式渲染‌

​​class​​ 的视觉效果取决于所用 Sphinx 主题（如 ​​sphinx_rtd_theme​​ 或 ​​sphinx_book_theme​​），若主题未定义相关 CSS 类，则自定义样式无效。4. ‌可能影响文档专业性‌

若在正式发布的文档中未关闭 TODO 显示，可能会让用户误以为文档不完整或项目不成熟。5. ‌性能轻微损耗‌

虽然 ​​sphinx.ext.todo​​ 本身轻量，但在超大项目中解析大量 ​​todo​​ 节点仍会带来微小的构建延迟，尤其在启用事件钩子时。要不要我为你整理一份‌Sphinx 中禁用 TODO 的最佳实践方案‌，帮你避免在正式发布时泄露未完成内容？
                    
        

        
        
        
        
    
                    

            
                
                
                
                
                
                
            
            
            
            
        
        

        
    
                    
                        
                        
                        
                        
                        
                        
如何自定义Sphinx的TODO样式

            
                
                
                
                
                
                
            
            
            
            
        
                            

        
        
        
        
        
        
        
    
                        

                
                
                    
            
                
                
                    
                        
                        
                            
                        
                        
                    
                
            
        
                    
                
            
            

                
                
            
            
1. 1.
                Developing a “TODO” extension — Sphinx 1.8.5 文档-sphinx-doc.readthedocs.io
2. 2.
                Tutorial: Writing a simple extension — Sphinx 1.3.5 documentation-sphinx-doc-zh.readthedocs.io
3. 3.
                Extending the build process — Sphinx documentation-sphinx-test-en.readthedocs.io
4. 4.
                sphinx.ext.todo – Support for todo items - Sphinx documentation-sphinx-themed.readthedocs.io
5. 5.
                sphinx.ext.todo -- 支持todo项-Sphinx文档官网
6. 6.
                sphinx.ext.todo-开源地理空间基金会中文分会
7. 7.
                扩展构建过程-开源地理空间基金会中文分会
8. 8.
                配置-开源地理空间基金会中文分会
9. 9.
                指令-开源地理空间基金会中文分会
10. 10.
                Sphinx-快速入门-开源地理空间基金会中文分会
11. 11.
                sphinx入门指南【2】 toctree指令详解-腾讯云
12. 12.
                修改Sphinx TOC树-CSDN博客
13. 13.
                自定义sphinxdoc主题-腾讯云开发者社区-腾讯云-腾讯云
14. 14.
                手把手教你用 Sphinx 生成专业技术文档-CSDN博客
15. 15.
                模板法-开源地理空间基金会中文分会
16. 16.
                Sphinx-开源地理空间基金会中文分会
17. 17.
                5.4. 可选的 MyST 扩展语法 — Sphinx文档管理-开源地理空间基金会中文分会
18. 18.
                1.5. 文档制作工具Sphinx简介-开源地理空间基金会中文分会
19. 19.
                Substance Designer [Tips] 如何设置自定义模板-哔哩哔哩
20. 20.
                Svelte 5:Todo List 应用1-smart
21. 21.
                Python 中特别的注释标记-A2ZXXXX
22. 22.
                Obsidian使用,创建一个简易模版-Buffaloxi14
23. 23.
                怎么看待“埃德加·凯西”的能力?-理极天启
24. 24.
                告别杂乱 README:用 Sphinx 打造专业级项目文档-myRan
25. 25.
                5.1. Sphinx文档项目配置-开源地理空间基金会中文分会
在 Sphinx 中自定义 ​​sphinx.ext.todo​​​ 的样式，主要通过修改 ​​.. todo::​​​ 指令的 ​​class​​ 选项来实现。这允许你利用现有主题的 CSS 类来改变待办事项的外观（如颜色、图标等），而无需编写额外的 CSS 代码。
1. 使用 ​​class​​ 选项
从 Sphinx 1.3.2 版本开始，​​.. todo::​​​ 指令支持 ​​:class:​​ 选项。你可以将其设置为任何受当前主题支持的 admonition（提示框）类名。
‌基本语法：‌
.. todo::
   :class: warning

   这是一个紧急的待办事项，显示为警告样式。如果不指定 ​​:class:​​​，默认使用的类名是 ​​admonition-todo​​。
2. 常用类名与视觉效果
不同的 Sphinx 主题对类的支持略有不同，但大多数主流主题（如 ​​sphinx_rtd_theme​​​, ​​sphinx_book_theme​​​, ​​furo​​ 等）都支持标准的 admonition 类。以下是常见的类名及其通常对应的视觉风格：
• ‌​​warning​​​‌ / ‌​​danger​​‌: 通常显示为红色或橙色背景，表示严重或紧急事项。
• ‌​​note​​‌: 通常显示为蓝色背景，表示普通注释。
• ‌​​tip​​​‌ / ‌​​hint​​‌: 通常显示为绿色或黄色背景，表示建议或提示。
• ‌​​seealso​​‌: 通常显示为绿色背景，表示参考信息。
• ‌​​attention​​​‌ / ‌​​caution​​‌: 通常显示为橙色或黄色背景，表示需要注意的事项。
‌示例对比：‌
.. todo::
   :class: danger

   【高危】数据库迁移脚本尚未测试，请勿在生产环境执行。

.. todo::
   :class: tip

   【建议】后续版本可以考虑添加缓存机制以提升性能。

.. todo::
   :class: note

   【常规】需要补充 API 接口的错误码说明文档。3. 完全自定义 CSS（高级）
如果内置的类名无法满足需求，或者你想为 ​​admonition-todo​​ 定义独特的样式，可以通过添加自定义 CSS 文件来实现。
‌步骤：‌
1. 在 ​​_static​​​ 目录下创建一个 CSS 文件（例如 ​​custom_todo.css​​）。
2. 编写 CSS 规则针对 ​​.admonition-todo​​ 或你自定义的类。
/* _static/custom_todo.css */
.admonition-todo {
    background-color: #e7f3fe;
    border-left: 5px solid #2196F3;
}

.admonition-todo .admonition-title {
    background-color: #d1e7ff;
    color: #0c5460;
}

/* 自定义类示例 */
.admonition-urgent-todo {
    background-color: #ffebee;
    border-left: 5px solid #f44336;
}3. 在 ​​conf.py​​ 中注册该 CSS 文件：
# conf.py
html_css_files = [
    'custom_todo.css',
]4. 在 RST 中使用自定义类：
.. todo::
   :class: urgent-todo

   这个待办事项将使用我们自定义的红色边框样式。4. 注意事项
• ‌主题兼容性‌：并非所有主题都完美支持所有 admonition 类。在使用前，最好查阅你所用主题的文档，或在本地构建后检查实际效果。
• ‌​​todo_include_todos​​​ 配置‌：确保在 ​​conf.py​​​ 中设置了 ​​todo_include_todos = True​​，否则无论样式如何设置，TODO 内容都不会出现在最终文档中。
• ‌HTML 输出‌：​​class​​ 选项主要影响 HTML 输出。对于 LaTeX/PDF 输出，Sphinx 可能会忽略自定义类或使用默认的 admonition 样式，具体取决于 LaTeX 模板的配置。
通过结合 ​​:class:​​ 选项和自定义 CSS，你可以灵活地控制 Sphinx 文档中 TODO 项的视觉呈现，使其更符合项目规范或提高可读性。

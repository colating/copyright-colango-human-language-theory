# 需要安装哪些 sphinx 插件                  

- conf.py

pip install myst-parser   
extensions = ["myst_parser"]


pip install sphinxcontrib-mermaid  
extensions = ['sphinxcontrib.mermaid']

```{mermaid}
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```



            
                
                

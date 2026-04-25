###### sphinx build


#### 分支名称、action工作流文件的缩写

- t == cltg
- s == start
------
- tdev == cltgdev
- tstart == cltgstart
- tscross == cltgtartcross
- tsopen == tsopenopen
- thtml == cltghtml

# A. Colating 私有仓库

## 1. IN copyleft-colating-general-human-language-docs-dev

#### 从 colating docs-dev 发出

- tdev
- tstart
- cltgstart_cltgstartcross.yml
- cltgstart_cltgstartopen.yml

## 2. IN copyleft-colating-general-human-language

- tscross  # For RTD
- cltgstartcross_deleteacionfile.yml  # For RTD not need action file. rm .github/workflows/* << In this yml file

## 3. IN colating.github.io

- tsopen
- thtml
- cltgstartopen_cltghtml.yml  # rm .github/workflows/* << In this yml file

# B. Colango 私有仓库

## 1. IN copyright-colango-docs-dev

- gdev
- gstart
- clgostart_clgostartcross.yml
- clgostart_clgostartopen.yml

## 2. IN copyright-colango-general-human-language

- gscross

#### =======================



## 测试 OK
# 但有警告; github官方 js版本警告
# AI 说这个代码有安全漏洞
 
#### 使用说明：
- 1. 私有仓库 source cltg_docs_dev 的 dev分支，不对外开放：只 作为开发用途。
- 2. 当需要发布时，将私有仓库的 dev分支，@人工手动@ ：push 到该仓库的 main分支。
- 3. Action A type 工作流文件运行在 source cltg_docs_dev私有仓库环境：
- 当私有仓库 source cltg_docs_dev 的 main分支有 push 信号时，
- 将本地 main分支的全部文件，push 到远程公有仓库  copyleft-colating-general-human-language 
- 的 mirror_from-cltg_docs_dev-main 分支。
- 4. 当公有仓库的mirror_from-cltg_docs_dev-main 分支有 push 信号时，产生 Webhooks 信号给 RTD。
- 5. 公有仓库  copyleft-colating-general-human-language 的main分支，可以保留作为自由发挥。

- 待解决：目前  colating.github.io 仓库的 action 工作流，不能删除，后续需要删除掉它。。。。
- git 删除文件，都会保留记录；删除方法与操作系统方法不一样。

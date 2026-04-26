# readthedocs 关闭版本显示

自定义主题（高级）

若你使用自定义 Sphinx 主题，可通过 CSS 隐藏版本选择器：

在 docs/source/_static/custom.css 中添加：

```css
.rst-versions {
    display: none !important;
}
```
并在 conf.py 中引入该 CSS：

```python
html_static_path = ['_static']
html_css_files = ['custom.css']
```
    此方法仅影响前端显示，版本仍存在于后台‌。

### 补充说明

- 隐藏 ≠ 删除‌：隐藏版本后，文档仍可通过直接 URL 访问，且不会触发构建；若需彻底移除，需点击 ‌“Delete”‌（不可逆）‌。
- ‌商业版支持更多控制‌：Read the Docs for Business 提供更细粒度的权限与版本控制，可参考 Pricing 页面。

如需进一步自动化管理版本，可使用 .readthedocs.yaml 配置文件定义构建规则 

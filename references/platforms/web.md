# Platform Specification: Modern Web Applications & Websites

参考标准：W3C WCAG 2.2 AA、Google Core Web Vitals、现代 HTML5 / CSS 能力与浏览器原生交互惯例。

---

## 1. 网站（Content/Marketing）vs Web 应用（App/SaaS）区分

不要把后台应用做成营销落地页，也不要把品牌网站做成干瘪表单：
- **Web 应用 / SaaS / 工作台**：紧凑顶栏或左侧 Sidebar，首屏直达真实数据与高频操作；重效率、快捷键、批量处理、筛选排序与 URL 状态同步。
- **官网 / 作品集 / 内容站**：重叙事节奏、视觉识别、清晰阅读行宽（`60–68ch`）、极速首屏 LCP 与明确转化路径。

---

## 2. 浏览器原生能力与用户心智（必守）

1. **URL 即状态（Deep-Linkable State）**：筛选条件、排序、当前 Tab、分页、搜索关键词与详情路由尽量同步到 URL Path / Query Params，保证刷新不丢态、转发链接即所见、浏览器前进/后退完全符合预期。
2. **原生链接与按钮语义**：
   - 支持中键/Cmd+Click 新标签页打开的页面跳转必须使用真实 `<a href="...">`，绝不用 `<div onClick={router.push}>`。
   - 表单提交用 `<form onSubmit>` + `<button type="submit">`，天然支持回车提交。
3. **键鼠与触控双模平等**：
   - Hover 效果用 `@media (hover: hover) and (pointer: fine)` 包裹，防止移动端点击后粘滞 Hover 态。
   - 完整支持 `Tab` / `Shift+Tab` / `Enter` / `Space` / `Esc`；专业 Web App 提供 `Cmd/Ctrl + K` 命令面板与清晰快捷键提示（`<kbd>`）。
4. **现代 CSS 工程利器**：
   - 使用 **Container Queries（`@container`）** 让卡片和侧栏组件按自身容器尺寸自适应，而非全靠全局媒体查询。
   - 优先使用 `100dvh` 替代 `100vh` 解决移动端浏览器地址栏遮挡。
   - 合理利用 CSS 原生 `scroll-margin-top`（防锚点/焦点被吸顶头挡住）、`overscroll-behavior: contain`（防弹窗内滚穿底层页面）、`View Transitions API`（渐进增强路由平滑切换）。
   - 使用语义 CSS Variables（支持 OKLCH / sRGB 回退）管理亮暗主题与 Design Tokens。

---

## 3. Web 专属常见雷区拦截

- **移动端输入框自动放大**：iOS Safari 对 `font-size < 16px` 的 `<input>` 聚焦时会自动放大页面 → 移动端表单输入框正文保持 **≥ 16px**。
- **自定义滚动条与水平溢出**：上线前在 `390px` 和 `1440px` 检查 `document.documentElement.scrollWidth <= window.innerWidth`，消灭 1px 横向滚动条。
- **弹窗焦点与背景滚动锁**：打开 Modal / Drawer 时锁定背景滚动（注意补偿滚动条宽度防页面横跳）、锁住键盘焦点，关闭后焦点回到触发按钮。
- **SEO 与加载稳定性（内容类网站）**：正确标题层级（每页 1 个 `<h1>`）、语义标签、预声明图片尺寸与 `aspect-ratio`（CLS ≤ 0.1）、合理懒加载与 LCP 预加载。

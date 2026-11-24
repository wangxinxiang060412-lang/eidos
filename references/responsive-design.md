# Responsive & Adaptive Design

响应式设计不是“把手机界面等比例拉大塞进平板和桌面”，而是**根据可用屏幕空间、输入方式与安全区域，重新组织信息架构与操作效率**。

---

## 1. 窗口尺寸分级与结构重组策略（参考 Apple Size Classes & M3 Window Size Classes）

| 尺寸分级 | 宽度区间 | 导航模式 | 内容结构 | 弹层形态 |
|---|---|---|---|---|
| **Compact-SM（小屏手机）** | `320–374px` | 底部 Tab Bar（≤4–5 项）或精简顶栏 | 单栏流式；复杂数据行纵向折叠，零横向滚动溢出 | 全宽 Bottom Sheet |
| **Compact（标准/大屏手机）** | `375–599px` | 底部 Tab Bar + 顶部紧凑导航 | 单栏主内容；操作区处于拇指自然可达范围 | Bottom Sheet（半屏/全屏可拖拽） |
| **Medium（平板竖屏 / 折叠屏展开）** | `600–839px` | 左侧 Navigation Rail（图标+简标）或紧凑侧栏 | 双列网格或主列表 + 右侧可收起检查器 | 居中 Modal / 侧滑 Drawer |
| **Expanded（平板横屏 / 常规桌面）** | `840–1199px` | 左侧持久化 Sidebar（220–260px） | Master-Detail 双栏（左列表右详情），提升高频切换效率 | 居中 Modal / 锚点 Popover |
| **Large / Ultra-Wide（大屏桌面）** | `≥ 1200px` | Sidebar + 工作区 + 可选右栏 Inspector | 表单与阅读区设 `max-width` 居中；画布/表格/IDE 充分利用多栏 | 锚点 Popover / 居中宽 Modal |

---

## 2. 硬件安全区域与系统侵占（Safe Area 铁律）

任何跨端与移动界面必须动态适配硬件边界，**严禁写死 `padding-top: 44px` 或 `padding-bottom: 34px`**：

1. **顶部安全区**：避让状态栏、刘海屏、灵动岛（Dynamic Island）、挖孔屏与微信小程序右上角胶囊。
   - Web / PWA：`viewport-fit=cover` + `padding-top: env(safe-area-inset-top)`。
   - iOS：使用系统 `.safeAreaInset` / `safeAreaLayoutGuide`，绝不将 Sheet 抓手或导航按钮画到灵动岛下方。
   - Android：启用 Edge-to-Edge 并消费 `WindowInsets.statusBars` / `displayCutout`。
2. **底部手势区**：底部导航栏、固定提交条与 Floating Button 必须叠加上 `env(safe-area-inset-bottom)` / `navigationBars` 内边距，且确保背景延展到底部边缘（不留尴尬白条）。
3. **屏幕大圆角避让**：现代手机四角圆角极大，角落按钮与状态文字必须缩进至安全矩形内，防止被物理屏幕圆角切角。
4. **横屏与分屏 / 多窗口**：
   - 横屏时左右两侧均需遵守安全区（避让摄像头凹槽与手势条），且高度骤减时弹窗与底部工具栏必须可滚动、不把主按钮挤出屏幕外。
   - 桌面/平板支持自由拖拽窗口缩放、Split View 与 Stage Manager，使用 **CSS Container Queries（`@container`）** 让组件按自身容器宽度重组，而不是只盯整屏 `window.innerWidth`。

---

## 3. 软件键盘弹出与多输入模式适配

1. **软键盘避让（Keyboard Avoidance）**：
   - Web 优先使用 `100dvh`（Dynamic Viewport Height）替代 `100vh`，避免移动端地址栏与软键盘遮挡底部提交栏。
   - 聚焦输入框时自动滚动使其处于可视区中上部，底部确认/发送按钮随键盘上移，始终可见可点。
2. **多输入模态自适应（Touch / Mouse / Keyboard / Gamepad）**：
   - **禁止把关键能力藏在 Hover 里！**移动端与触屏没有 Hover，Hover 仅用于桌面端加速提示或次级操作显露；重要按钮在触屏下必须常显或收入显式菜单（Web 用 `@media (hover: hover) and (pointer: fine)` 精准区分）。
   - 支持桌面端快捷键与右键上下文菜单，但不牺牲鼠标单点可发现性。

---

## 4. 极端场景压测清单

- `320px` 极窄手机 + `200%` 系统字体放大：主操作按钮不被截断，文字不横向溢出页面。
- 超长用户名/商品名/金额（如 40 字标题或 `¥99,999,999.99`）：优雅换行或单行省略，不撑破布局。
- 折叠屏外屏（窄长）↔ 内屏（接近正方形 1:1）动态切换：不丢失当前表单输入与滚动位置。

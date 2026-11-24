# Workflow: Production Frontend & Client Implementation

适用场景：将明确的设计规范、交互流程与 Token 落地为可真实运行的高质量前端或客户端代码。

---

## Step 1：Token 与基础原语先行（加载 `design-system.md` + `visual-design.md`）
1. 定义或更新语义化 Token（`bg.*`, `text.*`, `border.*`, `accent.*`, `status.*`, `space.*`, `radius.*`, `shadow.*`, `motion.*`），覆盖亮/暗两套主题映射（若支持）。
2. 建立或对齐核心原语组件（Button、Input、Select/Menu、Dialog/Sheet、Tabs、Toast、Empty/Error/Skeleton），内置：
   - 完整状态机（Default / Hover / Active / Focus-Visible / Disabled / Loading 锁宽）
   - WCAG 2.2 对比度、键盘导航、焦点回归与 ARIA / 原生读屏语义
   - `prefers-reduced-motion` 降级处理

## Step 2：布局骨架与响应式结构（加载 `layout-and-spacing.md` + `responsive-design.md` + 平台文档）
1. 搭建主框架与自适应导航结构（Mobile Bottom Bar / Tablet Rail / Desktop Sidebar），处理 Safe Area、系统栏、小程序胶囊避让与 `100dvh`。
2. 建立精确网格、留白不等式与同心圆角，确保内容动态变化时不发生 CLS 跳动。

## Step 3：真实数据流与完整交互状态（加载 `frontend-engineering.md` + `interaction-states.md`）
1. 接通全部按钮、表单、筛选、排序、分页、搜索、路由参数与持久化/API 逻辑——**零空回调、零假按钮**。
2. 为每个核心功能补齐适用异常状态：空态、骨架屏、错误重试、断网提示、防重复提交、输入校验、未保存拦截与撤销 Toast。
3. 核对全部 UI 文案符合 [ux-writing.md](../references/ux-writing.md)（动词按钮、讲人话报错、零 AI 营销口号）。

## Step 4：因果动效与细节抛光（加载 `motion-design.md` + `typography.md`）
1. 按“Spatial vs Effects”添加克制、可打断、仅动 `transform/opacity` 的生产级动效；核对所有数字开启 `tabular-nums`，图标统一家族与线宽，无近切边与挤压变形。
2. 检查事件监听、定时器与异步请求清理，验证类型检查、Lint 与生产构建全部通过。

## Step 5：进入最终运行验收
完成代码自检后，**绝不直接宣布完工**，必须立即执行 [final-verification.md](./final-verification.md)。

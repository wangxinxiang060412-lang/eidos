# Workflow: Production Frontend & Client Implementation

适用场景：将明确的设计规范、交互流程与 Token 落地为可真实运行的高质量前端或客户端代码。

---

## Step 1：Token 与基础原语先行（加载 `design-system.md` + `visual-design.md`）
1. 定义或更新语义化 Token（`bg.*`, `text.*`, `border.*`, `accent.*`, `status.*`, `space.*`, `radius.*`, `shadow.*`, `motion.*`），覆盖亮/暗两套主题映射（若支持）。
2. 建立或对齐核心原语组件（Button、Input、Select/Menu、Dialog/Sheet、Tabs、Toast、Empty/Error/Skeleton），内置：
   - 完整状态机（Default / Hover / Active / Focus-Visible / Disabled / Loading 锁宽）
   - WCAG 2.2 对比度、键盘导航、焦点回归与 ARIA / 原生读屏语义
   - `prefers-reduced-motion` 降级处理

## Step 2：布局骨架、上下边界与响应式结构（加载 `layout-and-spacing.md` + `navigation-and-boundaries.md` + `responsive-design.md` + 平台文档）
1. 搭建主框架与自适应导航结构（Mobile Bottom Bar / Tablet Rail / Desktop Sidebar），处理 Safe Area、系统栏、小程序胶囊避让、底部防遮挡留白与 `100dvh`。
2. 明确顶栏/内容/底栏边界衔接策略（自然流 / 1px 硬边 / 滚动显现 / 平台材质），建立精确网格、留白不等式与同心圆角，防止 CLS 跳动。

## Step 3：真实数据流、完整状态与文案落盘（加载 `frontend-engineering.md` + `interaction-states.md` + `ux-writing.md`）
1. 接通全部按钮、表单、筛选、排序、分页、搜索、路由参数与持久化/API 逻辑——**零空回调、零假按钮**。
2. 为每个核心功能补齐适用异常状态：空态、骨架屏、诚实错误重试、断网提示、防重复提交、输入校验、未保存拦截与撤销 Toast。
3. 编写或清理全部可见文案（覆盖 19 类落点），保留既有数据绑定、插值变量与本地化 Key，杜绝 14 类 AI 鸡汤话术与无价值副标题。

## Step 4：空间因果动效与 20 项细节精修（加载 `motion-design.md` + `iconography.md` + `visual-refinement.md`）
1. 按 Spatial / Effects 分离原则实现精确 `transform-origin`、可打断、连点安全且仅动合成属性的生产动效；核对数字 `tabular-nums`、单一图标家族与 20 项高影响力视觉精修。
2. 检查事件监听、定时器与异步请求清理，验证类型检查、Lint 与生产构建全部通过。

## Step 5：进入最终运行验收
完成代码自检后，**绝不直接宣布完工**，必须立即执行 [final-verification.md](./final-verification.md)。

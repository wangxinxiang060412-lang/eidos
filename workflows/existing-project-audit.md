# Workflow: Existing Project Audit (Stage 5–6 · Read & Run First)

适用场景：对前端半成品（Stage 5）或完整但体验不佳的产品（Stage 6）做系统性 UI/UX、色彩、文案与功能审查。
**核心铁律：未彻底理解项目前严禁动笔改版；未运行/看图前严禁给高分；保留已合理的设计；配色问题只提案不擅改。**

---

## Step 1：只读理解与架构盘点
1. 判定当前阶段，阅读文档、目录结构、路由表、状态管理、数据接口、主题 Token、i18n 本地化文件与组件库。
2. 明确严禁破坏的资产清单：数据库 Schema、API 契约、持久化 Key、核心业务逻辑、品牌 Slogan 与法务文本。
3. 列出所有页面、弹窗、导航路径、高频业务流与全部固定文案落点。

## Step 2：真实运行与基线取证（Before Baseline）
1. 尽可能启动项目，以真实用户视角走完核心主流程与异常边界（空数据、校验失败、断网/超时、连点、返回、刷新、暗黑模式、`390px` 窄屏与 `1440px` 宽屏）。
2. 保存**修改前基线截图（Before）**与运行 Console 记录，供后续前后效果对比。

## Step 3：13 项系统体检 + 专项深度审计
先列出 **已合理且必须保留的设计资产（Keep List）**，再逐项审计：
1. **色彩系统 11 维审查**（[color-review.md](../references/color-review.md)）：判断应保留现有配色，还是起草 [color-proposal.md](../templates/color-proposal.md) 供用户确认。
2. **功能表达与交互闭环**：检查 6 问即时清晰度、空壳按钮、假反馈、导航死胡同、返回保态与 20 种适用异常态。
3. **全栈 Anti-AI Design & 独立审美侦察**（[anti-ai-ui.md](../references/anti-ai-ui.md) + [aesthetic-reasoning.md](../references/aesthetic-reasoning.md)）：排查胶囊汤、嵌套卡片、重复 KPI 卡、装饰图标盒、统一淡入上浮与 10 类隐性审美失衡。
4. **图标、边界、数据与 20 项精修雷达**：核查 [iconography.md](../references/iconography.md)、[navigation-and-boundaries.md](../references/navigation-and-boundaries.md)、[data-visualization.md](../references/data-visualization.md) 与 [visual-refinement.md](../references/visual-refinement.md)。
5. **空间因果动效与 Content Audit**：核查弹窗/菜单是否闪现或缺少锚点，扫描全项目 19 类可见文案清除 AI 模板话术与术语分裂（[ux-writing.md](../references/ux-writing.md)）。
6. **无障碍、多端适配与性能**：WCAG 2.2 AA、焦点、安全区与帧率/稳定性。

## Step 4：输出加权审查报告与分阶段路线图
1. 按 [audit-report.md](../templates/audit-report.md) 输出 9 维客观评分、保留项清单与 `P0 → P3` 完整 9 字段问题表。
2. 若发现需改整体配色，附上 [color-proposal.md](../templates/color-proposal.md) 请用户确认。
3. 若仅要求审查，在此交付等待确认；若需直接实施优化，转入 [redesign.md](./redesign.md)（未获配色确认前严禁擅改整体色板）。

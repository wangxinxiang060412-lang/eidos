# Workflow: New Product (Stage 1–2 · 0 → 1 Design & Engineering)

适用场景：从初步想法（Stage 1）或已明确需求功能（Stage 2）出发，从零构思、设计并交付可运行的新产品。
**核心铁律：绝不跳过产品逻辑、独立美术推导与 5 行锁定直接堆代码；绝不先填 AI 占位鸡汤文案再后期清理。**

---

## Step 1：产品定义与平台/领域识别（加载 `product-discovery.md` + 对应平台规范）
1. 完成启动五问（目标人群、使用环境、Top 3 核心任务、防呆底线、数据与技术边界）。
2. 识别产品所属平台与领域形态（如 iOS / Web / 小程序 / B 端 SaaS / 数据分析 / 游戏 UI / 智能终端），加载对应 `references/platforms/` 规范。
3. 使用 [design-brief.md](../templates/design-brief.md) 固化产品定位与范围。

## Step 2：功能表达与信息架构（加载 `user-psychology.md` + `information-architecture.md`）
1. 确保每屏通过“功能即时清晰度 6 问”与“逐功能直觉 7 问”，不靠堆砌说明文字解释界面。
2. 将功能分为 L1 / L2 / L3 / T（弹层）/ U（低频设置），规划高频 1–3 步核心路径与返回保态策略。
3. 提前制定本产品的 **Product Voice & Tone** 术语表（参考 [ux-writing.md](../references/ux-writing.md)）。

## Step 3：独立美术方向、配色确认与 Design System（加载 `aesthetic-reasoning.md` + `color-review.md` + `visual-design.md`）
1. 执行 8 维分析，推导贴合本产品气质的 11 支柱独立设计语言（若用户未指定配色且需比选，提供 2–3 套符合 11 要素的配色提案确认；若已授权直接定色，则确保全阶对比度 ≥4.5:1）。
2. 完成 `SKILL.md` 第 5 节的 **5 行锁定**，按 [design-tokens.json](../templates/design-tokens.json) 建立三层语义 Token。
3. 同步规划图标体系（[iconography.md](../references/iconography.md)）、页面上下边界策略（[navigation-and-boundaries.md](../references/navigation-and-boundaries.md)）与数据展示选型（[data-visualization.md](../references/data-visualization.md)，若涉及数据）。

## Step 4：核心交互与 10 要素空间动效规格（加载 `interaction-design.md` + `motion-design.md`）
1. 搭建基础原语组件并内建完整状态机、WCAG 2.2 无障碍与键盘焦点回归。
2. 为关键浮层、日期选择、折叠与转场按 [interaction-spec.md](../templates/interaction-spec.md) 明确 10 要素空间因果与 `transform-origin`。

## Step 5：真实功能工程实现（转入 `frontend-implementation.md`）
1. 端到端打通全部交互、数据持久化/接口、完整异常状态与自然简洁的真实业务文案。
2. 对照 [anti-ai-ui.md](../references/anti-ai-ui.md) 26 项全栈排雷与 [visual-refinement.md](../references/visual-refinement.md) 做首轮精修。

## Step 6：14 步真实运行验收与 Content Audit（转入 `final-verification.md`）
启动运行，完成全局与局部截图、动效观察、文案审计与问题闭环修复，输出 [delivery-report.md](../templates/delivery-report.md)。

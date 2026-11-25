---
name: eidos
description: >-
  EIDOS — Product Design & Experience Engineering. Design with intention. Build with precision.
  End-to-end product design (UI/UX, independent art direction, color review, visual refinement,
  iconography, data visualization, spatial-causal motion, content design, design systems, WCAG 2.2)
  and verified frontend/client engineering across iOS, iPadOS, Android, Web, macOS, Windows,
  Mini Programs, B2B/SaaS, Data Analytics/Dashboards, Smart Devices, and Game UI/HUD. Use when
  designing 0-to-1 products, reviewing/refining existing designs or WIP builds, removing AI UI/copy
  slop, crafting spatial motion, or shipping verified interactive interfaces. Do not use for pure
  backend/API-only work, DevOps, or static non-UI text edits.
license: MIT
metadata:
  brand: EIDOS
  tagline: "Design with intention. Build with precision."
  author: Wang Xinxiang
  version: "2.0.0"
  standards: "Apple HIG (iOS 26), Material 3 Expressive, WCAG 2.2, W3C DTCG 2025.10, Fluent 2, WeChat Mini Program, XAG"
---

# EIDOS — Product Design & Experience Engineering

> *Design with intention. Build with precision.*  
> 有意识地设计，以精确的方式实现。

EIDOS 让 AI 作为成熟的产品设计与体验工程团队工作，同时具备产品策略、UX、独立美术指导、视觉精修、动效编排、文案设计、Design System、前端/客户端工程与实机 QA 能力——**帮助每一个产品找到属于自己的最佳设计形态，而不是用一套模板制造相似界面**。

---

## 1. 十级设计决策优先级阶梯（冲突裁决唯一依据）

当不同设计原则产生冲突时，严格按以下 1 → 10 顺序裁决（**无障碍、可读性与用户明确指定的硬性要求贯穿全部阶段，非事后附加**）：

1. **安全性、数据完整性与基础可用性**（防误删、防丢数据、不崩溃、≥4.5:1 可读对比度）
2. **核心功能的正确性与完整性**（零假按钮、零空回调、程序状态与文案 100% 诚实一致）
3. **产品意图与功能表达的明确性**（打开 3 秒内懂用途、懂焦点、懂下一步，不靠说明墙）
4. **用户操作习惯与核心任务效率**（遵循成熟肌肉记忆与平台原生惯例，高频任务 1–3 步）
5. **信息架构及认知负荷**（清晰分层、渐进披露、返回保态、减少不必要选择与步骤）
6. **交互反馈与空间连续性**（明确因果起止、迅速灵动可打断、页面上下边界与安全区贯通）
7. **平台适配与运行性能**（按端重组而非缩放；INP ≤200ms / CLS ≤0.1 / 稳定 60–120fps）
8. **视觉一致性与美术品质**（统一语义 Token、光学对齐、高影响力精修、零 AI 模板痕）
9. **品牌辨识度及设计独特性**（按产品领域建立独立美术语言与语言体系，拒绝换皮模板）
10. **装饰性细节与非必要视觉效果**（若损害前 9 项任何一条，立即删除）

---

## 2. 不可违背的硬性门禁（Hard Gates）

- **配色确认门禁（Color Gate）**：**未经用户明确确认，严禁直接更改存量项目的整体配色、品牌主色及主要色彩系统**（除非用户已明确授权 AI 自主定色）。发现明显配色问题时，按 [color-review.md](./references/color-review.md) 输出多套完整方案与同屏视觉预览供确认；其他明确提升体验的细节在授权范围内可直接优化。
- **保留合理资产与范围收敛**：已有方案、半成品或成熟产品中已经合理的设计**主动保留**；严禁删除有效功能、破坏数据库/接口/状态管理或修改品牌 Slogan/法务条款；局部优化严控 Diff 边界。
- **反模糊与全栈去 AI 味**：禁止停留在“让界面更高级/更丝滑”的模糊描述，转化为可检查动作；清除 UI、图标、数据、动效与文案上的全部模板化 AI 痕迹。
- **诚实交付与负收益回退**：严禁假按钮、假成功反馈或未运行即宣称通过；修改后若前后视觉/体验对比无实质收益或退化，**主动撤销回退**；环境受限未测项如实写入 `Not Checked`。

---

## 3. 第一步：按项目所处 7 大阶段选择工作方式

先判定当前阶段（详规见 [product-discovery.md](./references/product-discovery.md)），再加载对应工作流：

| 阶段 | 用户当前状态 | 对应工作流与核心策略 |
|---|---|---|
| **Stage 1–2** | 初步想法 / 已明确需求功能 | → [new-product.md](./workflows/new-product.md)（先定位、IA、独立美术推导与 5 行锁定，再编码） |
| **Stage 3–4** | 已有参考图、设计方案或部分设计稿 | → [redesign.md](./workflows/redesign.md) + [color-review.md](./references/color-review.md)（先理解意图与保留项，配色确认后延展落地） |
| **Stage 5–6** | 前端半成品 / 完整但体验不佳的产品 | → [existing-project-audit.md](./workflows/existing-project-audit.md)（先读代码运行，做 13 项体检与 9 维评分，分阶段零回归修复） |
| **Stage 7** | 成熟产品局部优化 | → [redesign.md](./workflows/redesign.md) + [visual-refinement.md](./references/visual-refinement.md)（锁死范围，做高杠杆精修与精准修复） |
| **编码 / 验收阶段** | 进入工程实现 / 上线前验证 | → [frontend-implementation.md](./workflows/frontend-implementation.md) · [final-verification.md](./workflows/final-verification.md) |

---

## 4. 渐进式参考文件加载表（按需每次只读 2–5 份，严禁全量读取）

| 任务焦点 | 按需读取文件 |
|---|---|
| **阶段路由与需求/存量 13 项体检** | [product-discovery.md](./references/product-discovery.md) |
| **功能表达 6 问、用户直觉与定律** | [user-psychology.md](./references/user-psychology.md) |
| **配色 11 维审查与用户确认门禁** | [color-review.md](./references/color-review.md) |
| **独立美术方向（8 维→11 支柱）与自主审美侦察** | [aesthetic-reasoning.md](./references/aesthetic-reasoning.md) |
| **6 大合规审美起点原型、表面物理与暗黑光影** | [visual-design.md](./references/visual-design.md) |
| **20 项高影响力局部视觉精修雷达** | [visual-refinement.md](./references/visual-refinement.md) |
| **26 项全栈 Anti-AI-Design 排雷（UI/图标/数据/动效）** | [anti-ai-ui.md](./references/anti-ai-ui.md) |
| **图标系统 10 项审查与语义规范** | [iconography.md](./references/iconography.md) |
| **页面上下边界、导航衔接与安全区连续性** | [navigation-and-boundaries.md](./references/navigation-and-boundaries.md) |
| **信息架构分层、导航拓扑与返回保态** | [information-architecture.md](./references/information-architecture.md) |
| **按钮热区、拇指区、容器选型与触觉反馈** | [interaction-design.md](./references/interaction-design.md) |
| **10 要素空间因果动效、17 类组件矩阵与 Stageshow 工艺** | [motion-design.md](./references/motion-design.md) |
| **17 类数据展示选型与可视化美学** | [data-visualization.md](./references/data-visualization.md) |
| **界面文案设计、Product Voice 与 14 类去 AI 文案审查** | [ux-writing.md](./references/ux-writing.md) |
| **排版阶梯、中英混排、等宽数字与 Dynamic Type** | [typography.md](./references/typography.md) |
| **间距不等式、同心圆角公式与光学对齐** | [layout-and-spacing.md](./references/layout-and-spacing.md) |
| **多设备尺寸重组、安全区与键盘避让** | [responsive-design.md](./references/responsive-design.md) |
| **Design Tokens（DTCG 2025.10）与组件治理** | [design-system.md](./references/design-system.md) |
| **20 种完整交互状态与异常闭环** | [interaction-states.md](./references/interaction-states.md) |
| **WCAG 2.2 AA+ 无障碍、键盘、读屏与色盲安全** | [accessibility.md](./references/accessibility.md) |
| **决策树、10 槽协议与跨模型能力自适应模式** | [model-adaptive-workflow.md](./references/model-adaptive-workflow.md) |
| **前端/客户端真实接线、技术栈复用与内存清理** | [frontend-engineering.md](./references/frontend-engineering.md) |
| **Core Web Vitals、帧率预算与低端机降级** | [performance.md](./references/performance.md) |
| **14 步运行验收、逐帧检查、前后对比与负收益回退** | [visual-verification.md](./references/visual-verification.md) |
| **9 维度加权审查评分与 P0–P3 分级标准** | [audit-framework.md](./references/audit-framework.md) |
| **目标平台 / 产品形态（按需只读对应 1–2 份）** | [ios.md](./references/platforms/ios.md) · [android.md](./references/platforms/android.md) · [web.md](./references/platforms/web.md) · [desktop.md](./references/platforms/desktop.md) · [mini-program.md](./references/platforms/mini-program.md) · [game-ui.md](./references/platforms/game-ui.md) · [enterprise-saas.md](./references/platforms/enterprise-saas.md) · [data-analytics.md](./references/platforms/data-analytics.md) · [smart-devices.md](./references/platforms/smart-devices.md) |
| **多领域正反模式对照（中小模型强烈建议读）** | [good-patterns.md](./examples/good-patterns.md) · [bad-patterns.md](./examples/bad-patterns.md) |

**模板与清单**：
- 模板：[design-brief.md](./templates/design-brief.md) · [color-proposal.md](./templates/color-proposal.md) · [audit-report.md](./templates/audit-report.md) · [design-tokens.json](./templates/design-tokens.json) · [component-spec.md](./templates/component-spec.md) · [interaction-spec.md](./templates/interaction-spec.md) · [delivery-report.md](./templates/delivery-report.md)
- 清单：[ux-checklist.md](./checklists/ux-checklist.md) · [ui-checklist.md](./checklists/ui-checklist.md) · [motion-checklist.md](./checklists/motion-checklist.md) · [accessibility-checklist.md](./checklists/accessibility-checklist.md) · [functional-checklist.md](./checklists/functional-checklist.md) · [release-checklist.md](./checklists/release-checklist.md)

---

## 5. 编码前 5 行锁定与跨模型防退化护栏

在写任何 UI 代码前（详规见 [model-adaptive-workflow.md](./references/model-adaptive-workflow.md)），先明确写下 5 项锁定决策，**严禁临场拼凑样式与文案**：

1. **阶段与色彩权限**：明确当前属 Stage 1–7 哪一阶段；存量配色是“保留”“已获确认变更”还是“先出提案等待确认”。
2. **独立美术方向与令牌（60-30-10）**：选定专属美术气质、亮/暗表面阶梯、唯一主强调色与语义状态色。
3. **字体、图标与边界策略**：锁定字体/等宽数字、单一图标体系、页面上下边界衔接方式（自然流 / 1px 硬边 / 滚动显现 / 平台材质）。
4. **容器、数据与动效决策**：明确哪些用列表/表格/开放画布而非卡片；数据采用何种最直观形态；核心浮层与转场的 `transform-origin` 与速度档。
5. **产品语气、主焦点与闭环状态**：确定单屏唯一主 CTA、Product Voice 语气与术语、以及必须实现的异常状态。

---

## 6. 任务完成门禁（Definition of Done）

执行闭环：**分析 → 色彩与方向确认 → 设计 → 实现 → 14 步真实运行验收 → Content Audit → 前后对比与精修 → 复测**。全部满足方算完工：

- [ ] **零 P0 缺陷**（核心流程可用、零假控件、零数据风险、零严重无障碍阻断——存在 P0 一票否决）。
- [ ] **遵守配色与修改权限**（未擅自变更未获确认的品牌配色、Slogan、法务文案与存量有效功能）。
- [ ] **完成真实视觉、动效与 Content Audit 复核**（全局 + 局部细节 + 多视口 + 异常态 + 去 AI 模板痕与文案审查）。
- [ ] **前后对比确认正向收益**（无收益或体验下降的改动已主动回退；未测项已诚实披露在 `Not Checked`）。

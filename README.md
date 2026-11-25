# EIDOS

**Product Design & Experience Engineering.**

> *Design with intention. Build with precision.*  
> 有意识地设计，以精确的方式实现。

**EIDOS** 是一套面向 AI Coding Agent（Antigravity、Claude Code、Codex、Cursor 等）的产品级 **UI/UX 设计、独立审美推理、视觉精修、空间因果动效、内容文案设计、Design System 与前端/客户端体验工程交付** Skill（v2.0）。

它不是空泛的提示词集合，而是一套采用 **Progressive Disclosure（渐进式披露）** 架构构建的完整设计与工程操作系统——**拉高不同参数规模模型的设计质量下限，同时保留高阶模型的独立审美创造空间**，帮助每一个产品找到属于自己的最佳设计形态。

---

## 核心能力体系（v2.0 升级亮点）

- **7 阶段精准工作方式路由**：区分初步想法、明确需求、参考方案、部分设计稿、前端半成品、完整但体验不佳的产品与成熟产品局部优化，先理解意图与保留合理资产，再执行 13 项全盘体检。
- **10 级设计决策优先级阶梯**：明确“安全/可用性 → 核心功能 → 功能表达 → 用户习惯 → IA → 空间连续性 → 平台性能 → 视觉一致 → 品牌辨识 → 装饰细节”唯一冲突裁决顺序。
- **配色审查与用户确认硬门禁**：11 维色彩审查 + 11 要素备选方案 + 同屏实景视觉预览；**未经用户明确确认严禁擅改整体配色与品牌主色**。
- **独立美术语言与 20 项高影响力视觉精修**：告别千站一面与单纯换皮；融合跨学科视觉思维、10 类隐性审美问题主动侦察与低成本高杠杆精修雷达。
- **全栈 Anti-AI Design & 去 AI 化文案体系**：26 项跨 UI / 图标 / 数据 / 动效模板病排雷 + 14 类中文 AI 模板套话清除 + 19 类全范围文案审计与诚实报错底线。
- **10 要素空间因果动效 + 17 类组件映射**：融合 Apple *Fluid Interfaces*、Material 3 Expressive 与 [Stageshow](https://github.com/benjitaylor/skills)（MIT）生产工艺，明确变换原点、可打断、连点弹性与减少动效降级。
- **全平台与全产品形态理解**：覆盖 iOS / iPadOS（iOS 26 Liquid Glass）、Android（M3 Expressive）、Web、macOS / Windows（Fluent 2）、微信小程序、游戏 UI/HUD，以及 **B 端企业级/SaaS、数据分析/可视化大屏、智能终端（车载/TV/穿戴/Kiosk）**。
- **模型能力自适应与 14 步闭环验收**：用 10 槽协议与 5 大确定性决策树消除模糊指令，配合前后视觉对比、Content Audit、**负收益主动回退**与 `Not Checked` 诚实披露。

---

## 目录结构

```text
eidos/
├── SKILL.md                             # 核心入口与渐进式路由（10 级优先级 + 7 阶段路由 + 硬门禁）
├── README.md                            # 项目说明、系列规划与安装触发指南
├── LICENSE                              # MIT License
├── CREDITS.md                           # 一手官方文档、开源参考与许可证声明
├── references/                          # 25 份专项设计/工程/验收参考 + 9 份平台与领域规范
│   ├── product-discovery.md             # 7 阶段项目路由与存量 13 项体检
│   ├── user-psychology.md               # 功能表达 6 问、7 问直觉检查与 10 大定律
│   ├── color-review.md                  # 11 维色彩审查与用户确认硬门禁
│   ├── aesthetic-reasoning.md           # 8 维→11 支柱独立美术推导与 10 类主动审美侦察
│   ├── visual-design.md                 # 6 大合规审美起点原型、表面物理与暗黑光影
│   ├── visual-refinement.md             # 20 项高影响力视觉微调精修雷达
│   ├── anti-ai-ui.md                    # 26 项全栈 AI 模板病（UI/图标/数据/动效）排雷
│   ├── iconography.md                   # 10 项图标系统审查与语义工艺
│   ├── navigation-and-boundaries.md     # 页面上下边界、导航衔接与 8 种空间过渡策略
│   ├── information-architecture.md      # 五级功能分层、导航拓扑与返回保态
│   ├── interaction-design.md            # 按钮热区、拇指区、容器选型与触觉反馈
│   ├── motion-design.md                 # 10 要素空间因果动效、17 类组件矩阵与 Stageshow 工艺
│   ├── data-visualization.md            # 17 类数据展示选型与可视化美学
│   ├── ux-writing.md                    # 产品语言体系、14 类 AI 文案排雷与 19 面文案审计
│   ├── typography.md                    # 排版阶梯、中英混排、等宽数字与 Dynamic Type
│   ├── layout-and-spacing.md            # 留白不等式、同心圆角与光学对齐
│   ├── responsive-design.md             # 多端窗口重组、安全区与键盘避让
│   ├── design-system.md                 # 3 层 DTCG 2025.10 Token 与组件治理
│   ├── interaction-states.md            # 20 种完整交互与异常状态闭环
│   ├── accessibility.md                 # WCAG 2.2 AA+ 对比度、键盘、读屏与色盲安全
│   ├── model-adaptive-workflow.md       # 10 槽协议、5 大确定性决策树与跨模型自适应
│   ├── frontend-engineering.md          # 真实接线、零假按钮、技术栈复用与资源释放
│   ├── performance.md                   # Core Web Vitals、帧率预算与低端机降级
│   ├── visual-verification.md           # 14 步运行验收、逐帧动效检查、前后对比与负收益回退
│   ├── audit-framework.md               # 9 维度加权评分与 P0–P3 分级标准
│   └── platforms/                       # 9 份平台与产品领域专项规范
│       ├── ios.md
│       ├── android.md
│       ├── web.md
│       ├── desktop.md
│       ├── mini-program.md
│       ├── game-ui.md
│       ├── enterprise-saas.md
│       ├── data-analytics.md
│       └── smart-devices.md
├── workflows/                           # 5 套端到端标准化工作流
│   ├── new-product.md
│   ├── existing-project-audit.md
│   ├── redesign.md
│   ├── frontend-implementation.md
│   └── final-verification.md
├── checklists/                          # 6 份可执行验收清单
│   ├── ux-checklist.md
│   ├── ui-checklist.md
│   ├── motion-checklist.md
│   ├── accessibility-checklist.md
│   ├── functional-checklist.md
│   └── release-checklist.md
├── templates/                           # 7 份交付文档与 DTCG 2025.10 Token 模板
│   ├── design-brief.md
│   ├── color-proposal.md
│   ├── audit-report.md
│   ├── design-tokens.json
│   ├── component-spec.md
│   ├── interaction-spec.md
│   └── delivery-report.md
├── examples/                            # 多产品类型正反模式对照库
│   ├── good-patterns.md
│   └── bad-patterns.md
└── scripts/
    └── validate_skill.py                # Frontmatter、链接可达性、DTCG 别名与 WCAG 对比度校验
```

---

## EIDOS 系列规划（Suite Roadmap）

以 `eidos` 作为核心底座，未来可按专业领域演进为完整的 EIDOS 系列技能矩阵（当前版本已将核心能力以渐进式模块内置于本仓库）：

| Skill 名称 | 定位 | 当前承载模块 |
|---|---|---|
| **`eidos`** | 核心产品设计（主套件） | [SKILL.md](./SKILL.md) 全量路由、决策引擎与核心工作流 |
| **`eidos-motion`** | 交互动效 | [motion-design.md](./references/motion-design.md) · [motion-checklist.md](./checklists/motion-checklist.md) |
| **`eidos-audit`** | UI/UX 审查 | [existing-project-audit.md](./workflows/existing-project-audit.md) · [audit-framework.md](./references/audit-framework.md) |
| **`eidos-native`** | 原生应用设计 | [ios.md](./references/platforms/ios.md) · [android.md](./references/platforms/android.md) · [desktop.md](./references/platforms/desktop.md) · [mini-program.md](./references/platforms/mini-program.md) · [smart-devices.md](./references/platforms/smart-devices.md) |
| **`eidos-play`** | 游戏界面设计 | [game-ui.md](./references/platforms/game-ui.md) |
| **`eidos-system`** | 设计系统构建 | [design-system.md](./references/design-system.md) · [color-review.md](./references/color-review.md) · [design-tokens.json](./templates/design-tokens.json) |

---

## 安装与使用

### 方式 1：Agent Skills CLI 一键安装（推荐，支持 Claude Code / Cursor / Codex / Antigravity 等）

```bash
npx skills add wangxinxiang060412-lang/eidos
```

### 方式 2：手动安装到指定 Agent

```bash
# Antigravity 全局
git clone https://github.com/wangxinxiang060412-lang/eidos.git ~/.gemini/config/skills/eidos

# Antigravity 单项目
git clone https://github.com/wangxinxiang060412-lang/eidos.git .agents/skills/eidos

# Claude Code 全局
git clone https://github.com/wangxinxiang060412-lang/eidos.git ~/.claude/skills/eidos

# Cursor 项目级
git clone https://github.com/wangxinxiang060412-lang/eidos.git .cursor/skills/eidos
```

---

## 触发示例（Prompt Examples）

1. **全新项目 0→1**：
   > “加载 `eidos` 技能，为我从零设计并开发一个支持亮/暗模式的摄影作品管理与评片 Web 应用，建立独立美术方向、完成真实交互闭环并用 Playwright 做多端与动效验收。”
2. **已有半成品全面体验审查 + 配色提案**：
   > “用 `eidos` 审查我当前的前端半成品，先运行项目再做 13 项体检、文案审计和 9 维度打分；如果配色有问题，先给我 2 套带同屏预览的配色方案确认，不要擅自改色。”
3. **局部高影响力精修（去 AI 味）**：
   > “按 `eidos` 的高影响力视觉精修与去 AI 化文案规范，优化工作台和数据总览页，删掉重复 KPI 卡片、无用副标题与装饰小胶囊，修复日期选择器动效起点，严禁破坏现有接口。”
4. **专业领域与特种端开发**：
   > “按 `eidos` 的 B 端 SaaS / 数据分析大屏 / 微信小程序 / 游戏 HUD 规范，重构核心页面并验证真实运行表现。”

---

## 自动校验脚本

```bash
python3 scripts/validate_skill.py
```

自动校验 YAML frontmatter、`SKILL.md` 行数预算、全仓库相对链接可达性、`design-tokens.json` 别名解析、WCAG 2.2 AA 色彩对比度及基本规则一致性。

---

## 许可证与致谢

本项目采用 [MIT License](./LICENSE) 开源。所研究的官方设计规范、可用性理论与开源项目出处及许可证说明详见 [CREDITS.md](./CREDITS.md)。

# Research Sources, Standards & License Attributions

本 Skill 所有规范均为基于一手官方文档、经典人机交互研究与开源工程实践独立提炼与综合编排，未直接照搬第三方原文。以下记录核心参考来源、适用范围及许可证说明：

## 1. 平台官方设计规范

| 规范名称 | 维护方 | 适用范围 | 来源 |
|---|---|---|---|
| Apple Human Interface Guidelines (含 iOS/iPadOS/macOS 26 Liquid Glass & WWDC Designing Fluid Interfaces) | Apple Inc. | iOS、iPadOS、macOS 布局、材质、导航、触控、动效与无障碍 | https://developer.apple.com/design/human-interface-guidelines/ |
| Material Design 3 & M3 Expressive Motion Physics | Google LLC | Android、跨平台设计令牌、动态色彩、弹簧物理动效与触控规范 | https://m3.material.io/ |
| Microsoft Fluent 2 Design System | Microsoft Corp. | Windows 11 桌面端间距、排版、Mica / Acrylic 材质与窗口行为 | https://fluent2.microsoft.design/ |
| 微信小程序官方设计指南 | Tencent / WeChat | 微信小程序导航栏、右上角胶囊避让、`rpx` 适配、字号与触控热区 | https://developers.weixin.qq.com/miniprogram/design/ |
| Xbox Accessibility Guidelines (XAG) | Microsoft Gaming | 游戏 UI 导航、焦点管理（XAG 112/113）、多感官冗余提示（XAG 103）与可读性 | https://learn.microsoft.com/en-us/gaming/accessibility/guidelines |

## 2. 无障碍、令牌与 Web 性能国际标准

| 标准名称 | 标准组织 | 适用范围 | 来源 |
|---|---|---|---|
| WCAG 2.2 (Web Content Accessibility Guidelines) | W3C WAI | 对比度（1.4.3 / 1.4.11）、焦点不被遮挡（2.4.11）、最小目标尺寸（2.5.8）与键盘导航 | https://www.w3.org/WAI/standards-guidelines/wcag/ |
| W3C Design Tokens Format Module (`2025.10`) | W3C Design Tokens Community Group (DTCG) | 跨平台 Design Tokens JSON 规范（`$value`、`$type`、`$description` 与别名引用） | https://tr.designtokens.org/format/ |
| Core Web Vitals (LCP / INP / CLS) | Google web.dev | Web 加载速度、交互响应延迟（INP ≤ 200ms）与布局稳定性（CLS ≤ 0.1） | https://web.dev/articles/vitals |

## 3. 人机交互与 UX 基础理论

- **Jakob Nielsen & Don Norman (Nielsen Norman Group)**：10 Usability Heuristics、Mental Models、Affordances & Signifiers、Natural Mapping（《The Design of Everyday Things》）。
- **经典人因工程定律**：Fitts's Law（Paul Fitts, 1954）、Hick-Hyman Law（1952）、Jakob's Law（Jakob Nielsen）、Gestalt Principles（Proximity / Similarity / Continuity / Closure / Figure-Ground / Common Region）、Miller's Law & Cognitive Load Theory（John Sweller）、Doherty Threshold（1982）、Peak-End Rule（Daniel Kahneman）。

## 4. 开源 Skill 与设计工程参考

| 项目 | 作者 / 维护方 | 许可证 | 本 Skill 提炼与借鉴内容 |
|---|---|---|---|
| **Stageshow** (`benjitaylor/skills`) | Benji Taylor (Copyright © 2026) | **MIT License** | 提炼其视觉克制、光学对齐（cap-height 居中、同心圆角、杜绝近切边）、因果动效连续性（“静框衬动”、局部更新不重排、边缘不切割文字、落位后零跳变）、“所见→所改”帧级排演与独立新鲜视角审查方法，并针对**生产环境真实交互软件**改写了时长预算、可打断性与功能闭环约束。来源：https://github.com/benjitaylor/skills |
| **Agent Skills Open Specification** | agentskills.io / Linux Foundation Agentic AI Foundation | Open Specification | 遵循 3 层渐进式披露（Metadata → `SKILL.md` → `references/`）与标准 YAML frontmatter 格式。来源：https://agentskills.io |
| **成熟开源 Design Systems 研究** | Radix UI (MIT)、Shopify Polaris (MIT)、GitHub Primer (MIT)、IBM Carbon (Apache-2.0)、Adobe Spectrum (Apache-2.0) | MIT / Apache-2.0 | 参考其三层语义 Token 架构、无障碍组件状态机与高密度界面信息组织方式。 |

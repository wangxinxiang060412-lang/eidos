# Research Sources, Standards & License Attributions

**EIDOS** 所有规范均为基于一手官方文档、经典人机交互与跨学科设计研究、以及开源工程实践独立提炼与综合编排，未直接照搬第三方原文。以下记录核心参考来源、适用范围及许可证说明：

## 1. 平台与终端官方设计规范

| 规范名称 | 维护方 | 适用范围 | 来源 |
|---|---|---|---|
| Apple Human Interface Guidelines (含 iOS/iPadOS/macOS 26 Liquid Glass & WWDC Designing Fluid Interfaces) | Apple Inc. | iOS、iPadOS、macOS、watchOS、tvOS 布局、材质、边界、动效与无障碍 | https://developer.apple.com/design/human-interface-guidelines/ |
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

## 3. 人机交互、跨学科美学与数据可视化理论

- **人机交互与 UX**：Jakob Nielsen & Don Norman（10 Usability Heuristics、Mental Models、Affordances & Signifiers、Natural Mapping）；Fitts's Law、Hick-Hyman Law、Jakob's Law、Gestalt Principles、Cognitive Load Theory、Doherty Threshold、Peak-End Rule。
- **跨学科视觉与排版**：Swiss International Typographic Style（Josef Müller-Brockmann 网格与比例秩序）、Dieter Rams《好设计的十条原则》（功能诚实与克制）、Edward Tufte 数据墨水比与诚实可视化原则（《The Visual Display of Quantitative Information》）。

## 4. 开源 Skill 与设计工程参考

| 项目 | 作者 / 维护方 | 许可证 | 本 Skill 提炼与借鉴内容 |
|---|---|---|---|
| **Stageshow** (`benjitaylor/skills`) | Benji Taylor (Copyright © 2026) | **MIT License** | 提炼其视觉克制、光学对齐（cap-height 居中、同心圆角、杜绝近切边）、空间因果连续性（“静框衬动”、原位态变、边缘不切字、锚点不漂移、落位零跳变）、“所见→所改”帧级排演与新鲜视角审查方法，并针对**生产环境真实交互软件**改写了时长预算、可打断性与功能闭环约束。来源：https://github.com/benjitaylor/skills |
| **Agent Skills Open Specification** | agentskills.io / Linux Foundation Agentic AI Foundation | Open Specification | 遵循 3 层渐进式披露（Metadata → `SKILL.md` → `references/`）与标准 YAML frontmatter 格式。来源：https://agentskills.io |
| **成熟开源 Design Systems 研究** | Radix UI (MIT)、Shopify Polaris (MIT)、GitHub Primer (MIT)、IBM Carbon (Apache-2.0)、Adobe Spectrum (Apache-2.0) | MIT / Apache-2.0 | 参考其三层语义 Token 架构、无障碍组件状态机、产品内容语气规范（Content Design）与高密度 B 端信息组织。 |

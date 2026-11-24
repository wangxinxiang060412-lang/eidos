# Product Design & Frontend Engineering Skill

一套面向 AI Coding Agent（Antigravity、Claude Code、Codex、Cursor 等）的产品级 **UI/UX 设计、审美规范、动效工艺、Design System 与前端/客户端工程交付** Skill。

它不是空泛的审美提示词，也不是静态页面生成器，而是一套采用 **Progressive Disclosure（渐进式披露）** 架构构建的完整设计与工程操作系统——让不同参数规模的模型都能像成熟产品研发团队一样思考、克制审美、完整编码、运行验收并对最终体验负责。

---

## 核心特性

- **双模式工作流**：
  - **存量项目**：先读代码 → 理解业务 → 运行观察 → 9 维度打分与 P0–P3 审查 → 最小范围精准优化 → 回归验收（绝不为了炫技重构，绝不破坏数据库/接口/已有功能）。
  - **全新项目 0→1**：产品定位 → 用户心理与 IA → 5 行审美与令牌锁定 → 交互与动效规格 → 真实工程实现 → 运行截图/录屏闭环验收。
- **高审美下限保障（低参数模型友好）**：内置 6 套经过对比度验证的产品级审美原型（含精确 Hex / OKLCH 表面阶梯、文字阶梯、亮暗双模式）、同心圆角公式、留白不等式、多层次柔和阴影配方与 18 项 Anti-AI-UI 精准排雷清单，将“高级审美”转化为可执行的数学与判断规则。
- **全平台原生规范覆盖**：iOS / iPadOS（含 iOS 26 Liquid Glass 导航层铁律）、Android（Material 3 Expressive 弹簧物理令牌）、现代 Web（WCAG 2.2 + Core Web Vitals）、Desktop（macOS 26 + Windows 11 Fluent 2 Mica/Acrylic）、微信小程序（官方胶囊避让与 `rpx` 适配）、游戏 UI / HUD（Diegetic/Spatial/Meta 分类、手柄焦点图与 XAG 无障碍规范）。
- **因果动效与 Stageshow 工艺融合**：提炼 [benjitaylor/skills (Stageshow)](https://github.com/benjitaylor/skills) 的构图、光学对齐、帧级排演与“所见→所改”验收法，并明确区分**演示型动效**与**生产环境功能性交互动效**（可打断、速度投影、≤300ms 响应、尊重 `prefers-reduced-motion`）。
- **严格验收与诚实汇报机制**：引入 P0 一票否决制与 `Not Checked` 强制披露，杜绝仅靠读代码就宣称“UI 已完成”。

---

## 目录结构

```text
product-design-engineering/
├── SKILL.md                          # 核心入口与渐进式路由（YAML frontmatter 符合 agentskills.io & Antigravity 规范）
├── README.md                         # 项目说明、安装与触发指南
├── LICENSE                           # MIT License
├── CREDITS.md                        # 一手官方文档、开源参考与许可证声明
├── references/                       # 18 份核心设计/工程/验收参考 + 6 份平台专项规范
│   ├── product-discovery.md
│   ├── user-psychology.md
│   ├── information-architecture.md
│   ├── interaction-design.md
│   ├── motion-design.md
│   ├── visual-design.md
│   ├── anti-ai-ui.md
│   ├── typography.md
│   ├── layout-and-spacing.md
│   ├── responsive-design.md
│   ├── design-system.md
│   ├── accessibility.md
│   ├── interaction-states.md
│   ├── ux-writing.md
│   ├── frontend-engineering.md
│   ├── performance.md
│   ├── visual-verification.md
│   ├── audit-framework.md
│   └── platforms/
│       ├── ios.md
│       ├── android.md
│       ├── web.md
│       ├── desktop.md
│       ├── mini-program.md
│       └── game-ui.md
├── workflows/                        # 5 套端到端标准化工作流
│   ├── new-product.md
│   ├── existing-project-audit.md
│   ├── redesign.md
│   ├── frontend-implementation.md
│   └── final-verification.md
├── checklists/                       # 6 份可执行验收清单
│   ├── ux-checklist.md
│   ├── ui-checklist.md
│   ├── motion-checklist.md
│   ├── accessibility-checklist.md
│   ├── functional-checklist.md
│   └── release-checklist.md
├── templates/                        # 6 份交付文档与 DTCG 2025.10 Token 模板
│   ├── design-brief.md
│   ├── audit-report.md
│   ├── design-tokens.json
│   ├── component-spec.md
│   ├── interaction-spec.md
│   └── delivery-report.md
├── examples/                         # 正反模式对照库（带精确代码与设计推演）
│   ├── good-patterns.md
│   └── bad-patterns.md
└── scripts/
    └── validate_skill.py             # Skill 结构、链接、Frontmatter 与 Token JSON 自动校验脚本
```

---

## 安装与使用

### 方式 1：通过 Agent Skills CLI 一键安装（支持 Claude Code / Cursor / Codex / Antigravity 等）

```bash
npx skills add wangxinxiang060412-lang/product-design-engineering
```

### 方式 2：安装到 Antigravity（全局或单项目）

- **全局生效（所有项目可用）**：
  ```bash
  git clone https://github.com/wangxinxiang060412-lang/product-design-engineering.git \
    ~/.gemini/config/skills/product-design-engineering
  ```
- **单项目生效（提交进团队仓库）**：
  ```bash
  git clone https://github.com/wangxinxiang060412-lang/product-design-engineering.git \
    .agents/skills/product-design-engineering
  ```

### 方式 3：安装到 Claude Code / Cursor

```bash
# Claude Code 全局
git clone https://github.com/wangxinxiang060412-lang/product-design-engineering.git \
  ~/.claude/skills/product-design-engineering

# Cursor 项目级
git clone https://github.com/wangxinxiang060412-lang/product-design-engineering.git \
  .cursor/skills/product-design-engineering
```

---

## 触发示例（Prompt Examples）

1. **全新项目 0→1**：
   > “使用 `product-design-engineering` 技能，为我从零设计并开发一个支持亮/暗模式的个人财务与订阅管理 Web 应用，需要完整的数据录入、筛选、撤销删除、移动端适配和 Playwright 视觉验收。”
2. **存量项目体验审查**：
   > “请按 `product-design-engineering` 的存量项目审查流程，先运行我的项目，对所有页面、导航和按钮做一次完整的 UI/UX Audit，输出加权评分和 P0–P3 优化清单，先不要改代码。”
3. **局部改版与去 AI 味**：
   > “帮我优化设置页和商品详情页的视觉层级与交互动效，去掉现在的紫蓝渐变和嵌套卡片味，但绝对不要改动已有的结算接口和状态管理逻辑。”
4. **跨端与平台原生开发**：
   > “按微信小程序原生规范重构点单页与购物车底栏，注意避让右上角胶囊按钮、适配全面屏底部安全区，并补全空态与断网重试。”
5. **游戏 UI 与 HUD 设计**：
   > “为这款俯视角动作 Roguelike 游戏设计战斗 HUD 与背包界面，要求支持手柄焦点导航、高对比度可读性以及非侵入式低血量反馈。”

---

## 校验 Skill 完整性

仓库内置自检脚本，修改任何文件后可运行：

```bash
python3 scripts/validate_skill.py
```

自动校验 YAML frontmatter 合规性、`SKILL.md` 上下文预算、全仓库相对 Markdown 链接有效性、`design-tokens.json` 格式与基本一致性检查。

---

## 许可证与致谢

本项目采用 [MIT License](./LICENSE) 开源。所研究的官方设计规范、可用性理论与开源项目出处及许可证说明详见 [CREDITS.md](./CREDITS.md)。

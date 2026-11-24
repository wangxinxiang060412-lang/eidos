# Design System Architecture & Token Governance

Design System 的核心目标是**让产品在不同页面、不同主题与不同端保持一致的秩序与高质量体验，同时不因过度抽象拖垮工程迭代速度**。

---

## 1. 三层 Token 架构（遵循 W3C DTCG `2025.10` 标准）

严禁在业务组件中到处硬编码十六进制色值（如 `#3B82F6`）、随意像素值或魔术毫秒数。采用清晰三层架构（完整 JSON 起始模板见 [design-tokens.json](../templates/design-tokens.json)）：

| 层级 | 作用 | 命名示例 | 使用规则 |
|---|---|---|---|
| **Tier 1: Primitive（基础色阶/标尺）** | 定义原始调色板与物理刻度，不表达含义 | `color.neutral.50`、`color.blue.600`、`space.4` | **禁止业务组件直接引用**（仅被语义层引用） |
| **Tier 2: Semantic（语义令牌）** | 定义界面角色与意图，负责亮/暗主题与品牌切换 | `color.bg.canvas`、`color.bg.surface`、`color.text.primary`、`color.accent.primary`、`color.status.destructive` | **业务组件默认唯一引用层** |
| **Tier 3: Component（组件级令牌，按需）** | 仅当某高频复杂组件需要独立换肤或精细调节时建立 | `button.primary.bg`、`input.border.focus` | **克制使用**：普通小项目停在 Tier 2 即可，避免过度设计 |

### 必需的核心语义 Token 集合
- **Surface（背景层级）**：`bg.canvas`、`bg.surface`、`bg.surface-raised`、`bg.surface-overlay`、`bg.subtle`（悬浮/选中浅底）
- **Text（文字阶梯）**：`text.primary`、`text.secondary`、`text.tertiary`、`text.disabled`、`text.on-accent`
- **Border（边界阶梯）**：`border.subtle`、`border.default`、`border.strong`、`border.focus`
- **Brand & Interactive**：`accent.primary`、`accent.primary-hover`、`accent.primary-active`、`accent.subtle`
- **Semantic Status**：`status.success`、`status.warning`、`status.destructive`、`status.info`（各配对应 `-bg` 与 `-text` 高对比组合）
- **Scale & Physics**：`typography.*`、`space.*`、`radius.*`、`shadow.*`、`motion.duration.*`、`motion.easing.*`、`zIndex.*`

---

## 2. 亮 / 暗主题治理原则

1. **主题切换零硬编码**：所有页面元素与图标均通过语义 Token 驱动，切换 Light / Dark 时只需替换语义映射表，严禁在业务代码里写满 `isDark ? '#111' : '#fff'`。
2. **语义对等而非数学反转**：
   - 浅色卡片常用白底 + 灰画布；暗色卡片用更浅一层灰底 + 深灰画布 + 细微顶边高光。
   - 语义状态色（红/绿/黄）在暗色下需要更高明度与更低刺眼纯度，确保对比度 ≥ 4.5:1。
3. **尊重系统偏好 + 支持手动覆盖**：默认跟随系统 `prefers-color-scheme` / 系统深色模式，提供“跟随系统 / 浅色 / 深色”三态切换并持久化。

---

## 3. 组件抽象与治理纪律（防止“设计系统过工程化”）

- **同功能同表现**：同一产品的搜索框、日期选择、确认弹窗、分页器、Toast 必须统一复用一套基础组件，绝不允许 A 页面和 B 页面长得像两家公司写的。
- **单一职责与组合优于巨型 Props 怪兽**：
  - 基础原语（Button、Input、Select、Dialog、Sheet、Tabs、Toast）必须内置完整交互态、键盘导航与无障碍属性（Web 优先基于 Radix UI / React Aria / Base UI 等 Headless 无障碍原语，避免手写漏洞百出的下拉框与焦点陷阱）。
  - **禁止过度抽象**：如果一个业务卡片只在一个页面出现，直接用语义 Token + 基础原语组合编写即可，不要为它抽象一个带 25 个布尔开关的 `<SuperUniversalCard />`。
- **组件交付规格**：新建或重构核心共享组件时，参照 [component-spec.md](../templates/component-spec.md) 明确 Anatomy、Variants、States、Tokens 与 A11y 契约。

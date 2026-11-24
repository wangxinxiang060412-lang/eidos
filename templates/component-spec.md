# Component Specification: <组件名>

## 1. 用途与非用途
- **适用场景**：`<何时应该用它>`
- **不适用场景**：`<何时应该改用其他组件，避免滥用>`

## 2. 结构剖析（Anatomy）
- 根容器：`...`（最小触控热区：`≥ 44px` / `≥ 32px` 桌面）
- 必选插槽：`label` / `content`
- 可选插槽：`leadingIcon`（固定尺寸 `flex: none`）、`trailingIcon` / `shortcut`

## 3. 变体与尺寸（Variants & Sizes）
| 属性 | 可选值 | 默认值 | 使用约束 |
|---|---|---|---|
| `variant` | `primary` / `secondary` / `ghost` / `destructive` | `secondary` | 单屏最多 1 个 `primary` |
| `size` | `sm` (`32px`) / `md` (`38px`) / `lg` (`44px`) | `md` | 移动端主操作默认 `lg` |

## 4. 完整状态与 Token 映射
| 状态 | 背景 Token | 文字 Token | 边框 / 动效行为 |
|---|---|---|---|
| Default | `...` | `...` | `...` |
| Hover | `...` | `...` | `150ms effect`（仅 `@media (hover: hover)`） |
| Active | `...` | `...` | `0ms` 即时 `scale(0.98)` |
| Focus-Visible | 继承 | 继承 | `2px solid border.focus`, `offset 2px` |
| Selected / Open | `...` | `...` | 保持视觉高亮 |
| Disabled | `...` | `text.disabled` | `cursor: not-allowed`，必要时提供禁用原因 |
| Loading | 保持原色 | 隐藏文案或伴随进度 | **锁定原宽度防周围跳动**，拦截重复点击 |

## 5. 无障碍与键盘契约
- 原生标签 / Role：`<button>` / `role="..."`
- 键盘操作：`Enter` / `Space` / `Esc` / 方向键行为
- 读屏属性：`aria-label` / `aria-busy` / `aria-expanded` / `aria-controls`

## 6. 边界情况
- 超长文案策略（截断 / 换行）、窄屏表现、200% 字体缩放、暗黑模式验证要点。

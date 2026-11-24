# Good Patterns: High-Craft Production UI & Interaction Recipes

本文件提供可直接复用的高工艺模式，帮助不同参数规模的模型稳定交付接近资深产品团队水准的视觉、交互与工程细节。

---

## 1. 同心圆角与克制柔和卡片（光影 & 暗黑双模式）

**要点**：外圆角 = 内圆角 + 内边距；亮色用“极细 1px 描边 + 贴底接触影 + 环境柔影”，暗色用**提亮表面一档 + 顶部 1px 微光**，零脏黑重影。

```css
.card {
  --card-padding: 12px;
  --inner-radius: 6px;
  padding: var(--card-padding);
  border-radius: calc(var(--inner-radius) + var(--card-padding)); /* 18px 同心圆角 */
  background: var(--bg-surface);
  box-shadow:
    0 0 0 1px rgba(15, 23, 42, 0.06),
    0 1px 2px rgba(15, 23, 42, 0.05),
    0 6px 16px -4px rgba(15, 23, 42, 0.06);
}

[data-theme="dark"] .card {
  background: var(--bg-surface); /* #14171D 位于 #0D0F12 画布之上 */
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.06),
    0 0 0 1px rgba(255, 255, 255, 0.08);
}

.card-media {
  border-radius: var(--inner-radius); /* 6px 严丝合缝 */
  aspect-ratio: 16 / 10;              /* 预声明比例防止 CLS 跳动 */
  object-fit: cover;
}
```

---

## 2. 锁宽防跳动 + 原地 Loading 态生产按钮

**要点**：点击瞬间响应按压缩放；切入 Loading 时原地保留文案宽度（CSS Grid 单格叠放），旁边按钮绝不抖动；仅桌面真鼠标设备启用 Hover，且实心按钮悬停加深本色不灰掉；仅键盘导航显示 `:focus-visible`。

```css
.btn-primary {
  display: inline-grid;
  place-items: center;
  min-height: 40px;                 /* 移动端可调至 44px */
  padding: 0 16px;
  border: 0;
  border-radius: 8px;
  background: var(--accent-primary);
  color: var(--text-on-accent);
  font-weight: 500;
  transition: background-color 150ms cubic-bezier(0.2, 0, 0, 1),
              transform 100ms cubic-bezier(0.2, 0, 0, 1);
}

.btn-primary > * { grid-area: 1 / 1; } /* 文案与 Spinner 共享一格，切态零宽跳 */

@media (hover: hover) and (pointer: fine) {
  .btn-primary:hover:not(:disabled) { background: var(--accent-primary-hover); }
}

.btn-primary:active:not(:disabled) { transform: scale(0.98); }

.btn-primary:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: 2px;
}

.btn-primary[data-loading="true"] .btn-label { visibility: hidden; }

@media (prefers-reduced-motion: reduce) {
  .btn-primary { transition: none; }
  .btn-primary:active:not(:disabled) { transform: none; }
}
```

---

## 3. 乐观删除 + 5 秒可撤销闭环（优于烦人的“确定要删除吗？”）

**要点**：对可逆删除/归档立即从列表中平滑折叠移出，底部弹出带 `aria-live="polite"` 的 Toast 提供 **“撤销”** 动作；超时后才真正提交远端/永久销毁，中途点击撤销则原位恢复。

```text
用户点击“归档”
  ├─ 0ms   ：列表项先淡出内容（80ms）再平滑闭合高度（200ms，不硬切文字）
  ├─ 50ms  ：底部安全区上方浮现 Toast：“已归档《Q4 预算表》 [撤销]”
  ├─ 5s 内 ：用户点“撤销” → 取消定时器，条目在原索引位置平滑重新展开
  └─ 5s 后 ：执行真正持久化删除；若接口失败 → 自动回滚条目并提示失败重试
```

---

## 4. 列表行替代多余卡片网格（高信噪比信息密度）

**要点**：设置页、账单明细、订单列表用统一网格轨道（固定列宽 + `flex-shrink: 0` 图标列 + 弹性主内容列 `min-width: 0` + 右对齐 `tabular-nums` 金额列）+ 极细内嵌分割线。

```css
.bill-row {
  display: grid;
  grid-template-columns: 36px minmax(0, 1fr) auto;
  align-items: center;
  gap: 12px;
  min-height: 56px;
  padding: 10px 16px;
  border-bottom: 1px solid var(--border-subtle);
}

.bill-title {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: var(--text-primary);
}

.bill-amount {
  font-variant-numeric: tabular-nums;
  white-space: nowrap;              /* 数值与货币单位绝不折行 */
  font-weight: 600;
}
```

---

## 5. 不硬切文字的平滑展开折叠（Grid Row Transition）

**要点**：绝不对 `height: auto` 做生硬裁剪；用 `grid-template-rows: 0fr → 1fr` 驱动容器空间，内部内容淡入略滞后、淡出略提前，边缘永远不劈文字。

```css
.disclosure-panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 240ms cubic-bezier(0.22, 1, 0.36, 1);
}
.disclosure-panel[data-open="true"] { grid-template-rows: 1fr; }

.disclosure-inner {
  overflow: hidden;
  opacity: 0;
  transition: opacity 140ms ease;
}
.disclosure-panel[data-open="true"] .disclosure-inner {
  opacity: 1;
  transition-delay: 60ms;
}
```

---

## 6. 微信小程序自定义导航栏精准胶囊避让（计算范式）

```js
// 动态计算导航栏尺寸，严禁硬编码 88px / 44px
const { statusBarHeight, screenWidth } = wx.getWindowInfo();
const capsule = wx.getMenuButtonBoundingClientRect();
const navGap = capsule.top - statusBarHeight;
const navBarHeight = capsule.height + navGap * 2;
const rightSafeInset = screenWidth - capsule.left + 8; // 右侧控件必须避开此宽度
const canGoBack = getCurrentPages().length > 1;        // 深层直达时切回首页图标
```

---

## 7. 原生移动端高质感速配参考

- **iOS 26 (SwiftUI)**：列表内容区保持实色高对比 `.listStyle(.insetGrouped)`；仅悬浮操作栏/底栏应用系统默认材质或 `.glassEffect()`；按钮热区用 `.frame(minWidth: 44, minHeight: 44)`；金额数字加 `.monospacedDigit()`；支持 `.accessibilityReduceMotion`。
- **Android (Jetpack Compose)**：入口调用 `enableEdgeToEdge()`，用 `Modifier.windowInsetsPadding(WindowInsets.safeDrawing)` 避让系统栏；层次用 `MaterialTheme.colorScheme.surfaceContainerLow / High`；列表强制 `LazyColumn` + 稳定 `key`；动效优先 `MaterialTheme.motionScheme.defaultSpatialSpec()` / `fastEffectsSpec()`。

# Good Patterns: Multi-Domain High-Craft UI, Motion & Copy Recipes

本文件提供跨产品类型的**高工艺正例与可执行配方**，帮助不同参数规模的模型直观理解“为什么这种设计适合这类产品”以及如何落盘到精确代码。

---

## 一、六类不同产品的独立设计形态（为什么它们不该长得一样）

| 产品类型 | 优秀设计形态特征 | 为什么适合它 |
|---|---|---|
| **1. 摄影 / 影像评片工具** | 极低饱和度暗中性画布（`#161618`），照片近乎满出血居中展示，右侧 `280px` 紧致检查器用 `12px` 等宽数字展示光圈/快门/ISO 与直方图，界面零装饰彩色 | 用户的眼睛必须把 100% 色彩敏感度留给照片本身；任何彩色徽章、厚白边或花哨阴影都会干扰曝光与白平衡判断 |
| **2. 个人理财 / 金融分析** | 冷静中性亮画布（`#F5F7FA`），顶部“总资产 Hero Stat + 周期涨跌（符号+颜色+基准）”配一条极简 30 日 Sparkline；下方直接进入分组账单明细行，金额右对齐 + `tabular-nums` | 金融用户追求审慎核对与秒级扫视，清晰排版比 4 张同质化圆角 KPI 卡片与花哨圆环图可信十倍 |
| **3. B 端企业级 / SaaS 后台** | 紧凑 `52px` 顶栏 + 可收起 `220px` 左侧导航 + 硬边界 `1px` 分隔；高密度数据表（行高 `40px`、吸顶表头、批量勾选浮动操作条）；点击单据从右侧滑出详情抽屉（Side Drawer） | 业务人员每天处理数百单，保留列表上下文的右侧抽屉与高信噪比表格比反复整页跳转和虚空大留白效率高数倍 |
| **4. 消费生活 / 微信小程序** | 微暖米纸底（`#FAF8F5`）+ 唯一温润陶土/鼠尾草主色；顶部动态避让微信右上角胶囊；底部固定栏叠加 `env(safe-area-inset-bottom)` 且列表底部留足防遮挡呼吸空间；标题直给“收藏 / 点单”，零废话副标题 | 贴合日常高频单手使用场景，温润克制又不牺牲点击准度与可读性 |
| **5. 学习 / 音乐内容产品** | 阅读/学习类严控 `60–66ch` 舒展行宽与 `1.65` 中文行高；音乐播放器以专辑封面为绝对焦点，底部迷你播放条自然延伸背景材质并在点击时平滑展开为全屏播放页 | 内容本身是主角，界面退后为节奏清晰、边界连续的沉浸容器 |
| **6. 动作 / 策略游戏 UI & HUD** | 中心战斗视野 100% 纯净；边缘 HUD 契合世界观材质，浮于 3D 画面上的血量与冷却自带暗色柔边保护层；手柄 D-Pad 焦点框极清晰，插拔键鼠实时切换按键图标 | 兼顾高压瞬间读数、动态亮暗背景可读性与世界观沉浸感 |

---

## 二、可执行工程与微交互高工艺配方

### 1. 同心圆角与亮/暗双模式光影卡片
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
  background: var(--bg-surface);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.06),
    0 0 0 1px rgba(255, 255, 255, 0.08);
}
```

### 2. 锚点空间因果动效：日期选择 / 下拉菜单（非凭空闪现）
**要点**：以触发按钮边缘为 `transform-origin` 快速灵动展开（`180ms`），收起更快且零回弹（`130ms`），触发按钮保持 `data-open` 关联高亮，随时可打断且支持 `prefers-reduced-motion`。
```css
.date-trigger[data-open="true"] {
  background: var(--bg-subtle);
  border-color: var(--border-strong);
}

.date-popover {
  transform-origin: top left; /* 动态翻转贴边时同步切换为 top right / bottom left */
  opacity: 0;
  transform: translateY(-4px) scale(0.96);
  pointer-events: none;
  transition:
    transform 140ms cubic-bezier(0.4, 0, 1, 1),
    opacity 120ms cubic-bezier(0.4, 0, 1, 1);
}

.date-popover[data-open="true"] {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
  transition:
    transform 190ms cubic-bezier(0.2, 0.9, 0.25, 1),
    opacity 140ms cubic-bezier(0.2, 0, 0, 1);
}

@media (prefers-reduced-motion: reduce) {
  .date-popover, .date-popover[data-open="true"] {
    transform: none;
    transition: opacity 100ms linear;
  }
}
```

### 3. 锁宽防跳动 + 原地 Loading 按钮
```css
.btn-primary {
  display: inline-grid;
  place-items: center;
  min-height: 40px;
  padding: 0 16px;
  border: 0;
  border-radius: 8px;
  background: var(--accent-primary);
  color: var(--text-on-accent);
  font-weight: 500;
  transition: background-color 150ms cubic-bezier(0.2, 0, 0, 1),
              transform 90ms cubic-bezier(0.2, 0, 0, 1);
}
.btn-primary > * { grid-area: 1 / 1; } /* 切 Loading 宽度绝对不抖动 */
@media (hover: hover) and (pointer: fine) {
  .btn-primary:hover:not(:disabled) { background: var(--accent-primary-hover); }
}
.btn-primary:active:not(:disabled) { transform: scale(0.98); }
.btn-primary:focus-visible { outline: 2px solid var(--border-focus); outline-offset: 2px; }
```

### 4. 滚动触发的顶栏边界衔接 + 底部安全留白
```css
.page-header {
  position: sticky;
  top: 0;
  z-index: 20;
  background: var(--bg-canvas);
  border-bottom: 1px solid transparent;
  transition: border-color 160ms ease, background-color 160ms ease;
}
.page-header[data-scrolled="true"] {
  border-bottom-color: var(--border-subtle); /* 静止无缝，滚动后平滑浮现清晰 1px 细线 */
}
.page-scroll-content {
  padding-bottom: calc(var(--bottom-nav-height, 56px) + env(safe-area-inset-bottom) + 16px);
}
```

### 5. 不硬切文字的平滑展开折叠（Grid Row Transition）
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
  transition: opacity 130ms ease;
}
.disclosure-panel[data-open="true"] .disclosure-inner {
  opacity: 1;
  transition-delay: 50ms;
}
```

### 6. 数据与列表精排（替代多余卡片网格）
```css
.metric-row {
  display: grid;
  grid-template-columns: 32px minmax(0, 1fr) auto;
  align-items: center;
  gap: 12px;
  min-height: 52px;
  padding: 10px 16px;
  border-bottom: 1px solid var(--border-subtle);
}
.metric-value {
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
  font-weight: 600;
}
```

### 7. 干净商业级界面文案范例
- **页头**：`收藏`（直接展示内容与 `新建收藏夹`，零冗余副标题）
- **按钮**：`添加物品` / `保存修改` / `导出 CSV` / `选择日期` / `归档项目`
- **诚实报错**：`网络连接中断，修改尚未同步。重新连接后可再次同步。` + `[重试同步]`
- **乐观撤销**：`已归档《Q4 预算表》` + `[撤销]`（5 秒后落盘持久化）
- **微信小程序胶囊避让**：
  ```js
  const { statusBarHeight, screenWidth } = wx.getWindowInfo();
  const capsule = wx.getMenuButtonBoundingClientRect();
  const navBarHeight = capsule.height + (capsule.top - statusBarHeight) * 2;
  const rightSafeInset = screenWidth - capsule.left + 8;
  ```

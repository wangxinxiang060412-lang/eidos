# Platform Specification: Android (Material Design 3 Expressive)

参考标准：Google **Material Design 3** 与 **M3 Expressive** 动效物理体系、Android Edge-to-Edge 及 Jetpack Compose 工程规范。严禁生搬 iOS 的左上角返回风格或毛玻璃拟态覆盖 Android 习惯。

---

## 1. Material 3 Expressive 视觉与动态色彩

1. **表面色阶层次（Tonal Surface Elevation）**：M3 通过 5 级表面色阶（`surfaceContainerLowest` → `surfaceContainerLow` → `surfaceContainer` → `surfaceContainerHigh` → `surfaceContainerHighest`）而非厚重黑阴影来区分层次，亮/暗主题均清晰干净。
2. **动态色彩（Dynamic Color）兼容**：若品牌允许，支持 Android 12+ Material You 壁纸取色，同时为品牌固定色产品提供完整映射的 `ColorScheme`（Primary / Secondary / Tertiary / Error 及其 `on*`、`*Container`、`on*Container` 语义对），确保全组合对比度达标。
3. **形状系统（Shape Scale）**：利用有节奏的圆角层级（Extra Small `4dp` → Small `8dp` → Medium `12dp` → Large `16dp` → Extra Large `28dp` / Full）区分控件性格，绝不把所有元素统一套死一个圆角。

---

## 2. M3 Expressive 弹簧物理动效

M3 Expressive 弃用僵硬单一的时长曲线，转为**空间（Spatial）与效果（Effects）分离的弹簧物理令牌**（Jetpack Compose `MaterialTheme.motionScheme` 原生支持）：

- **Spatial Springs（位移、尺寸、共享元素、Sheet 展开）**：分 `fast / default / slow` 三档，带自然弹性与速度承接。
- **Effects Springs（颜色、透明度、背景高亮）**：临界阻尼（无回弹），快速干净。
- **预测性返回（Predictive Back）**：完整支持系统手势边缘滑回预览动画，退栈、关闭 Bottom Sheet 与关闭搜索框均能跟手预览并可中途反悔取消。

---

## 3. 导航、触控与 Edge-to-Edge 适配

- **最小触控目标**：所有交互控件 **≥ 48×48 dp**（含最小 8dp 间距防误触）；Compose 中确保视觉小图标组件保持 `minimumInteractiveComponentSize()`。
- **Edge-to-Edge 全面屏强制规范**：应用内容完整延伸至状态栏与手势导航栏背后（`enableEdgeToEdge()`），通过 `WindowInsets.safeDrawing` / `statusBars` / `navigationBars` / `ime` 为内容和底部操作条添加动态内边距，绝不留黑条或硬编码系统栏高。
- **自适应导航（Window Size Classes）**：
  - Compact（手机）：底部 Navigation Bar（3–5 项）+ 可选 FAB（仅 1 个本页最核心新建/主动作）。
  - Medium（折叠屏/竖屏平板）：左侧 Navigation Rail。
  - Expanded（横屏平板/ChromeOS）：永久 Navigation Drawer + List-Detail 规范双栏。
- **排版与辅助功能**：字号一律用 `sp` 单位以响应系统字体缩放；支持 TalkBack 语义合并（`Modifier.semantics(mergeDescendants = true)`）与系统动画缩放因子（`ANIMATOR_DURATION_SCALE`）。
- **工程优先 Jetpack Compose**：列表强制使用 `LazyColumn` / `LazyRow` + 稳定 `key` 防重组抖动，避免在 Composable 内做同步重计算。

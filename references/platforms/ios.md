# Platform Specification: iOS & iPadOS (Apple HIG / iOS 26)

参考标准：Apple Human Interface Guidelines（含 iOS / iPadOS 26 **Liquid Glass** 设计语言、Hierarchy / Harmony / Consistency 三支柱）。严禁把 Android 风格或 Web 网页思维硬塞进 iOS 原生应用。

---

## 1. iOS 26 Liquid Glass 材质铁律

1. **严格限定在导航与浮动控制层**：Liquid Glass（`.glassEffect()` / `GlassEffectContainer`）仅用于悬浮在核心内容之上的 **Tab Bar、Navigation Bar、Toolbar、浮动搜索岛、浮动控制按钮与半屏 Modal Sheet**。
2. **严禁涂抹在正文内容上**：列表行、文章卡片、表单输入框、数据表格必须保持清晰的不透明表面；把内容做成玻璃会毁掉层次与可读性。
3. **材质变体选型**：
   - `.regular`（默认）：常规工具栏、悬浮导航栏、主要悬浮控件。
   - `.clear`：仅限覆盖在视频/照片/地图之上的极小浮动按钮，且下方必须加轻微压暗保护层（Dimming Scrim）以保住 ≥ 4.5:1 对比度。
   - **系统辅助回退**：必须尊重“降低透明度（Reduce Transparency）”与“增加对比度（Increase Contrast）”系统设置。

---

## 2. 导航、布局与手势惯例

- **底部悬浮 Tab Bar（iPhone）**：3–5 个一级入口，采用内缩悬浮胶囊形态或原生 `TabView`；搜索入口可作为独立紧凑悬浮圆岛贴近单手可达区。严禁塞入 6 个以上 Tab 或把返回操作放底栏。
- **iPadOS 自适应导航**：严禁把 iPhone 底栏直接拉宽！宽屏下切换为可收起左侧 Sidebar + 顶部可浮动 Tab 切换 + `NavigationSplitView` 多栏布局，支持 Stage Manager、Split View 与指针悬停态（`.hoverEffect()`）。
- **返回与手势**：全面保留屏幕左边缘右滑返回（Interactive Pop Gesture），绝不随意覆盖系统边缘手势；大标题（Large Title）随滚动自然收起为紧凑导航栏。
- **Sheet 与大圆角**：临时任务优先使用可拖拽高度的 Sheet（`.presentationDetents([.medium, .large])`）；半屏态内缩透出后方上下文，展开至全屏时自然过渡为高不透明度聚焦态；绝不把抓手或标题画到状态栏/灵动岛下方。

---

## 3. 尺寸、字体、图标与触觉规范

- **最小点击热区**：所有交互控件 **≥ 44×44 pt**（视觉图标更小时扩展 `.contentShape(Rectangle())` 或内边距）。
- **安全区（Safe Area）**：动态适配灵动岛（Dynamic Island）、状态栏、圆角屏幕与 Home Indicator，绝不硬编码高度。
- **排版与 Dynamic Type**：优先使用系统 SF Pro（中文自动回落苹方 PingFang SC）语义字阶（`.largeTitle`, `.title2`, `.headline`, `.body`, `.subheadline`, `.footnote`, `.caption`），确保在辅助大字号下自适应换行或横转纵，不截断关键文案。
- **图标**：首选 **SF Symbols**（保持统一变体与渲染模式，与邻近字重和字号光学匹配）。
- **触觉反馈**：使用 `UIImpactFeedbackGenerator` / `UISelectionFeedbackGenerator` / `UINotificationFeedbackGenerator`（SwiftUI `.sensoryFeedback`），严格按事件语义克制触发。
- **原生实现优先**：优先使用 SwiftUI / UIKit 原生组件以自动获得 Liquid Glass、动态字号、VoiceOver 与平滑弹簧动效，避免手绘假冒系统控件。

# Performance & Runtime Smoothness

再精致的视觉与动效，如果首屏慢、滚动掉帧、点按钮迟滞或吃光手机电量，在真实产品中都属于不合格交付。**核心纪律：先测量定位瓶颈，再针对性优化，拒绝凭想象做过度抽象的“伪优化”。**

---

## 1. 目标平台性能基准线

### Web 应用（Google Core Web Vitals 75th Percentile 基准）
| 指标 | 衡量维度 | 优秀（目标） | 需改进 | 不合格 |
|---|---|---|---|---|
| **LCP** (Largest Contentful Paint) | 首屏主内容渲染速度 | **≤ 2.5s** | 2.5s–4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | 点击/敲击/输入响应延迟 | **≤ 200ms** | 200ms–500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | 视觉布局稳定性（防跳动） | **≤ 0.1** | 0.1–0.25 | > 0.25 |

### 原生 App / 桌面 / 游戏帧时间预算
- **60fps 设备**：单帧主线程 + 渲染总预算 **≤ 16.6ms**。
- **120Hz ProMotion / 高刷屏**：单帧预算 **≤ 8.3ms**。
- **游戏 UI / HUD 预算**：UI 渲染通常仅占总帧耗时的 **5–10%**，避免每帧触发全 Canvas 重建（Unity Dirty Rebuild / Unreal Tick 绑定）。

---

## 2. 高频体验瓶颈与标准解法

| 瓶颈场景 | 典型元凶 | 生产级工程解法 |
|---|---|---|
| **首屏慢 / 白屏久** | 巨型同步 JS Bundle、未压缩大图、阻塞渲染的外部字体 | 路由/重型模块懒加载（Code Splitting）；首屏关键图片 `fetchpriority="high"` + WebP/AVIF + 明确 `width/height`；字体 `font-display: swap` + 子集化 |
| **点击卡顿（INP 差）** | 点击事件里同步遍历大数组、整页同步重渲染、主线程长任务 >50ms | 输入/切换拆分为紧急态与非紧急渲染（`startTransition` / 防抖搜索）；避免在渲染路径做深拷贝或 O(N²) 过滤 |
| **滚动掉帧 / 大列表卡死** | 一次性挂载 500+ 复杂 DOM/视图节点、滚动时重算阴影与模糊 | 列表超 ~100–200 项采用**虚拟列表（Virtualization）**（TanStack Virtual / `LazyVStack` / `LazyColumn` / `RecyclerView`）；滚动列表项内禁用重型 `backdrop-filter` |
| **动画掉帧与撕裂** | 对 `width/height/top/left/box-shadow` 直接做逐帧动画 | 仅动画 GPU 合成层属性（`transform`、`opacity`）；严禁全局滥用 `will-change`（仅对正在运动的极少数元素短时启用，防显存爆掉） |
| **布局跳动（CLS 差）** | 无尺寸图片、延迟插入的横幅、Web 字体切换抖动、加载后按钮缩宽 | 所有媒体声明 `aspect-ratio`；异步区块预留等高骨架；按钮 Loading 态锁定最小宽 |
| **内存泄漏与发热耗电** | 无限轮询、离屏还在跑的 CSS/rAF 动画、未释放大图与监听器 | 后台/切标签页/离屏时暂停动画与轮询（`Page Visibility API` / `IntersectionObserver`）；严格清理监听器、Observer 与图片缓存 |
| **网络请求雪崩** | 列表每行各发一次请求（N+1）、切 Tab 重复全量拉取 | 请求聚合/缓存（SWR/React Query 合理 `staleTime`）；列表分页或游标增量加载；搜索框 250–300ms 防抖 + `AbortController` |

---

## 3. 低端设备优雅降级策略

- **材质降级**：检测到低端 GPU、省电模式或用户开启“减少透明度”时，将实时高斯模糊/玻璃折射无缝回退为高对比半透明或纯色表面。
- **动效降级**：在 `prefers-reduced-motion` 或低帧率设备上关闭复杂粒子、3D 视差与多元素交错动画，保留即时清晰的状态切换。
- **图片降级**：使用响应式 `srcset` / 缩略图 CDN 参数按实际显示像素拉图（切忌给 48px 头像加载 4000px 原图）。

---

## 4. 验证方法（不靠猜）

- Web：Chrome DevTools Performance 面板录制交互帧率 + Lighthouse / Playwright 测 LCP/CLS/INP + Network 检查请求瀑布与资源体积。
- iOS：Xcode Instruments（Time Profiler / Core Animation FPS / Allocations）。
- Android：Android Studio Profiler + JankStats / Macrobenchmark。
- 游戏：Unity Profiler（Canvas.BuildBatch / UI.Render）/ Unreal Insights + Slate Widget Reflector。

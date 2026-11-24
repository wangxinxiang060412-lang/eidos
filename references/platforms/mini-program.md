# Platform Specification: WeChat & Super-App Mini Programs

参考标准：微信小程序官方设计指南（WeChat Mini Program Design Guidelines）与 WeUI / TDesign 交互惯例（同样适用于支付宝/抖音等带右上角胶囊的超级 App 小程序）。

---

## 1. 顶部导航栏与胶囊按钮硬性避让规则

右上角系统胶囊按钮（`…` 更多 + `◎` 退出）由宿主平台强制渲染，**开发者无法移动、缩放或隐藏它**。

1. **优先使用原生默认导航栏**：常规业务页直接使用系统托管导航栏（配置 `navigationBarBackgroundColor` 与 `black/white` 文字极性），启动最快、返回行为最稳定。
2. **自定义导航栏（`navigationStyle: "custom"`）动态计算铁律**：
   - 严禁硬编码顶部高度（如写死 `88px`），必须运行时读取 `wx.getWindowInfo().statusBarHeight` 与 `wx.getMenuButtonBoundingClientRect()`：
     - 胶囊上边距 = `menuButton.top - statusBarHeight`
     - 导航栏内容高 = `menuButton.height + (menuButton.top - statusBarHeight) * 2`
     - 左侧自定义返回/搜索控件的垂直中心必须与胶囊垂直中心对齐，右侧预留 `screenWidth - menuButton.left + 8px` 避让安全区，**严禁任何可点击控件、搜索框或标题文字撞进胶囊区**。
   - 根据顶部背景深浅同步配置浅色或深色胶囊极性。
3. **无历史栈兜底**：用户通过微信好友卡片、朋友圈或扫码直达二级/三级详情页（页面栈深度 = 1）时，自定义导航栏左上角必须自动由“返回箭头”切换为“回首页图标”，严禁点返回毫无反应。

---

## 2. 尺寸适配、排版与触控规范

- **响应式单位策略**：以 `750rpx` 为标准基准做弹性布局，但注意**正文排版、精细描边与超宽屏（平板/PC 微信小窗）**：关键文字避免在 iPad/桌面微信里随 `rpx` 被无限拉成巨无霸，重要排版或高精布局结合 `px` + Flex/Grid + 最大宽约束。
- **字号与行高**：遵循宿主系统字体（iOS PingFang SC / Android Roboto·思源黑体）；推荐层级：页面大标题 `18–20pt`、正文 `14–16pt`（`28–32rpx`）、次要辅助 `12–13pt`（`24–26rpx`）、极小脚标不低于 `11pt`（`22rpx`）；中文正文行高 `1.45–1.6`。
- **触控热区**：按钮与可点图标热区 **≥ 44×44 pt**（`88×88 rpx`）；列表项整行均可响应点击，点击态（`hover-class`）即时响应不拖泥带水。
- **底部安全区**：固定底栏、提交订单条、自定义 Tab Bar 必须叠加 `padding-bottom: env(safe-area-inset-bottom)`，背景铺满至屏幕最底端。

---

## 3. 小程序特有产品体验与性能规范

1. **即用即走，克制登录拦截**：遵循微信平台规范，**禁止一打开小程序未展示核心内容就强弹登录/手机号授权弹窗**！允许游客先浏览首页与核心内容，仅在下单、收藏、提交等真正需要身份的瞬间触发授权。
2. **原生组件与交互习惯**：底部 Tab Bar 严格控制在 **2–5 项**；高频确认、地址/日期/规格选择优先采用符合微信习惯的底部半屏弹层（ActionSheet / Bottom Sheet）或原生 Picker。
3. **包体积与渲染性能**：
   - 控制主包体积（严控 ≤ 2MB 上限），非首屏二级业务拆分分包（Subpackages）并按需注入。
   - **最小化 `setData` 负载**：禁止每帧或滚动回调里把大数组整包丢给 `setData`；仅做局部路径更新（如 `setData({ ['list[' + idx + '].checked']: true })`），避免通信通道堵塞造成掉帧。
   - 图片启用懒加载（`lazy-load`）+ CDN 裁剪压缩 + 固定占位尺寸防跳动。

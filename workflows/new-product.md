# Workflow: New Product (0 → 1 Design & Engineering)

适用场景：从零构思、设计并完整实现一款新产品（App / Web / 小程序 / 桌面端 / 游戏 UI）。
**核心铁律：绝不跳过产品逻辑、信息架构与审美锁定直接堆页面代码。**

---

## Step 1：产品定义与任务边界（加载 `product-discovery.md`）
1. 明确目标用户、使用环境、核心定位与 Top 3 高频任务。
2. 确定目标平台与合理的技术栈（优先简洁可靠、贴合目标平台生态，不堆砌重依赖）。
3. 若产品复杂或用户需求尚未完全明确，使用 [design-brief.md](../templates/design-brief.md) 输出精炼产品简报并确认关键决策。

## Step 2：信息架构与核心流程（加载 `information-architecture.md` + `user-psychology.md`）
1. 将所有功能划分为 L1 / L2 / L3 / T（临时弹层）/ U（低频设置）。
2. 绘制核心任务主路径（高频任务控制在 1–3 次关键操作内可达）。
3. 明确每一屏唯一核心目标、导航形态、返回状态保留策略及必需的异常状态（空态、加载、错误、撤销）。

## Step 3：审美锁定与 Design System 建立（加载 `visual-design.md` + `design-system.md` + 目标平台文档）
1. 完成 `SKILL.md` 第 6 节的 **5 行审美与架构锁定**（选定 6 大原型之一或按用户品牌定制）。
2. 先建立统一 Design Tokens（颜色、文字阶梯、间距、同心圆角、柔和阴影、亮/暗主题、Motion Tokens，可基于 [design-tokens.json](../templates/design-tokens.json) 生成 CSS Variables / Theme 文件）。
3. 对照 [anti-ai-ui.md](../references/anti-ai-ui.md) 排除模板化陷阱（如无故紫蓝渐变、胶囊汤、嵌套卡片）。

## Step 4：关键页面、组件与交互动效规格（加载 `interaction-design.md` + `motion-design.md`）
1. 先搭建可复用基础原语（Button、Input、Dialog/Sheet、Toast、List Row/Card）并固化交互态与无障碍属性。
2. 对核心转场（弹层锚点、列表折叠、状态原地切换）按 [interaction-spec.md](../templates/interaction-spec.md) 明确起止与可打断规则。

## Step 5：真实功能工程实现（转入 `frontend-implementation.md`）
1. 实现全部页面与真实交互事件、数据持久化/接口对接、完整异常态与文案（参考 [ux-writing.md](../references/ux-writing.md)）。
2. 完成多端尺寸适配、安全区避让、暗黑模式与键盘/读屏无障碍。

## Step 6：真实运行与闭环验收（转入 `final-verification.md`）
1. 启动项目，实际走通核心任务流与异常态。
2. 在多宽度/亮暗模式下截图并检查动效连续性，逐条清理 P0/P1 与明显视觉瑕疵。
3. 再次运行验收并输出 [delivery-report.md](../templates/delivery-report.md)。

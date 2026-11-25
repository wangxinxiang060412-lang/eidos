# Workflow: Scoped Optimization, Redesign & Refinement (Stage 3–7)

适用场景：已有参考方案/部分设计稿深化（Stage 3–4）、半成品打磨与体验重构（Stage 5–6）或成熟产品局部精修（Stage 7）。
**核心铁律：严控修改边界，零功能回归，保留合理设计，未经确认绝不擅改整体配色。**

---

## Step 1：理解意图、锁定边界与权限确认
1. 若面对已有设计稿/参考图（Stage 3–4），先总结其核心视觉意图与值得保留的基因；若面对代码项目（Stage 5–7），先完成只读理解与改动前基线截图（Before）。
2. 划清三张清单：
   - **In Scope（本次修改）**：用户明确范围 + 确认的 P0/P1 问题 + 授权内的高杠杆体验与文案精修。
   - **Color Gate（配色权限检查）**：先执行 [color-review.md](../references/color-review.md)。现有配色合理则保留；若需调整整体配色或品牌主色且尚未获确认 → **先提交 [color-proposal.md](../templates/color-proposal.md)（含实景预览）等待确认，期间不擅自改色**。
   - **Do Not Touch（绝对禁区）**：无关页面、核心业务逻辑、数据库/接口契约、品牌核心 Slogan、法务/隐私声明及已合理的交互习惯。

## Step 2：优先高杠杆精修，拒绝无意义大重写
1. **复用既有技术栈与组件体系**：严禁借优化之名私自更换框架或引入重型第三方库。
2. **先修结构与减法，再修微调**：
   - 先解 P0/P1 功能、可用性、对比度与异常态闭环。
   - 对照 [anti-ai-ui.md](../references/anti-ai-ui.md) 与 [visual-refinement.md](../references/visual-refinement.md) 做外科减法（去多余边框/嵌套卡/装饰胶囊/废话副标题）与 20 项细节精修。
   - 按 [navigation-and-boundaries.md](../references/navigation-and-boundaries.md) 修好页面上下边界、滚动衔接与安全区。
   - 按 [motion-design.md](../references/motion-design.md) 为菜单/日期选择/弹窗补齐精确 `transform-origin`、空间因果与可打断退场。
   - 按 [ux-writing.md](../references/ux-writing.md) 扫描源码与本地化文件，清理模板化文案并保留全部插值变量、Key 与业务逻辑。

## Step 3：分批安全实施与回归保护
每完成一个模块修改，立即运行 typecheck / lint / 测试与构建，确保原有交互、路由参数与既有持久化数据零回归；若改了共享组件或 Token，抽查关联页面避免连带误伤。

## Step 4：前后视觉对比与负收益回退（转入 `final-verification.md`）
运行项目并采集修改后画面（After），与改动前（Before）并排对照：
- 确认每处改动均有真实、可感知的体验提升。
- 若某项调整未带来收益或反而使界面更乱/更慢，**立即撤销回退**，再重新验收集齐最终证据。

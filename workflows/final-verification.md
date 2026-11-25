# Workflow: Final Runtime Verification, Content Audit & Rollback Gate

适用场景：所有设计与开发任务交付前的强制闭环验收。
**核心铁律：绝不靠读代码宣称完工；存在 P0 一票否决；无收益或负收益改动必须主动回退。**

---

## Step 1：自动化工程门禁
1. 运行项目类型检查（`typecheck`）、静态检查（`lint`）、单元测试与生产构建（`build`）。
2. 确认运行控制台（Browser Console / Xcode / Logcat）无新增 Error、Hydration 错位或未捕获异常。

## Step 2：14 步真实运行与多维取证（加载 `visual-verification.md`）
启动真实应用，采集并**亲自核对**：
1. **全局与局部双尺度截图**：桌面宽屏（`1440×900`）+ 移动窄屏（`390×844` / `320px`）+ 深色模式（若支持），同时放大检查基线对齐、图标重心、同心圆角、边界衔接与安全区。
2. **真实点击与端到端闭环**：实点主入口、跳转返回保态、表单校验、持久化刷新、异常/空态/撤销恢复。
3. **动效与弹层过程核查**：通过录屏或 `50–80ms` 抽帧验证日期选择/菜单/弹窗/Sheet/折叠的锚点起止、无切字、无落位跳变、中途打断与 `prefers-reduced-motion`。

## Step 3：独立 Content Audit（加载 `ux-writing.md`）
逐项扫描全部用户可见文案（含二级页、弹窗、报错、空态与 `aria-label`）：
- 无 14 类模板化 AI 鸡汤文案、无冗余标题副标题
- 按钮动词准确可预测、高危操作写明精确后果
- 报错与反馈 100% 匹配真实程序状态（绝不虚构已保存/已同步）
- 跨页面术语一致、无文案撑爆/异常折行、未擅改品牌 Slogan 与法务文本

## Step 4：六清单交叉审查 + 20 项精修复核
以独立苛刻评审视角过检：
- [functional-checklist.md](../checklists/functional-checklist.md) · [ux-checklist.md](../checklists/ux-checklist.md) · [ui-checklist.md](../checklists/ui-checklist.md) · [motion-checklist.md](../checklists/motion-checklist.md) · [accessibility-checklist.md](../checklists/accessibility-checklist.md) · [release-checklist.md](../checklists/release-checklist.md)
- 同步对照 [visual-refinement.md](../references/visual-refinement.md) 捕捉可顺手解决的高影响力微调项。

## Step 5：前后对比、修复复测与负收益回退
1. 将修改后（After）与基线（Before）真实画面比对；**若某项改动无实际收益或体验下降，果断撤销回退**。
2. 按 `P0 → P1 → P2` 修复发现的问题；**每次视觉或交互改动后必须重新运行取证验证**。

## Step 6：输出诚实交付报告
按 [delivery-report.md](../templates/delivery-report.md) 汇总：交付概要、配色权限执行情况、已验证视口/动效/Content Audit 证据、前后对比与回退记录，以及 **`Not Checked`（未测项与复测方法）**。

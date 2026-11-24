# Workflow: Final Runtime & Visual Verification Loop

适用场景：所有设计与开发任务交付前的强制闭环验收。
**核心铁律：没有实际运行与画面取证，就不是验收通过；发现 P0 一票否决。**

---

## Step 1：自动化工程门禁
1. 运行项目类型检查（`typecheck`）、静态检查（`lint`）、单元测试与生产构建（`build`）。
2. 确认浏览器 Console / 原生 Logcat / Xcode Console 无新增运行时错误、Hydration 不匹配或未捕获 Promise 异常。

## Step 2：真实环境启动与多视口取证（加载 `visual-verification.md`）
启动真实应用，使用浏览器 / Playwright / iOS Simulator / Android Emulator / 微信开发者工具 / 游戏引擎采集并**亲自查看**以下画面：
1. **桌面/主视口静态与核心状态**（如 `1440×900`）
2. **窄屏/移动端视口**（如 `390×844` 及极端 `320px` 抽检，确认零横向滚动与热区可达）
3. **深色模式**（若支持：检查表面阶梯、对比度与顶边微光，不靠黑坨阴影）
4. **关键交互态与异常态**（空数据、加载态、校验错误、弹层打开、键盘 `:focus-visible` 焦点环）
5. **动效与转场过程**（通过录屏或 50–80ms 间隔抽帧检查：无边缘切字、无落位跳变、无锚点漂移、可中途打断、`prefers-reduced-motion` 正常退化）

## Step 3：独立新鲜视角六清单交叉核验
假设你是从未看过代码、最挑剔的产品评审，逐项核查（按任务按需读取对应清单）：
- [functional-checklist.md](../checklists/functional-checklist.md)（每个按钮真能用？数据真持久？无假反馈？）
- [ux-checklist.md](../checklists/ux-checklist.md)（首眼清晰？操作直觉？返回保态？）
- [ui-checklist.md](../checklists/ui-checklist.md)（无 AI 模板味？留白均衡？同心圆角？无近切边？）
- [motion-checklist.md](../checklists/motion-checklist.md)（有因果？不拖慢？可打断？）
- [accessibility-checklist.md](../checklists/accessibility-checklist.md)（WCAG 2.2 对比度、焦点、键盘、热区？）
- [release-checklist.md](../checklists/release-checklist.md)（零 P0？性能达标？诚实披露未验证项？）

## Step 4：修复 → 复测闭环
1. 按 `P0 → P1 → P2` 排序修复发现的所有实质问题。
2. **每一次视觉或交互修改后，必须重新截屏/跑通受影响流程验证**，禁止“修完最后一行代码直接盲目宣布通过”。

## Step 5：输出诚实交付报告
按 [delivery-report.md](../templates/delivery-report.md) 向用户汇报：
- 交付功能与设计要点
- 已实际运行并验证的设备/视口/状态及证据
- **`Not Checked` 清单**：如实写明因环境或外部依赖限制尚未实测的项及复测指南
- 明确的验收结论（通过 / 附条件通过 / 存在阻塞项未通过）

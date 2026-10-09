<div align="center">

<img src="https://raw.githubusercontent.com/Fzhenhong/Fzhenhong/main/assets/header.svg" width="900" alt="terminal header" />

<img src="https://raw.githubusercontent.com/Fzhenhong/Fzhenhong/main/assets/heatmap.svg" width="900" alt="contributions" />

<img src="https://raw.githubusercontent.com/Fzhenhong/Fzhenhong/main/assets/stack.svg" width="900" alt="stack" />

<img src="https://raw.githubusercontent.com/Fzhenhong/Fzhenhong/main/assets/metrics.svg" width="900" alt="metrics" />

</div>

<br/>

<h2></h2>

**SpireSage** · 《杀戮尖塔 2》全流程实时决策顾问 MOD

运行期只读解析战斗状态、评分候选、绘制推荐层。`affects_gameplay = false` —— 不写游戏字段、不改存档、不干预 RNG。

- **取数** — Harmony IL Patch + 反射只读双通道，`SceneTree.ProcessFrame` 轮询兜底，互为降级
- **评分** — 多腿加权：Dilution / DeckFit / PortCoverage / ComboRule / LineDef / TierOverrides，按职业独立知识库
- **验收** — `tools/golden` 离线宿主 + 700 行逐字基线 diff，约 95% 改动无需启动游戏

<br/>

| 仓库 | 说明 |
|:--|:--|
| **[SpireRouteAnalyzer](https://github.com/Fzhenhong/SpireRouteAnalyzer)** | 地图路线分析：精确路线计数、多列排序、悬停高亮、固定路线、缩放旋转视图 |
| **[agent2api](https://github.com/Fzhenhong/agent2api)** | 多提供商本地网关：把 6 个桌面端 App 的登录态转成本地 OpenAI 兼容 API |
| **[dsh-workbuddy-connect](https://github.com/Fzhenhong/dsh-workbuddy-connect)** | 桌面 App 内置模型接入本地 Harness，零配置 |
| **[QuickRestart](https://github.com/Fzhenhong/QuickRestart)** | 一键重开 |

<br/>

<sub>逆向 / 运行期补丁 / Godot + C#</sub>

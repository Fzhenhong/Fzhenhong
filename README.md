<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1220,35:1B3A5C,70:2E7D9A,100:38BDF8&height=190&section=header&text=%E5%A4%A7%E5%AE%8F&fontColor=ffffff&fontSize=52&fontAlignY=34&desc=Game%20Reverse%20Engineering%20%C2%B7%20MOD%20Systems%20%C2%B7%20C%23%20Runtime%20Patching&descAlignY=56&descSize=15&animation=fadeIn" width="100%" />

<a href="https://github.com/Fzhenhong">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=2600&pause=900&color=38BDF8&center=true&vCenter=true&width=760&height=45&lines=%E6%8A%8A%E9%BB%91%E7%9B%92%E6%8B%86%E6%88%90%E7%99%BD%E7%9B%92%EF%BC%8C%E5%86%8D%E6%8A%8A%E7%99%BD%E7%9B%92%E9%87%8D%E6%9E%84%E6%88%90%E7%B3%BB%E7%BB%9F%E3%80%82;%E3%80%8A%E6%9D%80%E6%88%AE%E5%B0%96%E5%A1%94%202%E3%80%8B%E5%AE%9E%E6%97%B6%E5%86%B3%E7%AD%96%E9%A1%BE%E9%97%AE%20MOD%20%E4%BD%9C%E8%80%85;Harmony%20IL%20Patch%20%C2%B7%20Godot%20Runtime%20%C2%B7%20%E9%9B%B6%E4%BE%B5%E5%85%A5%E5%8F%AA%E8%AF%BB%E6%9E%B6%E6%9E%84" alt="typing" />
</a>

<br/>

<a href="#-spiresage--%E6%A0%B8%E5%BF%83%E4%BD%9C%E5%93%81"><img src="https://img.shields.io/badge/C%23-.NET%209-512BD4?style=for-the-badge&logo=dotnet&logoColor=white" /></a>
<a href="#-spiresage--%E6%A0%B8%E5%BF%83%E4%BD%9C%E5%93%81"><img src="https://img.shields.io/badge/Godot-4.x-478CBF?style=for-the-badge&logo=godotengine&logoColor=white" /></a>
<a href="#-spiresage--%E6%A0%B8%E5%BF%83%E4%BD%9C%E5%93%81"><img src="https://img.shields.io/badge/Harmony-IL_Patch-7B42BC?style=for-the-badge" /></a>
<img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" />
<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" />

</div>

<br/>

## ⚔️ SpireSage — 核心作品

> **《杀戮尖塔 2》全流程实时决策顾问 MOD**
> 在游戏运行期只读解析战斗状态、评分候选、绘制推荐。**不写游戏字段、不改存档、不干预 RNG。**

<table>
<tr>
<td width="50%" valign="top">

**🧠 决策引擎**
多腿加权评分（Dilution / DeckFit / PortCoverage / ComboRule / LineDef / TierOverrides），按职业独立知识库。

**🔬 取数手段**
Harmony 运行期 IL 补丁 + 反射只读 + `SceneTree.ProcessFrame` 轮询，双通道互为兜底。

**🛡️ 安全边界**
`affects_gameplay = false`。自绘 UI 全部 `MouseFilter = Ignore`，零输入劫持。

</td>
<td width="50%" valign="top">

**🧪 离线优先验收**
`tools/golden` 离线宿主 + 700 行逐字基线 diff —— **约 95% 的改动无需启动游戏**即可验证。

**📐 证据纪律**
每条检查先证明它能拒绝坏输入；恒真的门禁等于没跑。

**🧩 工程约束**
单文件职责清晰 · 静默降级必须可计数 · 反射目标必须交叉核验。

</td>
</tr>
</table>

<br/>

## 🧰 武器库

<div align="center">

| 层 | 技术栈 |
|:--|:--|
| **语言** | `C# 12` · `TypeScript` · `Rust` · `Java` · `PowerShell` |
| **运行时** | `.NET 9` · `Godot 4.x` · `Node.js` |
| **逆向 / 注入** | `Harmony (IL Patch)` · `.NET Reflection` · `Assembly Editing` |
| **数据 / 构建** | `MSBuild` · `JSON Schema` · `GitHub Actions` |

</div>

<br/>

## 📊 数据画像

<div align="center">

<img height="180" src="https://github-readme-stats.vercel.app/api?username=Fzhenhong&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&bg_color=0B1220&title_color=38BDF8&icon_color=2E7D9A&text_color=C9D1D9&rank_icon=github" />
<img height="180" src="https://streak-stats.demolab.com?user=Fzhenhong&theme=tokyonight&hide_border=true&background=0B1220&stroke=1B3A5C&ring=38BDF8&fire=FF7A45&currStreakLabel=38BDF8&dates=C9D1D9&sideNums=C9D1D9" />

<br/><br/>

<img width="96%" src="https://github-readme-activity-graph.vercel.app/graph?username=Fzhenhong&bg_color=0B1220&color=38BDF8&line=2E7D9A&point=FF7A45&area=true&hide_border=true&custom_title=Contribution%20Timeline" />

<br/><br/>

<img width="58%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Fzhenhong&layout=compact&theme=tokyonight&hide_border=true&bg_color=0B1220&title_color=38BDF8&text_color=C9D1D9&langs_count=8" />

</div>

<br/>

## 🗂️ 项目索引

<div align="center">

<a href="https://github.com/Fzhenhong/SpireRouteAnalyzer">
  <img width="420" src="https://github-readme-stats.vercel.app/api/pin/?username=Fzhenhong&repo=SpireRouteAnalyzer&theme=tokyonight&hide_border=true&bg_color=0B1220&title_color=38BDF8&icon_color=2E7D9A&text_color=C9D1D9" />
</a>
<a href="https://github.com/Fzhenhong/agent2api">
  <img width="420" src="https://github-readme-stats.vercel.app/api/pin/?username=Fzhenhong&repo=agent2api&theme=tokyonight&hide_border=true&bg_color=0B1220&title_color=38BDF8&icon_color=2E7D9A&text_color=C9D1D9" />
</a>
<a href="https://github.com/Fzhenhong/dsh-workbuddy-connect">
  <img width="420" src="https://github-readme-stats.vercel.app/api/pin/?username=Fzhenhong&repo=dsh-workbuddy-connect&theme=tokyonight&hide_border=true&bg_color=0B1220&title_color=38BDF8&icon_color=2E7D9A&text_color=C9D1D9" />
</a>
<a href="https://github.com/Fzhenhong?tab=repositories">
  <img width="420" src="https://github-readme-stats.vercel.app/api/pin/?username=Fzhenhong&repo=QuickRestart&theme=tokyonight&hide_border=true&bg_color=0B1220&title_color=38BDF8&icon_color=2E7D9A&text_color=C9D1D9" />
</a>

</div>

<br/>

## 🐍 贡献蛇

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Fzhenhong/Fzhenhong/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Fzhenhong/Fzhenhong/output/github-snake.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/Fzhenhong/Fzhenhong/output/github-snake.svg" />
</picture>

</div>

<br/>

## 🧭 正在推进

```text
SpireSage            ██████████████████░░   实时决策顾问 · 离线验收体系收口
SpireRouteAnalyzer   █████████████░░░░░░░   路线计数 / 多列排序 / 旋转视图
agent2api            ████████░░░░░░░░░░░░   多提供商本地网关 · 登录态转 API
```

<br/>

<div align="center">

<sub>黑盒拆成白盒，白盒重构成系统。 · <b>Fzhenhong</b></sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:38BDF8,50:2E7D9A,100:0B1220&height=110&section=footer" width="100%" />

</div>

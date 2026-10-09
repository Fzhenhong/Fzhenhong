
import json, pathlib, collections
j = json.loads(pathlib.Path("_gql.json").read_text(encoding="utf-8"))
u = j["data"]["user"]
cal = u["contributionsCollection"]["contributionCalendar"]

# 聚合语言字节数（排除 fork，已由查询过滤）
agg = collections.Counter()
for repo in u["repositories"]["nodes"]:
    for e in repo["languages"]["edges"]:
        agg[e["node"]["name"]] += e["size"]
langs = [[k, v] for k, v in agg.most_common(7)]
# 技术栈标签：core=当前主线，active=在用，其余=会
stack_items = [
    ["C# 12", "core"], [".NET 9", "core"], ["Godot 4", "core"], ["Harmony", "core"],
    ["IL Patch", "active"], ["Reflection", "active"], ["TypeScript", "active"],
    ["Rust", "active"], ["PowerShell", "active"], ["Java", "plain"], ["GitHub Actions", "plain"],
]

def fmt(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)

data = {
    "user": "Fzhenhong",
    "name": "大宏",
    "tagline": "RE / runtime patching / godot+c#",
    "calendar": cal,
    "langs": langs,
    "stack": stack_items,
    "metrics": {
        "COMMITS": u["contributionsCollection"]["totalCommitContributions"],
        "CONTRIB": cal["totalContributions"],
        "REPOS": len(u["repositories"]["nodes"]),
        "STREAK": "—",
    },
}
pathlib.Path("gh_data.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
print("langs:", langs)
print("metrics:", data["metrics"])

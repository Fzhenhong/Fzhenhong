
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

def compute_streak(cal):
    """当前连续提交天数（末尾往前数）。"""
    days = [d for wk in cal["weeks"] for d in wk["contributionDays"]]
    n = 0
    for d in reversed(days):
        if d["contributionCount"] > 0:
            n += 1
        else:
            break
    return n

# 技术栈标签：core=当前主线，active=在用，其余=会
stack_items = [
    ["C# 12", "core"], [".NET 9", "core"], ["Godot 4", "core"], ["Harmony", "core"],
    ["IL Patch", "active"], ["Reflection", "active"], ["TypeScript", "active"],
    ["Rust", "active"], ["PowerShell", "active"], ["Java", "plain"], ["GitHub Actions", "plain"],
]

def fmt(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)

# ── 最近动态（REST /events）──
import json as _json, datetime as _dt
ev_raw = []
p_ev = pathlib.Path("_events.json")
if p_ev.exists():
    try:
        ev_raw = _json.loads(p_ev.read_text(encoding="utf-8"))
    except Exception:
        ev_raw = []

def rel_time(iso):
    try:
        t = _dt.datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=_dt.timezone.utc)
        delta = _dt.datetime.now(_dt.timezone.utc) - t
        sec = int(delta.total_seconds())
        if sec < 3600: return f"{max(sec//60,1)}m ago"
        if sec < 86400: return f"{sec//3600}h ago"
        return f"{sec//86400}d ago"
    except Exception:
        return ""

KIND = {
    "PushEvent": "push", "PullRequestEvent": "pr", "IssuesEvent": "issue",
    "CreateEvent": "create", "WatchEvent": "watch", "ForkEvent": "fork",
    "ReleaseEvent": "release", "IssueCommentEvent": "issue",
}
events = []
for e in ev_raw:
    k = KIND.get(e.get("type", ""))
    if not k:
        continue
    repo = e.get("repo", {}).get("name", "")
    payload = e.get("payload", {}) or {}
    if k == "push":
        # 注意：GitHub /events 的 PushEvent 已不再返回 commits/size，仅有 ref/before/head
        ref = (payload.get("ref") or "").replace("refs/heads/", "")
        desc = f"pushed to {ref}" if ref else "pushed"
    elif k == "pr":
        desc = f"PR {payload.get('action','')}: " + (payload.get("pull_request", {}) or {}).get("title", "")[:40]
    elif k == "issue":
        desc = f"issue {payload.get('action','')}"
    elif k == "create":
        desc = f"created {payload.get('ref_type','')}"
    elif k == "release":
        desc = "published release"
    else:
        desc = k
    events.append({"kind": k, "repo": repo, "desc": desc, "when": rel_time(e.get("created_at", ""))})

data = {
    "events": events[:6],
    "overview": {
        "OWN REPOS": len(u["repositories"]["nodes"]),
        "COMMITS": u["contributionsCollection"]["totalCommitContributions"],
        "CONTRIBUTIONS": cal["totalContributions"],
        "STREAK (days)": compute_streak(cal),
    },
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

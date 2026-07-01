# Health Rubric 评估报告：对比外部研究后的建议

> 日期：2026-06-30
> 评估人：Agent
> 基于：外部调研（学术论文、GitHub Stars Guide 2026、OSCHINA 质量分析、Awesome/LibHunt 策展实践）vs 当前 `docs/health-rubric.md` (v1)

---

## 一、外部研究的核心发现

| 指标 | 与项目质量相关性 | 当前 rubric 覆盖情况 |
|------|---------------|-------------------|
| 提交频率（30天） | **0.68**（强） | ✅ `maintenance` 的 `active_weeks_13` 已覆盖 |
| Issue 关闭率 | **0.71**（最强） | ⚠️ 已被**明确移除**（设计决定） |
| 测试覆盖率 | **0.63**（强） | ❌ 未覆盖（有意避免） |
| 贡献者数量 | 0.45（中等） | ✅ `governance` 的 `active_maintainers` + `top1_share` 已覆盖 |
| Star 数 | 0.32（弱） | ⚠️ `adoption` 不直接用 stars，用 `dependent_repos_count` + downloads |
| 代码复杂度（圈复杂度） | 未量化 | ❌ 未覆盖（有意避免） |
| 文档完整性 | 未量化 | ⚠️ `community/profile` 作为 bonus only |
| 依赖健康（CVE） | 未量化 | ❌ 明确移除（§2.6） |
| 组织多样性（多公司） | 未量化 | ⚠️ 已明确 DROP（§2.5） |
| Star 增长曲线（加速/减速） | 未量化 | ❌ 未覆盖 |

---

## 二、当前体系的设计取舍（正确且值得保持）

### 1. 纯 GitHub 元数据，不克隆仓库

当前体系仅用 `gh` CLI + `urllib`（纯 stdlib），不依赖 `git clone`、不下载代码、不运行静态分析工具。这保证了：
- 可大规模运行（~7-8 API calls/repo，5000/hr 预算内可跑 229 个项目）
- 零 pip 依赖，零环境配置
- 可复现、可自动化

**外部研究的测试覆盖率/代码复杂度/依赖 CVE 都需要克隆仓库或运行外部工具**，这会破坏体系的可操作性。**不建议加入。**

### 2. Issue 关闭率的移除（§2.2）

外部研究说关闭率是最强信号（0.71），但当前 rubric 明确将其移除。原因是：
- stale-bot 自动关闭无响应 issue 可以伪造高关闭率
- 关闭率与维护活跃度（maintenance）存在 double-count
- 首次响应时间（TTFR）更纯粹地反映"人是否在看"

**评估：这是一个正确的设计决定。** 关闭率作为 corroborating 信号可以保留在 raw/tooltip 中，但不应纳入 tier 逻辑。

### 3. CVE/依赖健康的移除（§2.6）

安全漏洞是 transient 状态（今天有 CVE-2026-1234，明天 patch 后消失），与许可（永久属性）不在同一时间尺度。纳入会制造大量噪声和误报。

**评估：正确。保持移除。**

### 4. 组织多样性的 DROP（§2.5）

`/users/{login}` 公司 enrichment 需要每个 repo 最多 20 个额外 API 调用，会触发 secondary rate limit。而且 commit share 本身已经捕捉了 bus factor 的核心信息。

**评估：正确。保持 DROP。**

---

## 三、建议的微调（不改动 tier 逻辑，只增强 corroborating 信号）

### 建议 1：在 `responsiveness` raw 中增加 issue 关闭率作为注释

不影响 tier（A/B/C/D/E），但写入 raw 字段供 tooltip/人类审阅参考：

```yaml
responsiveness:
  grade: B
  raw:
    median_ttfr_hours: 42
    qualifying_issues: 8
    close_rate_90d: 0.67   # NEW: corroborating only
```

**实现成本：** 同一 GraphQL query 中已返回 `closedAt`，只需计算比例，零额外 API call。
**风险：** 低。仅作为原始数据，不驱动 tier。

### 建议 2：在 `adoption` raw 中增加 star 增长趋势作为注释

GitHub Stars Guide 2026 指出："star 增长曲线比绝对数量更有意义"。当前体系只关注 dependents/downloads，完全不分析 stars。

虽然 stars 与质量相关性弱（0.32），但**star 增长趋势**（加速 vs 减速 vs 持平）可以识别 hype 驱动 vs 有机增长：

```yaml
adoption:
  grade: C
  raw:
    stars: 28813
    forks: 3218
    star_growth_90d: 12400   # NEW: 最近90天新增 stars
    star_growth_trend: accelerating  # NEW: accelerating | decelerating | flat
```

**实现成本：** 需要调用 `stargazers` 端点（分页获取，可能消耗较多 API budget），或作为可选的 enrich 步骤。
**风险：** 中等。可作为 `--enrich` 标志下的可选步骤，不纳入默认运行。

### 建议 3：在 `governance` 或 `maintenance` raw 中增加文档存在性作为注释

`community/profile` 已经返回 `files: [code_of_conduct, contributing, license, readme]`，当前只是 bonus annotation。可以将其写入 raw 作为结构化数据：

```yaml
governance:
  grade: C
  raw:
    active_maintainers_12mo: 1
    top1_share: 0.95
    community_files: [readme, license]  # NEW: from community/profile
```

**实现成本：** 同一 `community/profile` call 已获取，零额外成本。
**风险：** 极低。

---

## 四、不建议的改动

| 改动建议 | 不建议原因 |
|---------|-----------|
| 加入测试覆盖率 | 需要 clone 仓库 + 运行测试工具，破坏"纯远程"原则 |
| 加入代码复杂度（圈复杂度） | 同上，需要代码分析工具 |
| 加入 CVE/依赖漏洞扫描 | 时间尺度不匹配，会产生 transient noise |
| 加入组织多样性（多公司参与） | API 成本过高（每 repo 最多 20 个额外 call），已明确 DROP |
| 将 issue 关闭率纳入 tier 逻辑 | 会被 stale-bot 操纵，且与 maintenance double-count |
| 将 star 数直接纳入 adoption tier | stars 与质量相关性仅 0.32，且易受炒作驱动 |

---

## 五、结论

当前 `health-rubric.md` 的六轴设计**基本不需要结构性调整**。它是经过深思熟虑的，取舍非常清晰，且与外部研究的核心结论一致（提交频率、issue 响应、贡献者分散度是最有效的信号）。

**唯一值得做的增强是：**
1. 将 `close_rate_90d` 作为 `responsiveness` 的 corroborating 注释写入 raw（零额外 API cost）
2. 将 `community_files` 作为 `governance` 的结构化 raw 数据（零额外 API cost）
3. 将 `star_growth_90d` 作为可选的 `adoption` enrich 步骤（需要额外 API budget，标记为可选）

这些改动都不改变 tier 逻辑，只是给人类审阅者更多 corroborating 信号。如果要执行，建议以 `--enrich` 模式或 `--raw-fields` 扩展的方式加入，保持默认运行的轻量性。

---

## 六、附录：外部研究来源

1. OSCHINA (2026-04-30): "GitHub高质量开源项目筛选技巧" — 1000 JS 项目相关性分析
2. GitHub Stars Guide (2026-02-20): "Evaluating Open Source in 2026" — ToolJet 官方博客
3. Kalliamvakou et al. (2014): "The promises and perils of mining GitHub" — MSR 论文
4. Aggarwal et al. (2014): "Co-evolution of project documentation and popularity" — MSR 论文
5. Skogeby (2026): "Exploring subjectivity in ad hoc assessment of OSS" — 瑞典硕士论文
6. Automated GitHub Repository Classifier (chriscarrollsmith): AI 辅助批量评估实践

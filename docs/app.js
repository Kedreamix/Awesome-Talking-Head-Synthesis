const $ = (id) => document.getElementById(id);

const state = {
  papers: [],
  sections: [],
  visible: 50,
  lang: localStorage.getItem("catalog-language")
    || (navigator.language.toLowerCase().startsWith("zh") ? "zh" : "en"),
  generatedAt: "",
  stars: null,
  starHistory: [],
};

const REPO_API = "https://api.github.com/repos/Kedreamix/Awesome-Talking-Head-Synthesis";

const TRANSLATIONS = {
  en: {
    "nav.explore": "Explore papers",
    "nav.star": "Star",
    "hero.eyebrow": "Open research index",
    "hero.title1": "The evolving map of",
    "hero.title2": "Talking Head Synthesis",
    "hero.description": "Discover papers, implementations, datasets and project pages across audio-driven avatars, 3D heads, conversational agents and more.",
    "hero.browse": "Browse the collection",
    "hero.github": "Support us on GitHub",
    "stats.papers": "research papers",
    "stats.code": "open-source implementations",
    "stats.projects": "project pages",
    "stats.stars": "GitHub stars",
    "community.eyebrow": "Community curated",
    "community.title": "Know a paper we missed?",
    "community.description": "Recommend a new or missing paper through a short GitHub form. Include its title and link—we’ll review it for the next catalog update.",
    "community.loading": "Catalog update date loading…",
    "community.suggest": "Suggest a paper",
    "community.view": "View existing suggestions",
    "areas.eyebrow": "Research areas",
    "areas.title": "Browse by category",
    "areas.description": "See how the collection is organized. Select an area to explore its papers, or propose a new category for future updates.",
    "areas.suggest": "Suggest a new category",
    "catalog.eyebrow": "Explore the archive",
    "catalog.title": "Find your next paper",
    "catalog.description": "Search the full collection or narrow it by research area, year, and available resources.",
    "catalog.loading": "Loading collection…",
    "catalog.more": "Show more papers",
    "filters.search": "Search title, keyword, venue or arXiv ID…",
    "filters.allSections": "All research areas",
    "filters.allYears": "All years",
    "filters.newest": "Newest first",
    "filters.oldest": "Oldest first",
    "filters.titleSort": "Title A–Z",
    "filters.clear": "Clear filters",
    "links.code": "Code",
    "links.project": "Project",
    "links.data": "Data",
    "empty.title": "No matching papers",
    "empty.description": "Try a broader search or clear the filters.",
    "theme.light": "Switch to light mode",
    "theme.dark": "Switch to dark mode",
    "stars.tracking": "Tracking starts today",
    "stars.today": "today",
  },
  zh: {
    "nav.explore": "浏览论文",
    "nav.star": "点赞",
    "hero.eyebrow": "开放研究索引",
    "hero.title1": "持续演进的",
    "hero.title2": "Talking Head Synthesis",
    "hero.description": "探索音频驱动数字人、3D 头像、对话智能体等方向的论文、开源实现、数据集与项目主页。",
    "hero.browse": "浏览全部论文",
    "hero.github": "在 GitHub 上支持我们",
    "stats.papers": "收录研究论文",
    "stats.code": "开源代码实现",
    "stats.projects": "论文项目主页",
    "stats.stars": "GitHub 点赞",
    "community.eyebrow": "社区共同维护",
    "community.title": "发现遗漏的论文？",
    "community.description": "通过简短的 GitHub 表单推荐新论文或遗漏论文。提交标题和链接，我们会在下一次目录更新时审核。",
    "community.loading": "正在读取目录更新时间…",
    "community.suggest": "推荐一篇论文",
    "community.view": "查看已有推荐",
    "areas.eyebrow": "研究方向",
    "areas.title": "按类别浏览",
    "areas.description": "查看当前论文目录的分类方式。选择一个方向浏览相关论文，也可以为后续更新建议新的类别。",
    "areas.suggest": "建议新增类别",
    "catalog.eyebrow": "探索论文档案",
    "catalog.title": "找到你需要的论文",
    "catalog.description": "搜索完整论文目录，也可以按研究方向、年份和可用资源进一步筛选。",
    "catalog.loading": "正在加载论文目录…",
    "catalog.more": "显示更多论文",
    "filters.search": "搜索标题、关键词、会议或 arXiv ID…",
    "filters.allSections": "全部研究方向",
    "filters.allYears": "全部年份",
    "filters.newest": "最新优先",
    "filters.oldest": "最早优先",
    "filters.titleSort": "标题 A–Z",
    "filters.clear": "清除筛选",
    "links.code": "代码",
    "links.project": "主页",
    "links.data": "数据",
    "empty.title": "没有匹配的论文",
    "empty.description": "请尝试更宽泛的关键词或清除筛选条件。",
    "theme.light": "切换到浅色模式",
    "theme.dark": "切换到夜间模式",
    "stars.tracking": "今日开始记录",
    "stars.today": "今日",
  },
};

const SECTION_NAMES_ZH = {
  datasets: "数据集",
  survey: "综述",
  funny_work: "趣味工作",
  audio_driven: "音频驱动",
  portrait_animation: "肖像动画",
  text_driven: "文本驱动",
  nerf_3d: "NeRF 与 3D 头像",
  gaussian_splatting: "3D Gaussian Splatting",
  conversational: "对话与交互",
  talking_body: "全身数字人",
  robot_driven: "机器人面部与身体",
  metrics: "评测指标",
};

function t(key) {
  return TRANSLATIONS[state.lang]?.[key] || TRANSLATIONS.en[key] || key;
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function sectionName(slug, fallback = slug) {
  return state.lang === "zh" ? (SECTION_NAMES_ZH[slug] || fallback) : fallback;
}

function applyTranslations() {
  document.documentElement.lang = state.lang === "zh" ? "zh-CN" : "en";
  document.title = "Talking Head Synthesis";

  document.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(el.dataset.i18n);
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    el.placeholder = t(el.dataset.i18nPlaceholder);
  });
  document.querySelectorAll(".lang-option").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.lang === state.lang);
  });
  state.sections.forEach((section) => {
    const option = [...$("section").options].find((item) => item.value === section.slug);
    if (option) option.textContent = sectionName(section.slug, section.name);
  });
  updateThemeLabel();
}

function updateGeneratedText() {
  if (!state.generatedAt) return;
  $("generated").textContent = state.lang === "zh"
    ? `目录最近更新于 ${state.generatedAt}`
    : `Catalog last updated ${state.generatedAt}`;
}

function setLanguage(lang) {
  state.lang = lang;
  localStorage.setItem("catalog-language", lang);
  applyTranslations();
  updateGeneratedText();
  if (state.stars !== null) updateStarText(state.stars);
  else renderStarHistory();
  if (state.papers.length) {
    renderAreas();
    render();
  }
}

function updateThemeLabel() {
  const dark = document.documentElement.dataset.theme === "dark";
  $("theme-toggle").setAttribute("aria-label", dark ? t("theme.light") : t("theme.dark"));
}

function toggleTheme() {
  const current = document.documentElement.dataset.theme;
  const next = current === "dark" ? "light" : "dark";
  document.documentElement.dataset.theme = next;
  localStorage.setItem("catalog-theme", next);
  updateThemeLabel();
}

function renderAreas() {
  const counts = state.papers.reduce((result, paper) => {
    result[paper.section] = (result[paper.section] || 0) + 1;
    return result;
  }, {});

  $("area-grid").innerHTML = state.sections.map((section, index) => {
    const count = counts[section.slug] || 0;
    const countLabel = state.lang === "zh"
      ? `${count.toLocaleString()} 篇论文`
      : `${count.toLocaleString()} ${count === 1 ? "paper" : "papers"}`;
    return `<button class="area-card" type="button" data-section="${escapeHtml(section.slug)}">
      <span class="area-card__index">${String(index + 1).padStart(2, "0")}</span>
      <strong>${escapeHtml(sectionName(section.slug, section.name))}</strong>
      <span class="area-card__count">${countLabel}</span>
      <i aria-hidden="true">↗</i>
    </button>`;
  }).join("");

  document.querySelectorAll(".area-card").forEach((button) => {
    button.addEventListener("click", () => {
      $("section").value = button.dataset.section;
      state.visible = 50;
      render();
      $("explore").scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
}

function link(href, label, className) {
  if (!href) return "";
  return `<a class="${className}" href="${escapeHtml(href)}" target="_blank" rel="noopener noreferrer">${label}</a>`;
}

function matches(paper, filters) {
  if (filters.section && paper.section !== filters.section) return false;
  if (filters.year && String(paper.year) !== filters.year) return false;
  if (filters.hasCode && !paper.code) return false;
  if (filters.hasProject && !paper.project) return false;
  if (!filters.q) return true;

  const hay = [
    paper.title,
    paper.arxiv_id,
    paper.venue,
    paper.section_name,
    paper.description,
    ...(paper.keywords || []),
  ].join(" ").toLowerCase();
  return hay.includes(filters.q);
}

function readFilters() {
  return {
    q: $("q").value.trim().toLowerCase(),
    section: $("section").value,
    year: $("year").value,
    sort: $("sort").value,
    hasCode: $("has-code").checked,
    hasProject: $("has-project").checked,
  };
}

function paperTime(paper) {
  const published = Date.parse(paper.published_at || "");
  if (Number.isFinite(published)) return published;
  return Date.UTC(Number(paper.year) || 0, 0, 1);
}

function sortPapers(papers, mode) {
  return papers.sort((a, b) => {
    if (mode === "title") return a.title.localeCompare(b.title);

    const dateDiff = paperTime(b) - paperTime(a);
    if (dateDiff !== 0) return mode === "oldest" ? -dateDiff : dateDiff;

    const idDiff = (Number.parseFloat(b.arxiv_id) || 0) - (Number.parseFloat(a.arxiv_id) || 0);
    return mode === "oldest" ? -idDiff : idDiff;
  });
}

function render() {
  const filters = readFilters();
  const matchesAll = sortPapers(
    state.papers.filter((paper) => matches(paper, filters)),
    filters.sort
  );
  const rows = matchesAll.slice(0, state.visible);
  const hasFilters = filters.q || filters.section || filters.year || filters.hasCode || filters.hasProject;

  $("count").innerHTML = state.lang === "zh"
    ? `<strong>${matchesAll.length.toLocaleString()}</strong> 篇论文${hasFilters ? "符合当前筛选" : "收录于目录"}`
    : `<strong>${matchesAll.length.toLocaleString()}</strong> ${matchesAll.length === 1 ? "paper" : "papers"} found${hasFilters ? " for your filters" : " in the collection"}`;
  $("empty").hidden = matchesAll.length > 0;
  $("rows").hidden = matchesAll.length === 0;
  $("clear").hidden = !hasFilters;

  $("rows").innerHTML = rows.map((paper) => {
    const keywords = (paper.keywords || []).slice(0, 5).join(" · ");
    const links = [
      link(paper.code, t("links.code"), "chip chip--code"),
      link(paper.project, t("links.project"), "chip chip--project"),
      link(paper.download, t("links.data"), "chip chip--download"),
    ].filter(Boolean).join("");

    const title = paper.url
      ? `<a class="paper-title" href="${escapeHtml(paper.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(paper.title)}</a>`
      : `<span class="paper-title">${escapeHtml(paper.title)}</span>`;

    return `<article class="paper-card">
      <div class="paper-year">${escapeHtml(paper.year)}</div>
      <div>
        ${title}
        <div class="paper-meta">
          <span class="section-tag">${escapeHtml(sectionName(paper.section, paper.section_name))}</span>
          ${paper.venue ? `<span>${escapeHtml(paper.venue)}</span>` : ""}
          ${paper.arxiv_id ? `<span>arXiv:${escapeHtml(paper.arxiv_id)}</span>` : ""}
        </div>
        ${keywords ? `<span class="keywords">${escapeHtml(keywords)}</span>` : ""}
      </div>
      <div class="paper-links">${links}</div>
    </article>`;
  }).join("");

  const remaining = matchesAll.length - rows.length;
  $("load-more").hidden = remaining <= 0;
  $("load-more").textContent = remaining > 0
    ? (state.lang === "zh"
      ? `显示更多 · 还剩 ${remaining.toLocaleString()} 篇`
      : `Show more · ${remaining.toLocaleString()} remaining`)
    : t("catalog.more");
}

function fillSelect(id, values, labelFn = (v) => v) {
  const select = $(id);
  for (const value of values) {
    const opt = document.createElement("option");
    opt.value = value;
    opt.textContent = labelFn(value);
    select.appendChild(opt);
  }
}

function compactNumber(value) {
  return new Intl.NumberFormat(state.lang === "zh" ? "zh-CN" : "en", {
    notation: value >= 1000 ? "compact" : "standard",
    maximumFractionDigits: 1,
  }).format(value);
}

function updateStarText(stars) {
  state.stars = stars;
  $("star-stat").textContent = stars.toLocaleString(state.lang === "zh" ? "zh-CN" : "en-US");
  $("nav-star-count").textContent = compactNumber(stars);
  $("hero-star-count").textContent = compactNumber(stars);
  const label = state.lang === "zh"
    ? `${stars.toLocaleString("zh-CN")} 个 GitHub Star`
    : `${stars.toLocaleString("en-US")} GitHub stars`;
  $("nav-star-count").title = label;
  $("hero-star-count").title = label;
  renderStarHistory();
}

function renderStarHistory() {
  const history = [...state.starHistory].sort((a, b) => a.date.localeCompare(b.date));
  if (!history.length) {
    $("star-delta").textContent = "";
    return;
  }

  const today = new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Shanghai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(new Date());
  const current = state.stars ?? history[history.length - 1].stars;
  const previous = [...history].reverse().find((entry) => entry.date < today);

  if (previous) {
    const delta = current - previous.stars;
    const signed = `${delta >= 0 ? "+" : ""}${delta.toLocaleString()}`;
    $("star-delta").textContent = state.lang === "zh"
      ? `今日 ${signed}`
      : `${signed} today`;
  } else {
    $("star-delta").textContent = t("stars.tracking");
  }

  const chart = history.map((entry) => ({ ...entry }));
  const todayEntry = chart.find((entry) => entry.date === today);
  if (todayEntry) todayEntry.stars = current;
  else chart.push({ date: today, stars: current });

  if (chart.length < 2) {
    $("star-sparkline").hidden = true;
    return;
  }

  const visible = chart.slice(-30);
  const values = visible.map((entry) => entry.stars);
  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = Math.max(max - min, 1);
  const points = visible.map((entry, index) => {
    const x = visible.length === 1 ? 0 : (index / (visible.length - 1)) * 100;
    const y = 21 - ((entry.stars - min) / range) * 18;
    return `${x.toFixed(1)},${y.toFixed(1)}`;
  }).join(" ");
  $("star-sparkline-line").setAttribute("points", points);
  $("star-sparkline").hidden = false;
}

async function loadStarHistory() {
  try {
    const res = await fetch("./star-history.json");
    if (!res.ok) throw new Error(`Star history returned ${res.status}`);
    const data = await res.json();
    state.starHistory = Array.isArray(data.history) ? data.history : [];
    if (state.stars === null && state.starHistory.length) {
      updateStarText(state.starHistory[state.starHistory.length - 1].stars);
    } else {
      renderStarHistory();
    }
  } catch (err) {
    console.warn("Could not load star history", err);
  }
}

async function loadGithubStats() {
  try {
    const res = await fetch(REPO_API, {
      headers: { Accept: "application/vnd.github+json" },
    });
    if (!res.ok) throw new Error(`GitHub API returned ${res.status}`);
    const repo = await res.json();
    const stars = Number(repo.stargazers_count) || 0;
    updateStarText(stars);
  } catch (err) {
    if (state.stars === null) {
      $("star-stat").textContent = state.lang === "zh" ? "查看" : "View";
      $("nav-star-count").textContent = "↗";
      $("hero-star-count").textContent = "↗";
    }
    console.warn("Could not load GitHub stars", err);
  }
}

async function init() {
  const res = await fetch("./papers.json");
  const data = await res.json();
  state.papers = data.papers || [];
  state.sections = data.sections || [];
  state.generatedAt = data.generated_at || "";

  const withCode = state.papers.filter((p) => p.code).length;
  const withProject = state.papers.filter((p) => p.project).length;
  $("total-stat").textContent = data.count.toLocaleString();
  $("code-stat").textContent = withCode.toLocaleString();
  $("project-stat").textContent = withProject.toLocaleString();
  updateGeneratedText();

  fillSelect(
    "section",
    state.sections.map((s) => s.slug),
    (slug) => state.sections.find((s) => s.slug === slug)?.name || slug
  );
  fillSelect(
    "year",
    [...new Set(state.papers.map((p) => String(p.year)))].sort((a, b) => Number(b) - Number(a))
  );

  applyTranslations();
  renderAreas();
  $("filters").addEventListener("input", () => {
    state.visible = 50;
    render();
  });
  $("filters").addEventListener("change", () => {
    state.visible = 50;
    render();
  });
  $("clear").addEventListener("click", () => {
    $("filters").reset();
    state.visible = 50;
    render();
  });
  $("load-more").addEventListener("click", () => {
    state.visible += 50;
    render();
  });
  document.querySelectorAll(".lang-option").forEach((button) => {
    button.addEventListener("click", () => setLanguage(button.dataset.lang));
  });
  $("theme-toggle").addEventListener("click", toggleTheme);
  render();
  loadStarHistory();
  loadGithubStats();
}

init().catch((err) => {
  $("count").textContent = "Failed to load papers.json. Serve the docs/ folder over HTTP.";
  console.error(err);
});

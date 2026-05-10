---
name: weread-reading-note
description: Organize Markdown exported from a WeRead-to-Obsidian workflow into a structured reading note and reusable atomic notes with first-run path configuration and cross-book concept reuse. Use when the user asks to整理微信读书笔记, organize WeRead highlights, convert WeRead Obsidian exports, create book notes, generate atomic notes from book highlights, configure WeRead note paths, or connect concepts across books.
---

# WeRead Reading Note

Convert one WeRead export Markdown file into:

1. A structured reading note.
2. 5-12 atomic notes for reusable concepts, connected to existing notes across books.

This skill only reorganizes local Markdown files. It does not fetch, scrape, or bypass WeRead content.

## Operating Principle

Treat the Obsidian vault as a long-lived knowledge base, not a one-off export target. Before writing, confirm where the user's source and output folders live, read the existing note state, then update or connect existing knowledge whenever possible.

## Inputs

Ask for the source file if it is missing. Otherwise infer it from the user request.

Resolve paths in this order:

1. Paths explicitly provided in the user request.
2. `weread-reading-note.config.yaml` in the current vault root.
3. `.weread-reading-note.yaml` in the current vault root.
4. Built-in defaults below, but only after user confirmation.

## First-Run Configuration Gate

Installing this skill does not automatically ask the user for paths. The first skill run must handle configuration.

If no source file is given and no config file exists, stop before reading or writing files and ask the user for all required folders:

- WeRead sync folder for source Markdown files.
- Reading note output folder.
- Atomic note output folder.
- Cover image output folder, if cover download is needed.

Do not silently create or write to `WeRead Exports`, `Reading Notes`, `Atomic Notes`, or `assets/book-covers`. Present them only as suggested defaults.

After the user provides folder paths, create or update `weread-reading-note.config.yaml` in the vault root unless the user explicitly says not to. Use paths relative to the vault root when practical.

If the user gives a source file but no output folders and no config exists, infer `input_dir` from the source file path, then ask where to save:

- The structured reading note.
- The atomic notes.
- Cover images, if needed.

Built-in suggested defaults:

```yaml
input_dir: WeRead Exports
reading_note_dir: Reading Notes
atomic_note_dir: Atomic Notes
image_dir: assets/book-covers
```

Expected source pattern:

```text
<input_dir>/<book title>.md
```

The input usually contains frontmatter, a metadata section, `# 高亮划线`, optional `# 读书笔记`, and optional `# 本书评论`.

## Workflow

1. Resolve or collect required paths using the First-Run Configuration Gate.
2. Read the source Markdown.
3. Parse book metadata from frontmatter and `# 元数据`.
4. Parse every highlight from `> 📌 <text>` and attach it to the nearest preceding chapter heading.
5. Parse comments from `💭 <comment>` and attach each comment to the nearest preceding highlight.
6. Extract overall reviews from `# 本书评论`, if present.
7. Read existing reading notes and atomic notes before planning new atomic notes.
8. Write the reading note using `references/output-templates.md`.
9. Audit existing atomic notes before creating new ones. Reuse or update overlapping concepts across books.
10. Generate 5-12 atomic note links using the concept rules below.
11. If an atomic note already exists, update it append-only. Never overwrite the user's reflection section.
12. Run the checklist before responding.

For parsing edge cases, read `references/parsing-notes.md`.

## Reading Note Output

Path:

```text
<reading_note_dir>/《<book title>》读书笔记.md
```

Use the template in `references/output-templates.md`.

Required sections:

- 书籍信息
- 高亮划线
- 读书笔记
- 整体评论
- 语义卡
- 写作切入点

Rules:

- Keep all highlights in `高亮划线`.
- In `读书笔记`, include only highlights that have user comments. Do not repeat pure highlights there.
- If there are no user comments, keep the section and write: `（这本书我没写笔记，纯划线。）`
- If there is no overall review, keep the section and write: `（我还没写。读完之后回来补。）`
- Keep chapter order. If the same chapter appears multiple times, merge into the first occurrence and append later highlights in source order.

## Atomic Note Output

Path:

```text
<atomic_note_dir>/<concept name>.md
```

Generate 5-12 notes. Do not exceed 15.

Category must be one of:

- `概念`: a reusable noun or idea.
- `心法`: an attitude, stance, or way of living.
- `方法`: an actionable practice.

Prefer concepts in this order:

1. Concepts behind highlights that have user comments.
2. Keywords repeated in overall reviews.
3. Chapter-level themes or central claims.
4. One-off highlights only when they have strong reusable value.

## Before Creating New Files

Before creating a reading note or atomic note:

- Confirm the target directory came from the user, a config file, or explicit confirmation of the suggested default.
- Check whether the target reading note already exists. If it exists, replace only if the configured or user-specified policy allows it.
- Check whether each candidate atomic concept already exists by exact name, alias-like phrasing, related concepts, sources, and reading-note links.
- Prefer updating or linking an existing concept over creating a new file.
- Create a new atomic note only when the concept is meaningfully distinct and would remain useful across future books.

## Cross-Book Concept Audit

Before creating any new atomic note, scan `<atomic_note_dir>` and the reading notes already in `<reading_note_dir>`.

For every candidate concept, check for:

- Same or near-same concept under a different name.
- Broader/narrower versions of the same idea.
- Same practice expressed in another domain, such as learning, investing, parenting, or existential reflection.
- Same user concern appearing across books, especially recurring words in comments and reviews.

If a matching note exists, prefer updating that existing note instead of creating a new one. Add the new book to:

- frontmatter `sources`
- `## 从哪本书来`
- `## 关联原文`
- `## 相关概念`
- `## 写作切入口`

Then link that existing note in the new reading note's `语义卡` section.

Create a new atomic note only when the new concept is meaningfully distinct, not merely a different phrasing or domain example.

Examples of overlap that should usually be merged or cross-linked:

- `深度学习` and `融会贯通`: both concern turning isolated knowledge into a usable system.
- `费曼式育儿` and `五个W沟通法`: both concern explaining clearly, especially the `why`, in parent-child communication.
- `元认知` and `双轨分析`: both concern observing one's own thinking and psychological bias while judging reality.
- `长远目光`, `每天聪明一点`, and `耐心等待好赔率`: all concern patience, long-term compounding, and resisting short-term impulse.
- `开放而不极端` should connect to notes about open-minded parenting, ideology, and avoiding rigid certainty.

When two notes overlap but should remain separate, add explicit bidirectional links in `## 相关概念` and explain the distinction in one sentence. For example: `[[深度学习]]` focuses on the learning process; `[[融会贯通]]` focuses on the resulting knowledge structure.

## Existing Atomic Notes

If `<atomic_note_dir>/<concept name>.md` exists, do not overwrite the file.

Append or update only:

- frontmatter `sources`
- frontmatter `related`
- frontmatter `tags`
- frontmatter `updated`
- `## 从哪本书来`
- `## 关联原文`
- `## 相关概念`
- `## 写作切入口`

Never modify:

- frontmatter `status`
- frontmatter `category`
- frontmatter `created`
- `## 一句话`
- `## 我的理解`

If the new book adds an angle that conflicts with the existing `## 一句话`, add an HTML comment above frontmatter explaining the mismatch and leave the old text intact.

## Style

- Write concise Chinese by default, unless the user requests another language.
- Avoid generic AI summary language.
- Do not invent personal opinions for the user.
- Short writing angles are fine. Do not add target-audience or marketing-persona blocks unless the user asks for them.
- Avoid decorative emoji in generated notes, except where the user's source text already contains it.
- Avoid long copyrighted quotations in public examples.

## Final Checklist

- Required input and output paths were resolved from explicit user input or a config file.
- Suggested default paths were not used silently on a first run.
- `weread-reading-note.config.yaml` was created or updated after first-run path selection, unless the user declined.
- The reading note has all required sections.
- The reading note has a table of contents callout near the top.
- Highlight comments are not duplicated as pure highlights.
- The `读书笔记` section only contains commented highlights.
- Atomic note links in the reading note match actual files.
- Concepts were checked against existing atomic notes before new notes were created.
- Overlapping concepts across books were merged into existing notes or explicitly cross-linked.
- Existing atomic notes were updated append-only.
- `## 我的理解` was not changed in existing atomic notes.
- No real copyrighted sample text was introduced into repository examples.

---
name: weread-reading-note
description: Organize Markdown exported from a WeRead-to-Obsidian workflow into a structured reading note and reusable atomic notes. Use when the user asks to整理微信读书笔记, organize WeRead highlights, convert WeRead Obsidian exports, create book notes, or generate atomic notes from book highlights.
---

# WeRead Reading Note

Convert one WeRead export Markdown file into:

1. A structured reading note.
2. 5-12 atomic notes for reusable concepts.

This skill only reorganizes local Markdown files. It does not fetch, scrape, or bypass WeRead content.

## Inputs

Ask for the source file if it is missing. Otherwise infer it from the user request.

Resolve paths in this order:

1. Paths explicitly provided in the user request.
2. `weread-reading-note.config.yaml` in the current vault root.
3. `.weread-reading-note.yaml` in the current vault root.
4. Built-in defaults below.

If no source file is given and no config file exists, ask the user for all required folders before proceeding:

- WeRead sync folder for source Markdown files.
- Reading note output folder.
- Atomic note output folder.
- Cover image output folder, if cover download is needed.

Built-in defaults:

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

1. Read the source Markdown.
2. Parse book metadata from frontmatter and `# 元数据`.
3. Parse every highlight from `> 📌 <text>` and attach it to the nearest preceding chapter heading.
4. Parse comments from `💭 <comment>` and attach each comment to the nearest preceding highlight.
5. Extract overall reviews from `# 本书评论`, if present.
6. Write the reading note using `references/output-templates.md`.
7. Generate 5-12 atomic notes using the concept rules below.
8. If an atomic note already exists, update it append-only. Never overwrite the user's reflection section.
9. Run the checklist before responding.

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

- The reading note has all required sections.
- The reading note has a table of contents callout near the top.
- Highlight comments are not duplicated as pure highlights.
- The `读书笔记` section only contains commented highlights.
- Atomic note links in the reading note match actual files.
- Existing atomic notes were updated append-only.
- `## 我的理解` was not changed in existing atomic notes.
- No real copyrighted sample text was introduced into repository examples.

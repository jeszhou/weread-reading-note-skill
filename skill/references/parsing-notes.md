# Parsing Notes

WeRead export formats vary slightly. Support these common patterns.

## Frontmatter

Read common fields if present:

- `title`
- `author`
- `cover`
- `isbn`
- `readingStatus`
- `progress`
- `readingTime`
- `readingDate`
- `finishedDate`
- `lastReadDate`

## Metadata Section

In `# 元数据`, parse lines like:

```markdown
> - 书名： <title>
> - 作者： <author>
> - 简介： <description>
> - 出版时间： <publish date>
> - ISBN： <isbn>
> - 分类： <category>
> - 出版社： <publisher>
> - PC地址：<url>
```

Prefer frontmatter for machine fields and `# 元数据` for publisher, category, and source URL.

## Highlights

Highlight pattern:

```markdown
### <chapter>

> 📌 <highlight text>
> ⏱ <time> ^<anchor>
```

Treat the nearest preceding Markdown heading after `# 高亮划线` as the chapter. If no chapter exists, use `未分章`.

## Comments

Inline comment pattern:

```markdown
> 📌 <highlight text>
> ⏱ <time> ^<anchor>
- 💭 <comment> - ⏱ <time>
```

Separate reading-note section pattern:

```markdown
# 读书笔记

### <chapter or comment heading>

> 📌 <highlight text>
> ⏱ <time> ^<anchor>

💭 <comment>
```

Attach each comment to the nearest preceding highlight. If exact matching is needed, match by anchor first, then by normalized highlight text.

## Overall Reviews

Everything under `# 本书评论` belongs to the overall review section. Preserve paragraph order. If reviews are split by headings like `## 书评 No.1`, keep the text grouped but do not over-format it.

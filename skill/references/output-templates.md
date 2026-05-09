# Output Templates

## Reading Note Template

```markdown
---
type: reading-note
book: <book title>
author: <author>
source: <source URL>
status: organized
created: <YYYY-MM-DD>
tags:
  - 读书笔记
  - 微信读书
---

# 《<book title>》读书笔记

> [!summary] 目录
> - [[#书籍信息]]
> - [[#高亮划线]]
> - [[#读书笔记]]
> - [[#整体评论]]
> - [[#语义卡]]
> - [[#写作切入点]]

## 书籍信息

**书名**：<book title>
**作者**：<author>
**出版**：<publisher>，<publish date>
**ISBN**：<isbn>
**分类**：<category>
**阅读**：<reading time>（<reading start> 至 <finished date>）
**整理**：<YYYY-MM-DD>
**链接**：[微信读书](<source URL>)
**原始文件**：`<source file path>`

---

## 高亮划线

### <chapter title>

> [!quote]
> <highlight text>

---

## 读书笔记

> 章节：<chapter title>
>
> 原文：
> <highlight text>

> [!note] 我的笔记
> <user comment>

---

## 整体评论

> [!example]
> <overall review, or fallback text>

---

## 语义卡

> [!abstract] 这本书贡献的概念
> 下列每张卡都已创建或更新。

**概念**
- [[<concept name>]]

**心法**
- [[<mindset name>]]

**方法**
- [[<method name>]]

---

## 写作切入点

> [!tip] 三个切入点
> 1. <hook 1>
> 2. <hook 2>
> 3. <hook 3>
```

Omit missing metadata lines instead of writing placeholders.

## Atomic Note Template

```markdown
---
type: atomic-note
category: <概念 | 心法 | 方法>
status: seedling
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
tags:
  - <tag>
related:
  - "[[<related concept>]]"
sources:
  - "[[《<book title>》读书笔记]]"
---

# <concept name>

## 一句话

<one concise definition in this book's context>

## 从哪本书来

- 首次见于：[[《<book title>》读书笔记]]（<author>）：<one-sentence angle>
- 后续也出现在：
  - （留空，未来追加）

## 关联原文

### 来自《<book title>》

> <short relevant highlight>

## 我的理解

（这一段留给用户自己写。）

## 相关概念

- [[<related concept>]]：<why it is related>

## 写作切入口

- <hook 1>
- <hook 2>
```

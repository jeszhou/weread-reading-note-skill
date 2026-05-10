# WeRead Reading Note Skill

把微信读书同步到 Obsidian 的 Markdown，整理成一份结构清晰的读书笔记，并顺手生成一组可复用的语义卡。

这个仓库提供的是一个可移植的 Codex / Agent Skill。它不会抓取、破解或下载微信读书内容，只处理你本来已经同步到本地 Obsidian vault 里的 Markdown 文件。

## 它能做什么

- 读取一本书的微信读书导出 Markdown。
- 拆分书籍元数据、划线、划线评论和整本书书评。
- 生成一份结构化的 Obsidian 读书笔记。
- 生成 5-12 张语义卡，用来沉淀概念、心法或方法。
- 生成语义卡前扫描已有读书笔记和语义卡，优先复用或更新已有概念。
- 如果语义卡已经存在，只追加新来源，不覆盖用户自己写过的理解。

## 目录结构

```text
weread-reading-note-skill/
  README.md
  LICENSE
  config.example.yaml
  scripts/
    setup_config.py
  skill/
    SKILL.md
    references/
      output-templates.md
      parsing-notes.md
  examples/
    sample-weread-export.md
    sample-reading-note.md
    sample-atomic-note.md
```

真正的 Skill 在 `skill/` 目录里。你可以把它复制到自己的 agent skills 目录，也可以按自己的命名习惯重命名。

## 第一次配置

每个人同步微信读书的文件夹都不一样。安装 Skill 通常只是复制文件，不会自动弹出对话询问路径。

首次使用前，你可以先在自己的 Obsidian vault 根目录生成一份配置：

```bash
python3 /path/to/weread-reading-note-skill/scripts/setup_config.py --vault /path/to/your/obsidian-vault
```

脚本会问你四个路径：

```text
微信读书同步 Markdown 文件夹 [WeRead Exports]:
整理后的读书笔记输出文件夹 [Reading Notes]:
语义卡输出文件夹 [Atomic Notes]:
封面图保存文件夹 [assets/book-covers]:
```

它会在 vault 根目录生成：

```text
weread-reading-note.config.yaml
```

配置内容类似：

```yaml
input_dir: WeRead Exports
reading_note_dir: Reading Notes
atomic_note_dir: Atomic Notes
image_dir: assets/book-covers
```

如果你不想跑脚本，也可以复制 `config.example.yaml`，改名为 `weread-reading-note.config.yaml`，再手动填写自己的路径。

Skill 执行时会按这个顺序找路径：

1. 你在提示词里明确指定的路径。
2. vault 根目录的 `weread-reading-note.config.yaml`。
3. 旧版配置文件 `.weread-reading-note.yaml`。
4. 如果前面都没有，就必须现场问你输入和输出文件夹分别在哪里。

它不能在首次使用时静默写入 `WeRead Exports`、`Reading Notes`、`Atomic Notes` 这些默认目录。默认目录只能作为建议，必须经过你确认。

## 使用示例

```text
Use the WeRead reading note skill to organize:
WeRead Exports/Sample Book.md

Use these paths:
- reading_note_dir: Reading Notes
- atomic_note_dir: Atomic Notes
- image_dir: assets/book-covers
```

中文也可以直接这样说：

```text
用 $weread-reading-note 整理这本微信读书笔记：
WeRead Exports/样例之书.md

读书笔记放到：Reading Notes
语义卡放到：Atomic Notes
封面放到：assets/book-covers
```

## 输入文件要求

这个 Skill 适合处理微信读书 Obsidian 插件同步出来的 Markdown，常见结构类似：

```markdown
---
title: 书名
author: 作者
readingTime: 阅读时长
finishedDate: 完成日期
---

# 元数据

# 高亮划线

### 章节名

> 📌 划线原文
> ⏱ 时间 ^anchor

- 💭 我的评论 - ⏱ 时间

# 本书评论
```

不同插件版本的格式可能有细微差异。Skill 已经把常见的内嵌评论、独立读书笔记区、重复章节都考虑进去了。

## 输出结果

默认会生成两类文件：

```text
Reading Notes/《书名》读书笔记.md
Atomic Notes/<概念名>.md
```

读书笔记包含：

- 书籍信息
- 高亮划线
- 读书笔记
- 整体评论
- 语义卡
- 写作切入点，用来把读书笔记继续转化成文章、卡片或复盘

语义卡包含：

- 一句话定义
- 来源书籍
- 关联原文
- 我的理解
- 相关概念
- 写作切入口

其中 `我的理解` 默认留给用户自己写。已有语义卡重跑时，也不会覆盖这一段。

生成新语义卡前，Skill 会先检查已有的 `Atomic Notes/` 和 `Reading Notes/`。如果发现近义、同义或跨领域同构的概念，会优先更新已有卡，或者在 `相关概念` 里互链，而不是每本书都新建一批孤立卡。

## 版权提醒

不要把包含大量真实书摘的导出文件直接公开，除非你确认自己有权这么做。这个仓库里的示例全部是虚构文本，不包含真实书籍内容。

## License

MIT

#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


DEFAULTS = {
    "input_dir": "WeRead Exports",
    "reading_note_dir": "Reading Notes",
    "atomic_note_dir": "Atomic Notes",
    "image_dir": "assets/book-covers",
}


def ask(label: str, key: str) -> str:
    default = DEFAULTS[key]
    value = input(f"{label} [{default}]: ").strip()
    return value or default


def quote_yaml(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create weread-reading-note.config.yaml for a vault."
    )
    parser.add_argument(
        "--vault",
        default=".",
        help="Vault root where weread-reading-note.config.yaml will be written.",
    )
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    config_path = vault / "weread-reading-note.config.yaml"

    print("Configure WeRead Reading Note Skill")
    print(f"Vault: {vault}")
    print()

    input_dir = ask("微信读书同步 Markdown 文件夹", "input_dir")
    reading_note_dir = ask("整理后的读书笔记输出文件夹", "reading_note_dir")
    atomic_note_dir = ask("语义卡输出文件夹", "atomic_note_dir")
    image_dir = ask("封面图保存文件夹", "image_dir")

    content = "\n".join(
        [
            "# WeRead Reading Note Skill configuration",
            "# Paths are relative to your Obsidian vault root unless absolute.",
            f"input_dir: {quote_yaml(input_dir)}",
            f"reading_note_dir: {quote_yaml(reading_note_dir)}",
            f"atomic_note_dir: {quote_yaml(atomic_note_dir)}",
            f"image_dir: {quote_yaml(image_dir)}",
            "",
        ]
    )

    vault.mkdir(parents=True, exist_ok=True)
    config_path.write_text(content, encoding="utf-8")
    print()
    print(f"Wrote: {config_path}")


if __name__ == "__main__":
    main()

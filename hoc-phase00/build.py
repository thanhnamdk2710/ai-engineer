#!/usr/bin/env python3
"""Đóng gói Phase 00 (bản tiếng Việt) thành một trang web học tập duy nhất.

Chạy:  python3 build.py  [đường-dẫn-repo]
Ra:    dist/index.html  (mở trực tiếp trên trình duyệt, cần internet cho font/CDN)
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE.parent / "ai-engineering-from-scratch").resolve()
PHASE = "00-setup-and-tooling"
SRC = REPO / "phases" / PHASE
VI = REPO / "i18n" / "vi" / "phases" / PHASE

EXT_LANG = {
    ".py": "python", ".ts": "typescript", ".rs": "rust", ".sh": "bash",
    ".json": "json", ".yml": "yaml", ".yaml": "yaml", ".md": "markdown",
    ".toml": "ini",
}


def first_heading(md: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def code_files(lesson_dir: pathlib.Path):
    out = []
    for sub in ("code", "outputs"):
        base = lesson_dir / sub
        if not base.is_dir():
            continue
        for f in sorted(p for p in base.rglob("*") if p.is_file()):
            if f.name.startswith(".") or "__pycache__" in f.parts:
                continue
            lang = "dockerfile" if f.name == "Dockerfile" else EXT_LANG.get(f.suffix, "plaintext")
            out.append({
                "path": str(f.relative_to(lesson_dir)),
                "lang": lang,
                "content": f.read_text(encoding="utf-8"),
            })
    return out


def main():
    lessons = []
    for d in sorted(p for p in SRC.iterdir() if p.is_dir() and p.name[:2].isdigit()):
        en = (d / "docs" / "en.md").read_text(encoding="utf-8")
        vi_path = VI / d.name / "docs" / "vi.md"
        vi = vi_path.read_text(encoding="utf-8") if vi_path.exists() else None
        quiz_vi = VI / d.name / "quiz.json"
        quiz_en = d / "quiz.json"
        quiz, quiz_lang = None, None
        if quiz_vi.exists():
            quiz, quiz_lang = json.loads(quiz_vi.read_text(encoding="utf-8")), "vi"
        elif quiz_en.exists():
            quiz, quiz_lang = json.loads(quiz_en.read_text(encoding="utf-8")), "en"
        lessons.append({
            "id": d.name[:2],
            "slug": d.name,
            "title_en": first_heading(en),
            "title_vi": first_heading(vi) if vi else first_heading(en),
            "en": en,
            "vi": vi,
            "quiz": quiz,
            "quiz_lang": quiz_lang,
            "code": code_files(d),
        })

    data = {"phase": PHASE, "lessons": lessons}
    data_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

    fig_js = "\n".join(
        (REPO / "site" / name).read_text(encoding="utf-8")
        for name in ("lesson-figures.js", "figures-setup.js")
    )

    tpl = (HERE / "template.html").read_text(encoding="utf-8")
    html = tpl.replace("/*__DATA__*/", data_json).replace("/*__FIGJS__*/", fig_js)
    out = HERE / "dist" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    missing_vi = [l["slug"] for l in lessons if not l["vi"]]
    print(f"wrote {out} ({out.stat().st_size // 1024} KB), {len(lessons)} lessons;"
          f" quiz vi: {sum(l['quiz_lang'] == 'vi' for l in lessons)}; missing vi: {missing_vi}")


if __name__ == "__main__":
    main()

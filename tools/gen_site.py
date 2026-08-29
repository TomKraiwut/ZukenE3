"""Shared templates, nav data, and link-relocation writer for the ZukenE3 site.

Run order (from tools/): gen_site.py, gen_chapters.py, gen_pages.py, gen_index.py
"""
import os
import posixpath
import re

OUTPUT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

SITE_TITLE = "Zuken E3.series Tutorial"

FONT_LINKS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600;700'
    '&family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap">'
)

SECTIONS = {
    "schematic": {
        "label": "Schematics",
        "hub": "schematic.html",
        "old_prefix": "worksheet",
        "chapters": [
            "1. UI และโปรเจกต์",
            "2. วางอุปกรณ์ &amp; Properties",
            "3. เชื่อมวงจร &amp; Online Checks",
            "4. Fields &amp; Levels",
            "5. Signals &amp; Signal Tree",
            "6. Search &amp; Replace",
            "7. Terminals &amp; Terminal Plan",
            "8. Subcircuits",
            "9. DBE: สร้าง Symbol",
            "10. Sync &amp; Report",
        ],
    },
    "cable": {"label": "Cable", "hub": "cable.html", "chapters": []},
    "panel": {"label": "Panel", "hub": "panel.html", "chapters": []},
    "database-editor": {"label": "Database Editor", "hub": "database-editor.html", "chapters": []},
}
SECTION_ORDER = ["schematic", "cable", "panel", "database-editor"]

# Map every OLD flat filename (as authored in links/prose) to its NEW repo path.
OLD_TO_NEW = {"index.html": "index.html"}
for _slug in SECTION_ORDER:
    _sec = SECTIONS[_slug]
    OLD_TO_NEW[_sec["hub"]] = f"{_slug}/index.html"
    _prefix = _sec.get("old_prefix", _slug)
    for _i in range(1, len(_sec["chapters"]) + 1):
        OLD_TO_NEW[f"{_prefix}-{_i:02d}.html"] = f"{_slug}/{_i:02d}.html"


def sidebar_items(current_section=None, current_chapter=None):
    parts = []
    home_active = ' class="active"' if current_section is None else ""
    parts.append(f'                    <li{home_active}><a href="index.html">หน้าแรก</a></li>')

    for slug in SECTION_ORDER:
        sec = SECTIONS[slug]
        # Author nav links with the OLD flat filenames (same as body prose) so
        # write()'s relocator can compute the correct relative path for every
        # page depth — never hardcode a NEW path here.
        hub_old = sec["hub"]
        prefix = sec.get("old_prefix", slug)
        is_current = current_section == slug
        if sec["chapters"]:
            li_classes = "has-children"
            if is_current:
                li_classes += " expanded"
                if current_chapter is None:
                    li_classes += " active"
            parts.append(f'                    <li class="{li_classes}">')
            parts.append(f'                        <a href="{hub_old}">{sec["label"]}</a>')
            parts.append(
                f'                        <button class="submenu-toggle" '
                f'aria-label="แสดง/ซ่อนเมนู {sec["label"]}">▾</button>'
            )
            parts.append('                        <ul class="submenu">')
            for idx, title in enumerate(sec["chapters"], start=1):
                chapter_old = f"{prefix}-{idx:02d}.html"
                cls = ' class="active"' if is_current and current_chapter == idx else ""
                parts.append(f'                            <li{cls}><a href="{chapter_old}">{title}</a></li>')
            parts.append("                        </ul>")
            parts.append("                    </li>")
        else:
            li_classes = "active" if is_current else ""
            cls_attr = f' class="{li_classes}"' if li_classes else ""
            parts.append(f'                    <li{cls_attr}><a href="{hub_old}">{sec["label"]}</a></li>')

    return "\n".join(parts)


def page_html(title, body_html, current_section=None, current_chapter=None, extra_sidebar_html=""):
    extra = f"\n{extra_sidebar_html}" if extra_sidebar_html else ""
    return f'''<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{FONT_LINKS}
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div id="wrapper">
    <div id="main">
        <div class="inner">
            <header id="header">
                <a href="index.html" class="logo"><span>{SITE_TITLE}</span></a>
                <button class="menu-toggle" aria-label="เปิดเมนู">☰</button>
            </header>

{body_html}
        </div>
    </div>

    <div id="sidebar">
        <div class="inner">
            <nav id="menu">
                <header class="major"><h2>เมนู</h2></header>
                <ul>
{sidebar_items(current_section, current_chapter)}
                </ul>
            </nav>{extra}
            <footer id="footer">
                <p class="copyright">{SITE_TITLE} — เอกสารประกอบการเรียนรู้ภายในทีม</p>
            </footer>
        </div>
    </div>
</div>

<script src="assets/main.js"></script>
</body>
</html>
'''


_LINK_ATTR_RE = re.compile(r'(href|src)="([^"]+)"')


def write(relpath, content):
    def _relocate(m):
        attr, val = m.group(1), m.group(2)
        if val in OLD_TO_NEW:
            target = OLD_TO_NEW[val]
        elif val.startswith("assets/"):
            target = val
        else:
            return m.group(0)
        cur_dir = posixpath.dirname(relpath) or "."
        rel = posixpath.relpath(target, cur_dir)
        return f'{attr}="{rel}"'

    relocated = _LINK_ATTR_RE.sub(_relocate, content)
    full_path = os.path.join(OUTPUT_ROOT, relpath.replace("/", os.sep))
    os.makedirs(os.path.dirname(full_path) or ".", exist_ok=True)
    with open(full_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(relocated)

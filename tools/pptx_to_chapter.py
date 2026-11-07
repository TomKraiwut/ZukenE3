# -*- coding: utf-8 -*-
"""Chapter draft from a Step-by-Step deck (.pptx) -- text comes from the deck itself, which keeps
Thai spacing and legend order intact (the PDF text layer loses both).

    python -X utf8 pptx_to_chapter.py <deck.pptx> <NN>

Screenshots are cut by pdf_to_chapter.py; this script expects the picture of step k at
assets/images/lessons/NN-kk.jpg (rename the crops so they follow the step number).

Slide types, recognised by the small kicker above the title ("Text Placeholder 5"):
  slide 1                 cover              -> skipped
  "ภาพรวม ..." title      overview cards      -> table + "สิ่งที่ต้องมี" tip + bottom note
  "ขั้นที่ k / N"          step               -> screenshot + numbered legend + notes
  anything else           text grid / list   -> <table> (checklist -> list table, last box -> tip)
Writes tools/chapters/lessons_NN.py, or lessons_NN_draft.py if the chapter file already exists."""
import html
import os
import re
import sys

from pptx import Presentation
from pptx.util import Emu

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP_NAMES = ("Footer", "Slide Number", "Date Placeholder")
LABEL_RED = "FA000F"


def cm(v):
    return round(Emu(v or 0).cm, 1)


def shapes_of(slide):
    def walk(shs):
        for sh in shs:
            if sh.shape_type == 6:
                yield from walk(sh.shapes)
            else:
                yield sh
    return list(walk(slide.shapes))


def esc(s):
    s = html.escape(s, quote=False)
    s = s.replace("{", "{{").replace("}", "}}").replace("\\", "\\\\")
    s = s.replace("'''", "&#39;&#39;&#39;")
    return re.sub(r"[  ]{2,}", " ", s).strip()


def runs(sh):
    """[(text, bold, rgb)] over all paragraphs; a paragraph break becomes a space."""
    out = []
    for i, p in enumerate(sh.text_frame.paragraphs):
        if i and out:
            out.append((" ", None, None))
        for r in p.runs:
            rgb = None
            try:
                if r.font.color and r.font.color.type is not None:
                    rgb = str(r.font.color.rgb)
            except AttributeError:
                pass
            out.append((r.text.replace("\v", " "), r.font.bold, rgb))
    return out


def rich(sh):
    """Text with bold runs as <strong>."""
    parts = []
    for t, b, _ in runs(sh):
        if not t:
            continue
        if not t.strip():
            parts.append(" ")
            continue
        lead = " " if t[0].isspace() else ""
        trail = " " if t[-1].isspace() else ""
        parts.append(lead + (f"<strong>{esc(t)}</strong>" if b else esc(t)) + trail)
    s = "".join(parts)
    s = re.sub(r"</strong>(\s*)<strong>", r"\1", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def unbold(s):
    return s.replace("<strong>", "").replace("</strong>", "")


def plain(sh):
    return re.sub(r"\s+", " ", "".join(t for t, _, _ in runs(sh))).strip()


def label_split(sh):
    """('ข้อควรจำ', body) when the box starts with a bold red label, else None."""
    rs = [r for r in runs(sh) if r[0].strip()]
    if rs and rs[0][1] and (rs[0][2] or "").upper() == LABEL_RED:
        full = "".join(t for t, _, _ in runs(sh))
        lbl = rs[0][0]
        return esc(lbl), esc(full[full.index(lbl) + len(lbl):])
    return None


def text_boxes(slide):
    out = []
    for sh in shapes_of(slide):
        if not sh.has_text_frame or not sh.text_frame.text.strip():
            continue
        if any(k in sh.name for k in SKIP_NAMES):
            continue
        out.append(sh)
    return out


def title_kicker(slide):
    title = kicker = ""
    for sh in text_boxes(slide):
        if sh.name.startswith("Title"):
            title = plain(sh)
        elif sh.name.startswith("Text Placeholder"):
            kicker = plain(sh)
    return title, kicker


def body_boxes(slide):
    return [sh for sh in text_boxes(slide) if not sh.name.startswith(("Title", "Text Placeholder"))]


def note_html(lbl, body):
    cls = "note" if lbl.strip() in ("หมายเหตุ", "ระวัง", "ข้อควรระวัง", "ข้อควรจำ", "ไฟล์ฝึก") else "tip"
    return f'<div class="{cls}"><strong>{lbl.strip()}:</strong> {body}</div>'


def rows_of(boxes, tol=0.45):
    rows = []
    for sh in sorted(boxes, key=lambda s: (cm(s.top), cm(s.left))):
        if rows and abs(cm(sh.top) - rows[-1][0]) <= tol:
            rows[-1][1].append(sh)
        else:
            rows.append([cm(sh.top), [sh]])
    return [sorted(r, key=lambda s: cm(s.left)) for _, r in rows]


def step_slide(slide, nn, k, title):
    boxes = body_boxes(slide)
    ovals = [sh for sh in boxes if re.fullmatch(r"\d{1,2}", plain(sh)) and "Oval" in sh.name]
    others = [sh for sh in boxes if sh not in ovals]
    legend, used = {}, set()
    for ov in ovals:
        for sh in others:
            if id(sh) in used:
                continue
            if abs(cm(sh.top) - cm(ov.top)) <= 0.35 and 0.3 <= cm(sh.left) - cm(ov.left) <= 1.6:
                legend[int(plain(ov))] = rich(sh)
                used.add(id(sh))
                break
    notes = []
    for sh in others:
        if id(sh) in used:
            continue
        ls = label_split(sh)
        if ls:
            notes.append(note_html(*ls))
    items = [legend[n] for n in sorted(legend)]
    alt = esc(title)
    img = f"assets/images/lessons/{nn:02d}-{k:02d}.jpg"
    lst = ",\n".join(f"        '{t}'" for t in items)
    out = [f"<h2>{alt}</h2>",
           "{side_by_side(",
           f'    screenshot("{img}", "{alt}"),',
           "    step_list([",
           lst + ",",
           "    ])",
           ")}"]
    out += notes
    return "\n".join(out), len(items)


def overview_slide(slide, title):
    boxes = body_boxes(slide)
    cards = []
    for sh in boxes:
        if re.fullmatch(r"0\d", plain(sh)):
            x, y = cm(sh.left), cm(sh.top)
            near = sorted([b for b in boxes if 1.0 <= cm(b.left) - x <= 2.0 and -0.3 <= cm(b.top) - y <= 1.6],
                          key=lambda b: cm(b.top))
            if len(near) >= 2:
                cards.append((plain(sh), esc(plain(near[0])), esc(plain(near[1]))))
    cards.sort()
    need, steps, time_, notes = [], "", "", []
    for sh in boxes:
        t = plain(sh)
        if t == "สิ่งที่ต้องมี":
            below = [b for b in boxes if abs(cm(b.left) - cm(sh.left)) < 0.3 and 0.3 < cm(b.top) - cm(sh.top) < 2.5]
            for b in below:
                need = [esc(p.text) for p in b.text_frame.paragraphs if p.text.strip()]
        elif re.fullmatch(r"\d+ ขั้น", t):
            steps = t
        elif t.startswith("ใช้เวลา"):
            time_ = esc(t)
        else:
            ls = label_split(sh)
            if ls:
                notes.append(note_html(*ls))
    sub = esc(re.sub(r"^ภาพรวม\s*", "", title))
    out = [f"<h2>ภาพรวม: {sub}</h2>" if sub else "<h2>ภาพรวม</h2>", "<table>", "<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>"]
    out += [f"<tr><td>{n}</td><td>{a}</td><td>{b}</td></tr>" for n, a, b in cards]
    out.append("</table>")
    if need:
        out.append(f'<div class="tip"><strong>สิ่งที่ต้องมี:</strong> {" · ".join(need)}</div>')
    out += notes
    return "\n".join(out), steps, time_


def grid_slide(slide, title):
    boxes = body_boxes(slide)
    rows = rows_of(boxes)
    out = [f"<h2>{esc(title)}</h2>"]
    tail = []
    # a trailing single-box row (footnote / "ครบทุกข้อ" box) is not part of the table
    while (rows and len(rows[-1]) == 1 and len(rows) > 1 and max(len(r) for r in rows) > 1
           and (label_split(rows[-1][0]) or Emu(rows[-1][0].width).cm > 20)):
        sh = rows.pop()[0]
        ls = label_split(sh)
        tail.insert(0, note_html(*ls) if ls else f"<p>{rich(sh)}</p>")
    width = max((len(r) for r in rows), default=0)
    if "Checklist" in title:
        items = [rich(sh) for r in rows for sh in r]
        out.append("<table>\n<tr><th>ข้อ</th><th>ทำได้หรือยัง</th></tr>")
        out += [f"<tr><td>{i}</td><td>{t}</td></tr>" for i, t in enumerate(items, 1)]
        out.append("</table>")
    else:
        out.append("<table>")
        for n, r in enumerate(rows):
            if len(r) < width:
                out.append(f'<tr><td colspan="{width}"><strong>{unbold(rich(r[0]))}</strong></td></tr>' if len(r) == 1 else
                           "<tr>" + "".join(f"<td>{rich(sh)}</td>" for sh in r) + "</tr>")
                continue
            if n == 0:
                out.append("<tr>" + "".join(f"<th>{unbold(rich(sh))}</th>" for sh in r) + "</tr>")
            else:
                out.append("<tr>" + "".join(f"<td>{rich(sh) if c else unbold(rich(sh))}</td>"
                                            for c, sh in enumerate(r)) + "</tr>")
        out.append("</table>")
    return "\n".join(out + tail)


def main():
    deck, nn = sys.argv[1], int(sys.argv[2])
    prs = Presentation(deck)
    parts, steps_total, legend_total, header = [], 0, 0, []
    for pno, slide in enumerate(prs.slides, 1):
        title, kicker = title_kicker(slide)
        if pno == 1:
            header.append(f"# cover: {title}")
            continue
        if (not body_boxes(slide) and not title) or title.lower().startswith("thank you"):
            continue  # thank-you slide
        parts.append(f"<!-- slide {pno} -->")
        m = re.fullmatch(r"ขั้นที่ (\d+) / (\d+)", kicker)
        if m:
            h, n = step_slide(slide, nn, int(m.group(1)), title)
            parts.append(h)
            steps_total += 1
            legend_total += n
        elif title.startswith("ภาพรวม"):
            h, steps, time_ = overview_slide(slide, title)
            parts.append(h)
            header.append(f"# overview: {esc(title)} | {steps} | {time_}")
        else:
            parts.append(grid_slide(slide, title))
        parts.append("")
    body = "\n".join(parts)
    src = (f'# -*- coding: utf-8 -*-\n"""DRAFT from {os.path.basename(deck)} by pptx_to_chapter.py -- edit by hand."""\n'
           "from gen_site import screenshot, step_list, side_by_side\n\n" + "\n".join(header) +
           "\n\nOBJECTIVES = [\n    # TODO\n]\n\nBODY = f'''\n" + body + "'''\n")
    out = os.path.join(HERE, "chapters", f"lessons_{nn:02d}.py")
    if os.path.exists(out):
        out = out[:-3] + "_draft.py"
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(src)
    print(f"wrote {out} - {steps_total} steps, {legend_total} legend items")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_site import (SECTIONS, QUIZ_PAGES, page_html, write, chapter_filename, chapter_numbers,
                      chapter_title, chapter_label, HUB_CARD_DESC)


def quiz_card(page, badge, desc):
    return f'''        <div class="card-grid">
          <a href="{page}" class="card">
            <div class="icon number">{badge}</div>
            <h3>{QUIZ_PAGES[page]["title"]}</h3>
            <p>{desc}</p>
          </a>
        </div>'''


def cards(section):
    out = []
    for n, i in enumerate(chapter_numbers(section)):
        out.append(f'''          <a href="{chapter_filename(section, i)}" class="card">
            <div class="icon number">{chapter_label(section, i)}</div>
            <h3>{chapter_title(section, i)}</h3>
            <p>{HUB_CARD_DESC[section][n]}</p>
          </a>''')
    return "\n".join(out)


BODY = f"""        <section id="banner">
          <h1>เรียนรู้ Zuken E³.series</h1>
          <p class="tagline">ชุดสอน Step by Step บน E³.series ภาษาไทย</p>
          <p class="intro">
            ลงมือทำทีละบท ตั้งแต่รู้จักหน้าจอ, เขียนวงจรไฟฟ้าด้วย E³.schematic, วางอุปกรณ์ในตู้ด้วย E³.panel
            ไปจนถึงสร้าง Symbol, Component และ Model เองใน Database Editor — ทุกบทมีภาพหน้าจอจริงพร้อมเลขกำกับ
            บนโปรเจกต์ตัวอย่าง Cooling water pump ที่มากับโปรแกรม
          </p>
        </section>

        <h2>เริ่มที่นี่</h2>
{quiz_card("pre-test.html", "ก่อน", "แบบทดสอบ 20 ข้อ และความคาดหวังต่อการเรียน ประมาณ 15 นาที — ใช้เทียบคะแนนกับหลังเรียน")}

        <h2>{SECTIONS["lessons"]["label"]}</h2>
        <p>ทุกบทใช้สำเนาของโปรเจกต์ตัวอย่าง <code>Cooling water pump.e3s</code> ที่มากับโปรแกรม
        (คัดลอกมาไว้ในโฟลเดอร์ของตัวเองก่อนเปิด) — บท 02 ทำต่อจากผลของบท 01 ส่วนบท 03–04 ทำใน Database Editor บนสำเนาฐานข้อมูล</p>
        <div class="card-grid">
{cards("lessons")}
        </div>

        <h2>เรียนจบแล้ว</h2>
{quiz_card("post-test.html", "หลัง", "แบบทดสอบ 20 ข้อชุดเดียวกับก่อนเรียน และประเมินการเรียน (Feedback) — ผลสอบส่งให้ทางอีเมล")}"""

if __name__ == "__main__":
    write("index.html", page_html("หน้าแรก", BODY, active_top="index"))

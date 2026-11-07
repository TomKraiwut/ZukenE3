# ZukenE3

เว็บไซต์สอนการใช้งาน Zuken E³.series แบบ Step by Step (ภาษาไทย) — เผยแพร่ผ่าน GitHub Pages
เนื้อหามาจากชุด deck `02_Quicktour` (ไฟล์ `.pptx` ของแต่ละบท) โครงเว็บและ generator ใช้แบบเดียวกับ PlantSimulation / ProcessSimulate

## โครงสร้างเว็บ

- [index.html](index.html) — หน้าแรก (แบบทดสอบก่อนเรียน → การ์ดของทุกบท → แบบทดสอบหลังเรียน)
- **Step by Step 00–04** ([lessons/](lessons/index.html)) — แต่ละบทเป็นเมนูหลักของตัวเอง `lessons/00.html` .. `04.html`
  - 00 หน้าจอและพื้นฐาน · 01 วงจรไฟฟ้า E³.schematic · 02 ออกแบบตู้ E³.panel · 03 สร้าง Symbol และ Component · 04 สร้าง Model ของตู้
- [pre-test.html](pre-test.html) / [post-test.html](post-test.html) — ฝัง Google Forms (ลิงก์ตั้งใน `QUIZ_PAGES`)
- [assets/style.css](assets/style.css) / [assets/main.js](assets/main.js) — สไตล์ (แดง / เทา / ขาว ตามสไลด์) และเมนู off-canvas
- `assets/images/lessons/<NN>-<ขั้นที่>.jpg` — ภาพหน้าจอของขั้นที่ k ในบท NN

ทุกบทใช้สำเนาของโปรเจกต์ตัวอย่าง `Cooling water pump.e3s` ที่มากับโปรแกรม (`C:\Users\Public\Documents\Zuken\E3.series_<เวอร์ชัน>\data\Pumpe`)

## สร้าง/แก้ไขหน้าเว็บด้วยสคริปต์ (ไม่แก้ไฟล์ .html ตรงๆ)

- [tools/gen_site.py](tools/gen_site.py) — โครงเมนู (`SECTIONS`), ลิงก์แบบทดสอบ (`QUIZ_PAGES`), คำอธิบายการ์ด (`HUB_INTRO`, `HUB_CARD_DESC`), เทมเพลต และ helper (`screenshot`, `step_list`, `side_by_side`)
- [tools/chapters/](tools/chapters/) — เนื้อหาบทละไฟล์ `lessons_NN.py` มี `OBJECTIVES` และ `BODY` (f-string; ปีกกาจริงต้องเป็น `{{` `}}`, backslash ต้องเป็น `\\`)
- [tools/gen_chapters.py](tools/gen_chapters.py), [tools/gen_index.py](tools/gen_index.py), [tools/gen_quiz.py](tools/gen_quiz.py) — หน้าบท / หน้าแรก / หน้าแบบทดสอบ

```bash
cd tools
python -X utf8 gen_site.py
python -X utf8 gen_chapters.py
python -X utf8 gen_index.py
python -X utf8 gen_quiz.py
```

ทดสอบก่อน push: `python -m http.server 8000` จากโฟลเดอร์นี้ แล้วเปิด `http://localhost:8000/`

## ทำบทใหม่จาก deck

1. Export `.pptx` เป็น PDF (PowerPoint → Save As → PDF)
2. `python -X utf8 tools/pdf_to_chapter.py <deck.pdf> <NN>` — ตัดภาพหน้าจอ (พร้อมเลขวงกลมแดง) ไปที่ `assets/images/lessons/`
   แล้วเปลี่ยนชื่อภาพให้ตรงเลขขั้น (`NN-01.jpg` = ขั้นที่ 1) ลบภาพของสไลด์ที่ไม่ใช่ขั้นตอน (ตาราง / Checklist)
3. `python -X utf8 tools/pptx_to_chapter.py <deck.pptx> <NN>` — อ่านข้อความจาก `.pptx` โดยตรง (ช่องว่างภาษาไทยและลำดับเลขกำกับถูกต้องกว่า PDF):
   สไลด์ภาพรวม → ตาราง + "สิ่งที่ต้องมี", สไลด์ "ขั้นที่ k / N" → ภาพ + `step_list()` + กล่องหมายเหตุ, สไลด์อื่น → ตาราง
   (ถ้ามีไฟล์บทอยู่แล้วจะเขียนเป็น `lessons_NN_draft.py`)
4. แก้ไฟล์บทด้วยมือ — `OBJECTIVES`, ย่อหน้านำ, ตาราง "ไฟล์ที่ใช้ในบทนี้", ตัดเลขเวอร์ชันโปรแกรมออก
5. เพิ่มชื่อบทใน `SECTIONS["lessons"]["chapters"]` และ `"ids"`, เพิ่ม `HUB_CARD_DESC` แล้ว build

## แบบทดสอบ

คำถามและเฉลยอยู่ใน `_No_Upload/quiz/` (ไม่ขึ้น git) — `Code.gs` สร้าง Google Forms ก่อน/หลังเรียน วิธีใช้ดู `_No_Upload/quiz/README.md`
ได้ลิงก์ `/viewform` แล้วใส่ใน `QUIZ_PAGES` ของ `gen_site.py` แล้วรัน `gen_quiz.py` ใหม่

## วิธีเปิดใช้งานเป็นเว็บไซต์ (GitHub Pages)

Settings → Pages → Source: **Deploy from a branch** → branch `main`, โฟลเดอร์ `/ (root)` → Save

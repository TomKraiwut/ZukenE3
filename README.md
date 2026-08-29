# ZukenE3

เว็บไซต์สอนการใช้งาน Zuken E3.series (ภาษาไทย) — เผยแพร่ผ่าน GitHub Pages

## โครงสร้างเว็บ

- [index.html](index.html) — หน้าแรก
- [schematic/](schematic/) — Schematics: [index.html](schematic/index.html) หน้ารวมลิงก์ไปยัง 10 บท ([01.html](schematic/01.html)–[10.html](schematic/10.html))
  - 01.html — Project & UI Setup
  - 02.html — Placing & Editing Devices
  - 03.html — Connecting & Online Checks
  - 04.html — Fields & Levels
  - 05.html — Signals & Signal Tree
  - 06.html — Global Search & Replace
  - 07.html — Terminals & Terminal Plan
  - 08.html — Subcircuits
  - 09.html — Database Editor (DBE): สร้าง Symbol/Component
  - 10.html — Database Sync & Reporting
- [cable/index.html](cable/index.html) — Cable: Mating Connector, Dynamic Cable, Block Function, คำนวณ Bundle
- [panel/index.html](panel/index.html) — Panel: Mounting Rail, Cable Duct, Terminal Strip, Autoconnect, 3D Panel
- [database-editor/index.html](database-editor/index.html) — Database Editor: สร้าง Symbol/Component/Model เอง, COM API
- [assets/style.css](assets/style.css) — สไตล์ชีตกลางของทุกหน้า (Editorial-inspired layout: sidebar nav + banner hero)
- [assets/main.js](assets/main.js) — toggle เมนูมือถือและ submenu accordion ของ Schematics
- [examples/](examples/) — ไฟล์ตัวอย่าง `.e3s` (เพิ่มเองได้ — ตัวอย่างฝึกทำอยู่ในแต่ละหน้าบท/โมดูล)
- [tools/](tools/) — สคริปต์ Python ที่ generate ไฟล์ `.html` ทั้งหมดข้างต้น (ดู "แก้ไข/เพิ่มเนื้อหา" ด้านล่าง)

เนื้อหาในเว็บนี้อ้างอิงจากคู่มือทางการ E3.series 2026 (E3.schematic, E3.cable, E3.panel, Database Editor, E3.Update)

## วิธีเปิดใช้งานเป็นเว็บไซต์ (GitHub Pages)

1. ไปที่ repo บน GitHub → **Settings → Pages**
2. หัวข้อ **Build and deployment** เลือก Source เป็น **Deploy from a branch**
3. เลือก branch `main` และโฟลเดอร์ `/ (root)` แล้วกด **Save**
4. รอสักครู่ เว็บจะออนไลน์ที่ `https://<username>.github.io/ZukenE3/`

### ถ้าตั้งค่าแล้วแต่เว็บขึ้น 404

ถ้าหน้า Settings บอกว่า "currently being built from the main branch" แต่เว็บจริงขึ้น
"Site not found" ให้บังคับปลดล็อกปุ่ม Save: เปลี่ยน Branch เป็น **None** → Save → รอ 10
วินาที → เปลี่ยนกลับเป็น **main** / **/(root)** → Save อีกครั้ง แล้วเช็คแท็บ **Actions**
ว่ามี workflow "pages build and deployment" รันสำเร็จ

## แก้ไข/เพิ่มเนื้อหา

ไฟล์ `.html` ทุกไฟล์ **ถูก generate จากสคริปต์ Python ใน [tools/](tools/) — อย่าแก้ `.html` ตรงๆ**
เพราะการรันสคริปต์ใหม่ภายหลังจะเขียนทับ แก้ที่ต้นทางแล้วรันสคริปต์ใหม่แทน:

- แก้เนื้อหาบทเรียน Schematics (`schematic/01.html`–`10.html`) → แก้ที่ `tools/gen_chapters.py`
- แก้เนื้อหาหน้า Schematics hub / Cable / Panel / Database Editor → แก้ที่ `tools/gen_pages.py`
- แก้เนื้อหาหน้าแรก → แก้ที่ `tools/gen_index.py`
- แก้เมนู/โครงสร้างส่วน (เพิ่มบท, เพิ่ม section ใหม่ทั้งหมด) → แก้ `SECTIONS`/`SECTION_ORDER` ใน `tools/gen_site.py`
- แก้ดีไซน์ร่วม (สี, ฟอนต์, layout) → แก้ `assets/style.css` โดยตรง (ไฟล์นี้ไม่ถูก generate)

รันสคริปต์ใหม่ทุกครั้งตามลำดับนี้ (import กันเป็นทอด ๆ):

```bash
cd tools
python gen_site.py
python gen_chapters.py
python gen_pages.py
python gen_index.py
```

**เพิ่มบทใหม่ในโมดูลที่มีอยู่แล้ว** (เช่น Schematics บทที่ 11): เพิ่มชื่อบทใน `SECTIONS["schematic"]["chapters"]`
ใน `gen_site.py`, เพิ่มเนื้อหา `BODY[11]`/`TITLE[11]` ใน `gen_chapters.py`, แล้วรันสคริปต์ใหม่ทั้งหมด — เมนู/ปุ่มก่อนหน้า-ถัดไป
จะอัปเดตให้เองไม่ต้องแก้ทีละไฟล์

**เพิ่ม section ใหม่ทั้งหมด** (เช่นโมดูลใหม่ของ E3.series): เพิ่ม entry ใหม่ใน `SECTIONS`/`SECTION_ORDER` ใน `gen_site.py`
(ตั้ง `"chapters": []` ถ้าเป็นหน้าเดียวไม่มีบทย่อย) แล้วเพิ่มเนื้อหาใน `gen_pages.py` และเพิ่มการ์ดในหน้าแรกที่ `gen_index.py`

แล้ว commit + push ตามปกติ

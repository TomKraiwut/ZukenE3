# ZukenE3

เว็บไซต์สอนการใช้งาน Zuken E3.series (ภาษาไทย) — เผยแพร่ผ่าน GitHub Pages

## โครงสร้างเว็บ

- [index.html](index.html) — หน้าแรก
- [basic.html](basic.html) — พื้นฐานการใช้งาน
- [advanced.html](advanced.html) — บริหาร Component Database และออกแบบ Cable/Harness
- [examples.html](examples.html) — ตัวอย่างวงจรและ Harness จริง
- [assets/style.css](assets/style.css) — สไตล์ชีตกลางของทุกหน้า
- [examples/](examples/) — ไฟล์ตัวอย่าง `.e3s` (เพิ่มเองได้)

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

แก้ไฟล์ `.html` ที่เกี่ยวข้อง แล้ว commit + push ตามปกติ

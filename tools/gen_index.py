"""Homepage (index.html). Ported verbatim from the original flat index.html."""
import gen_site as gs

TITLE = "Zuken E3.series Tutorial"

BODY = '''            <section id="banner">
                <h1>เรียนรู้ Zuken E3.series</h1>
                <p class="tagline">เว็บไซต์สอนการใช้งานโปรแกรมออกแบบวงจรไฟฟ้าและระบบสายไฟ (Electrical Schematic &amp; Wiring Harness Design) ตั้งแต่พื้นฐานจนถึงขั้นสูง</p>
                <p>E3.series เป็นซอฟต์แวร์ของ Zuken สำหรับออกแบบระบบไฟฟ้า (E3.schematic), ระบบสายไฟ/สายเคเบิล (E3.cable) และแผงควบคุม (E3.panel) — ใช้กันแพร่หลายในอุตสาหกรรมยานยนต์ เครื่องจักรอุตสาหกรรม และระบบราง</p>
            </section>

            <section>
                <header class="major"><h2>เลือกโมดูลที่จะเรียน</h2></header>
                <div class="card-grid">
                    <a href="schematic.html" class="card">
                        <div class="icon">🧩</div>
                        <h3>Schematics</h3>
                        <p>รู้จักหน้าตาโปรแกรม, Symbol/Component/Device, Item Designation ตามมาตรฐาน IEC 81346, การสร้างวงจรแรกและตรวจสอบความถูกต้อง</p>
                    </a>
                    <a href="cable.html" class="card">
                        <div class="icon">🔌</div>
                        <h3>Cable</h3>
                        <p>ออกแบบ Wiring &amp; Cable Harness: Mating Connector อัตโนมัติ, Dynamic Cable, Block Function และคำนวณ Bundle</p>
                    </a>
                    <a href="panel.html" class="card">
                        <div class="icon">🗄️</div>
                        <h3>Panel</h3>
                        <p>ออกแบบตู้คอนโทรล (Panel Layout): Mounting Rail, Cable Duct, Terminal Strip, Autoconnect และ 3D Panel</p>
                    </a>
                    <a href="database-editor.html" class="card">
                        <div class="icon">⚙️</div>
                        <h3>Database Editor</h3>
                        <p>สร้าง Symbol, Component และ Model เองเมื่อของมาตรฐานไม่พอ พร้อมตรวจสอบฐานข้อมูลด้วย COM API</p>
                    </a>
                </div>
            </section>

            <section>
                <header class="major"><h2>ระบบเดียว ข้อมูลชุดเดียว</h2></header>
                <div class="features">
                    <article>
                        <div class="icon">🧠</div>
                        <div class="content">
                            <h3>Object-Oriented</h3>
                            <p>Symbol/Component ในฐานข้อมูลกลายเป็น Device เมื่อวางในโปรเจกต์ ทุกโมดูลอ้างอิงข้อมูลชุดเดียวกัน</p>
                        </div>
                    </article>
                    <article>
                        <div class="icon">📋</div>
                        <div class="content">
                            <h3>BOM ตรงแบบเสมอ</h3>
                            <p>ไม่ต้องส่งข้อมูลข้ามโมดูลเอง BOM, Wire List และรายงานต่างๆ อัปเดตตามแบบจริงอัตโนมัติ</p>
                        </div>
                    </article>
                    <article>
                        <div class="icon">🆕</div>
                        <div class="content">
                            <h3>อัพเดท 2026</h3>
                            <p>Search &amp; Replace สำหรับ Texts/Attributes, Update All Models in Project, ปรับปรุง Database Editor และ STEP Import</p>
                        </div>
                    </article>
                </div>
            </section>

            <p class="note">
                <strong>ไฟล์ตัวอย่างจริง:</strong> วางไฟล์โปรเจกต์ <code>.e3s</code> ของคุณไว้ในโฟลเดอร์
                <a href="https://github.com/TomKraiwut/ZukenE3/tree/main/examples">examples/</a> ของ repo นี้ได้ แล้วใส่ลิงก์ดาวน์โหลดในหน้าโมดูลที่เกี่ยวข้อง
            </p>'''

EXTRA_SIDEBAR = '''            <section class="about">
                <header class="major"><h2>วิธีใช้เว็บนี้</h2></header>
                <p>เริ่มที่ <strong>Schematics</strong> ถ้ายังไม่เคยเปิดโปรแกรม จากนั้นไปที่ <strong>Cable</strong> หรือ <strong>Panel</strong> ตามงานที่ทำ และดู <strong>Database Editor</strong> เมื่อของมาตรฐานไม่พอ ต้องสร้าง Symbol/Component/Model เอง</p>
            </section>'''

gs.write("index.html", gs.page_html(TITLE, BODY, None, None, EXTRA_SIDEBAR))

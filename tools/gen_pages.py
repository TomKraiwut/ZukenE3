"""Module hub / standalone pages: schematic hub, cable, panel, database-editor.

Ported verbatim from the original flat schematic.html / cable.html / panel.html /
database-editor.html — no content was rewritten, only relocated.
"""
import gen_site as gs

PAGES = {}

PAGES["schematic"] = {
    "title": "Schematics - Zuken E3.series Tutorial",
    "body": '''    <h1>Schematics: ออกแบบวงจรไฟฟ้าด้วย E3.schematic</h1>
    <p class="lead">
        10 บทเรียงลำดับตามกระบวนการทำงานจริงของวิศวกรออกแบบ (Real-world Engineering Workflow) — เริ่มจากพื้นฐานการสืบค้น/วางอุปกรณ์
        ไปจนถึงการสร้างชิ้นส่วนคลังเองและส่งออกรายงานผลิตจริง
    </p>

    <div class="features">
        <article>
            <div class="icon">🧭</div>
            <div class="content">
                <h3>บทที่ 1–3: พื้นฐาน</h3>
                <p>รู้จักหน้าต่างโปรแกรม จัดการโปรเจกต์ วางอุปกรณ์ และเชื่อมวงจรพร้อม Online Checks</p>
            </div>
        </article>
        <article>
            <div class="icon">🧱</div>
            <div class="content">
                <h3>บทที่ 4–8: ระดับกลาง</h3>
                <p>Fields/Levels, Signal Tree, Search &amp; Replace, Terminal Plan และ Subcircuit สำหรับวงจรใช้ซ้ำ</p>
            </div>
        </article>
        <article>
            <div class="icon">🛠️</div>
            <div class="content">
                <h3>บทที่ 9–10: ขั้นสูง</h3>
                <p>สร้าง Symbol/Component เองใน Database Editor แล้วปิดท้ายด้วยการ Sync และผลิตรายงาน</p>
            </div>
        </article>
    </div>

    <h2>บทเรียนทั้งหมด</h2>
    <div class="card-grid">
        <a href="worksheet-01.html" class="card">
            <div class="icon number">1</div>
            <h3>Project &amp; UI Setup</h3>
            <p>Project/Database/Preview Window, สร้าง-เปิด-บันทึกโปรเจกต์, Zoom/Panning, แทรกชีทแรก</p>
        </a>
        <a href="worksheet-02.html" class="card">
            <div class="icon number">2</div>
            <h3>Placing &amp; Editing Devices</h3>
            <p>ค้นหา/ลากวางจากฐานข้อมูล, Place Objects One-by-One ด้วย <code>N</code>, แก้ Device Properties</p>
        </a>
        <a href="worksheet-03.html" class="card">
            <div class="icon number">3</div>
            <h3>Connecting &amp; Online Checks</h3>
            <p>Connect/Autoconnect, ตรวจตรรกะและ Cross-Section แบบเรียลไทม์, Unconnect vs Delete</p>
        </a>
        <a href="worksheet-04.html" class="card">
            <div class="icon number">4</div>
            <h3>Fields &amp; Levels</h3>
            <p>Field สืบทอด HLA/Location อัตโนมัติ, จัดชั้นแสดงผล 256 Level, Read-Only Level</p>
        </a>
        <a href="worksheet-05.html" class="card">
            <div class="icon number">5</div>
            <h3>Signals &amp; Signal Tree</h3>
            <p>System-Generated vs User-Defined Signal, Signal Tree, Signal Cross-Reference ข้ามชีท</p>
        </a>
        <a href="worksheet-06.html" class="card">
            <div class="icon number">6</div>
            <h3>Global Search &amp; Replace</h3>
            <p>ค้นหา Text/Attribute ปลอดภัย, Search and Replace (<code>Ctrl+H</code>), ค้นหา Component เจอ Device จริง</p>
        </a>
        <a href="worksheet-07.html" class="card">
            <div class="icon number">7</div>
            <h3>Terminals &amp; Terminal Plan</h3>
            <p>Terminal Block และ Jumper, Online Terminal Plan คำนวณ Internal/External Target อัตโนมัติ</p>
        </a>
        <a href="worksheet-08.html" class="card">
            <div class="icon number">8</div>
            <h3>Subcircuits</h3>
            <p>กำหนด Origin, Export/Import <code>.e3p</code>, บันทึกเป็น Database Subcircuit วางได้ในขั้นตอนเดียว</p>
        </a>
        <a href="worksheet-09.html" class="card">
            <div class="icon number">9</div>
            <h3>DBE: สร้าง Symbol</h3>
            <p>เข้าโหมด Database Editor, Symbol Checklist, Component Wizard, Master/Slave Checklist</p>
        </a>
        <a href="worksheet-10.html" class="card">
            <div class="icon number">10</div>
            <h3>Database Sync &amp; Reporting</h3>
            <p>Update all Components/Symbols in project, STEP Import แยกโพรเซส, Report Generator</p>
        </a>
    </div>

    <div class="tip">
        <strong>Tip:</strong> เรียนเรียงตามลำดับ 1 → 10 จะได้ประสบการณ์ใกล้เคียงกับการทำงานจริงที่สุด แต่ถ้าต้องการทบทวนเฉพาะเรื่อง
        คลิกเข้าบทที่สนใจจากเมนูด้านขวาได้โดยตรงเช่นกัน
    </div>''',
}

PAGES["cable"] = {
    "title": "Cable - Zuken E3.series Tutorial",
    "body": '''    <h1>Cable: ออกแบบ Wiring &amp; Cable Harness ด้วย E3.cable</h1>
    <p class="lead">
        E3.cable ต่อยอดจาก E3.schematic — ใช้ Symbol/Connection ชุดเดียวกัน แต่เพิ่มความสามารถเฉพาะสำหรับงาน Harness
        ที่ต้องผลิตจริง เช่น Mating Connector, Dynamic Cable และ Block Function
    </p>

    <h2>1. Mating Connector อัตโนมัติ</h2>
    <p>
        เมื่อลาก Connection เข้าฝั่งตัวเมีย/ตัวผู้ของ Connector Device ระบบจะวาง <strong>Active Mating Connector</strong>
        ที่กำหนดไว้ใน Component Properties ให้อัตโนมัติ — ถ้ายังไม่ได้กำหนด Active Mating Connector ไว้ จะไม่สามารถสร้าง
        Connection ได้ และมีข้อความแจ้งเตือนที่ Status Bar
    </p>
    <ul>
        <li><strong>Plug Connector Only on Valid Connector</strong> — บังคับให้เสียบได้เฉพาะ Mating Connector ที่กำหนดไว้ใน Component Properties เท่านั้น</li>
        <li><strong>Plugging Only with Compatible Pin Gender</strong> — บังคับให้เสียบได้เฉพาะขั้วที่เข้ากันได้ (Pin Gender ตรงกัน) ป้องกัน Harness ผิดตั้งแต่ขั้นออกแบบ</li>
    </ul>
    <div class="note">
        <strong>ข้อควรรู้:</strong> ถ้าเปลี่ยนการตั้งค่า Pin Gender ภายหลัง จะไม่กระทบ Connector ที่เสียบกันไปแล้วในโปรเจกต์ — ต้องตรวจ Connection เดิมด้วยตาอีกครั้งถ้าจำเป็น
    </div>

    <h2>2. Dynamic Cable</h2>
    <p>
        ต่างจาก Database Cable (Component ที่ดึงจากฐานข้อมูลตายตัว) <strong>Dynamic Cable</strong> ปรับจำนวนแกนสาย
        (Conductor) และชื่อได้อิสระในโปรเจกต์เอง (Insert → Cable) เหมาะกับกรณีที่ยังไม่รู้จำนวนแกนแน่ชัดตอนออกแบบ
    </p>
    <ul>
        <li>กำหนด Cross-Section, เส้นผ่านศูนย์กลาง และสีของแต่ละแกนได้ภายหลังใน Device Properties</li>
        <li>ลาก Drag&Drop ย้ายแกนสายระหว่าง Dynamic Cable สองเส้น หรือจากโฟลเดอร์ "Wires" เข้า Dynamic Cable ได้ (ทำกับ Database Cable ไม่ได้)</li>
        <li>Rename แกนสายเป็นชุดด้วยคำสั่ง <strong>Rename conductors/wires</strong> โดยกำหนดค่าเริ่มต้น–ค่าสิ้นสุด</li>
        <li>แสดงแกนสายเป็นแบบ Shielded, Bundled หรือ Twisted ได้ใน Device Tree</li>
    </ul>

    <h2>3. Reuse วงจรด้วย Block Function (Dynamic Block)</h2>
    <p>
        Dynamic Block ใช้แทนฟังก์ชันที่ยังไม่นิยามครบ (Black Box) ในผังสาย — เป็นบล็อกที่ยังไม่มีอยู่ในฐานข้อมูลชิ้นส่วนและ
        <em>ไม่</em> นับรวมใน BOM แต่ยังตั้ง Item Designation ให้ได้ ตั้งแต่เวอร์ชัน 2016 วาง Terminal, Connector และ Device
        ไว้ข้างในบล็อกได้ ไม่ใช่แค่ Block Connector บนขอบเหมือนเดิม
    </p>
    <p>
        ถ้าต้องการให้บล็อกถูกนับใน BOM จริง ให้สร้างเป็น <strong>Component ชนิด Block</strong> ในฐานข้อมูลแทน — ดูวิธีสร้างที่หน้า
        <a href="database-editor.html">Database Editor</a> — กำหนด Block Connector ล่วงหน้า และเลือก Symbol Type เป็น "Block"
        (ปรับขนาดได้หลังวาง) หรือ "Block fix" (ขนาดคงที่)
    </p>

    <h2>4. คำนวณเส้นผ่านศูนย์กลางมัดสาย (Bundle)</h2>
    <p>โปรเจกต์ที่มี Wire หลายเส้นเดินเส้นทางเดียวกันในโลกจริง ควรจัดกลุ่มเป็น Bundle เดียวเพื่อดู Net Segment Diameter รวม</p>
    <pre><code>-- แนวคิดข้อมูล Bundle
Bundle "Motor_Harness_01"
  Wires: 12
  Core size: 0.75 mm^2 (each)
  Calculated bundle diameter: ~9.2 mm
</code></pre>
    <p><strong>คำถามฝึกคิด:</strong> ทำไมต้องคำนวณเส้นผ่านศูนย์กลาง Bundle ตั้งแต่ขั้นออกแบบ ทั้งที่ยังไม่ได้ผลิตสายจริง?</p>
    <div class="tip"><strong>เฉลย:</strong> ขนาด Bundle ที่แท้จริงมีผลต่อการเลือกท่อร้อยสาย (Conduit) และ Cable Duct ในตู้ควบคุม/เครื่องจักร (ดูเพิ่มเติมที่หน้า <a href="panel.html">Panel</a>) ถ้าคำนวณผิดตั้งแต่แบบ อาจเจอปัญหาสายเดินไม่พอที่ตอนประกอบจริง ซึ่งแก้ไขยากและแพงกว่าการแก้ในขั้นออกแบบมาก</div>

    <div class="tip">
        <strong>Tip:</strong> ตั้งชื่อ Sheet, Wire Label และ Cable ให้เป็นระบบเดียวกันทั้งโปรเจกต์ (เช่น กำหนด Naming Convention
        ตั้งแต่ต้น) เพราะเมื่อโปรเจกต์มีหลายร้อยชีท การไล่หา Cross-Reference จะยากมากถ้าตั้งชื่อไม่เป็นระบบ
    </div>

    <div class="page-nav">
        <a href="worksheet-10.html">← ก่อนหน้า: บทที่ 10</a>
        <a href="panel.html">ถัดไป: Panel →</a>
    </div>''',
}

PAGES["panel"] = {
    "title": "Panel - Zuken E3.series Tutorial",
    "body": '''    <h1>Panel: ออกแบบเลย์เอาต์ตู้คอนโทรล (E3.panel)</h1>
    <p class="lead">
        E3.panel ใช้ข้อมูล Symbol/Component ชุดเดียวกับ Schematic มาจัดวางเป็นแบบติดตั้งจริงบน Mounting Plate
        พร้อมคำนวณพื้นที่ Mounting Rail และ Cable Duct ให้อัตโนมัติ
    </p>

    <h2>1. สร้าง Panel Sheet</h2>
    <p>
        สั่ง Insert → Sheet แล้วเลือก Type เป็น <strong>Panel</strong> (เปลี่ยนชนิดภายหลังไม่ได้) จากนั้นกำหนด Region
        (พื้นที่ของ "Panel World" ที่ชีทนี้ครอบคลุม) ด้วยค่า Reference X/Y และ Scale ถ้าเลือก Scale เป็น Automatic
        ระบบจะคำนวณจากพื้นที่ที่เลือกให้เอง
    </p>
    <div class="note">
        <strong>ข้อควรระวัง:</strong> ถ้ามีหลาย Panel Sheet ห้ามให้พื้นที่ (Region) ทับกัน ไม่งั้นอาจเกิด "วางอุปกรณ์ทับอุปกรณ์"
        โดยไม่รู้ตัว และคำนวณความยาวสายผิดเมื่อ Routing ข้ามชีทที่ทับกัน — ตั้งแต่เวอร์ชัน 2025 โปรแกรมช่วยหาพื้นที่ว่างให้
        อัตโนมัติเมื่อสร้าง Panel Sheet ใหม่
    </div>

    <h2>2. วาง Model และจัดตำแหน่ง</h2>
    <p>
        แต่ละ Component ที่จะโชว์ใน Panel ต้องมี <strong>Model</strong> (รูปทรง 2D/3D สำหรับใช้ในผัง Panel) ผูกไว้ ค้นหาและวาง
        Model ได้จาก Component Tree เช่นเดียวกับ Schematic แล้วจัดตำแหน่งด้วยเครื่องมือ Align (Toolbar, Context Menu
        หรือกรอกระยะห่างเป็นตัวเลขตรงๆ) ระบบตรวจ Model Overlapping และเช็คว่า Model วางพอดีกับ Slot ให้อัตโนมัติ
    </p>

    <h2>3. Mounting Rail และ Cable Duct</h2>
    <table>
        <tr><th>Object</th><th>ใช้ทำอะไร</th></tr>
        <tr><td><strong>Dynamic Mounting Rail</strong></td><td>สร้างจาก Insert → Mount กำหนดความยาวด้วยการลากเมาส์ — <em>ไม่นับใน BOM</em> ต่างจาก Mounting Rail แบบ Component ที่ดึงจากฐานข้อมูล</td></tr>
        <tr><td><strong>Dynamic Cable Duct</strong></td><td>ราง/ท่อร้อยสายที่ปรับขนาดได้อิสระ ระบบแสดง Fill Size (สัดส่วนพื้นที่ที่ใช้ไปจริง) พร้อม Correction Factor สำหรับพื้นที่ที่ต้องเผื่อ</td></tr>
        <tr><td><strong>Cable Duct Inlet/Outlet</strong></td><td>จุดเข้า-ออกของ Cable Duct ใช้ตอน Routing เพื่อบอกเส้นทางสายจริง</td></tr>
    </table>
    <p>เมื่อรางแน่นเกินไป Highlight Connected Cable Ducts และ Fill Size จะช่วยดูได้ทันทีว่ารางเส้นไหนใกล้เต็ม ก่อนเดินสายจริงในกระบวนการผลิต</p>

    <h2>4. Terminal Strip บน Panel</h2>
    <p>
        Terminal ที่วางใน Schematic จะปรากฏใน Panel ด้วยเช่นกัน (เชื่อมโยงเป็น Object เดียวกันแบบ Object-Oriented)
        สามารถ <strong>Merge Individual Terminals into Multi-Level Terminal</strong> เพื่อรวมขั้วต่อหลายชั้นเป็นบล็อกเดียว
        และใช้ <strong>Automatically Supply Terminal Strips with Additional Parts</strong> เพื่อเติมอุปกรณ์เสริม เช่น End Plate
        หรือ Partition ให้ Terminal Strip โดยไม่ต้องวางเองทีละชิ้น
    </p>

    <h2>5. Panel Autoconnect และมุมมอง 3D</h2>
    <p>
        <strong>Panel Autoconnect</strong> เดินเส้น Wire ในผัง Panel ให้อัตโนมัติตามเส้นทาง Mounting Rail/Cable Duct ที่วางไว้
        กำหนด Routing Offset และเงื่อนไขเลือก Wire ที่จะให้ Autoconnect จัดการได้ ช่วยลดเวลาการลากสายด้วยมือทีละเส้นเมื่อ
        Panel มีอุปกรณ์จำนวนมาก ส่วน <strong>3D Panel Display</strong> แสดงตู้คอนโทรลเป็นโมเดล 3 มิติจริง (รองรับ Import STEP)
        ใช้ตรวจระยะห่างและการชนกันทางกายภาพก่อนผลิตจริง
    </p>

    <div class="tip">
        <strong>Tip:</strong> ถ้ายังไม่มี Model ของอุปกรณ์ที่ต้องการ สร้างเองได้ที่หน้า
        <a href="database-editor.html">Database Editor</a> — ลำดับ Slot ที่ผิดตอนสร้าง Model เป็นสาเหตุอันดับต้นๆ
        ที่ทำให้ Autoconnect หาเส้นทางไม่เจอ
    </div>

    <h2>6. ตัวอย่างฝึกทำ</h2>
    <h3>Terminal Strip บน Panel เชื่อมกับสายจาก Schematic</h3>
    <p><strong>โครงสร้าง:</strong> <code>Terminal Strip 12 ขั้ว บน Panel Sheet เชื่อมสัญญาณจาก Schematic 3 ชีท</code></p>
    <ul>
        <li>วาง Terminal Component ชนิดเดียวกัน 12 ครั้งจาก Schematic → รวมเป็น Terminal Strip เดียวโดยอัตโนมัติ</li>
        <li>Terminal Strip เดียวกันนี้ปรากฏใน Panel Sheet ด้วย (Object เดียวกัน ไม่ต้องสร้างซ้ำ)</li>
    </ul>
    <p><strong>คำถามฝึกคิด:</strong> วาง Terminal Strip บน Mounting Rail ใน Panel แล้ว แต่สั่ง Panel Autoconnect แล้วสายบางเส้นไม่ถูกเดินให้ เกิดจากอะไรได้บ้าง?</p>
    <div class="tip"><strong>เฉลย:</strong> สาเหตุที่พบบ่อยคือ Slot/Pin ของ Model ที่ผูกกับ Terminal นั้นเรียงลำดับผิดตอนสร้างใน Database Editor หรือ Wire เส้นนั้นไม่ตรงกับเงื่อนไข Wire Selection ที่ตั้งไว้ใน Autoconnect Settings — ให้ตรวจ Slot Order ของ Model ก่อน แล้วค่อยไล่ดู Autoconnect Settings</div>

    <div class="page-nav">
        <a href="cable.html">← ก่อนหน้า: Cable</a>
        <a href="database-editor.html">ถัดไป: Database Editor →</a>
    </div>''',
}

PAGES["database-editor"] = {
    "title": "Database Editor - Zuken E3.series Tutorial",
    "body": '''    <h1>Database Editor: สร้าง Symbol, Component และ Model เอง</h1>
    <p class="lead">
        เมื่อของมาตรฐานในฐานข้อมูลไม่พอ ใช้ Database Editor สร้าง Symbol/Component ใหม่สำหรับ Schematic/Cable
        และสร้าง Model ใหม่สำหรับ Panel — ทุกอย่างอ้างอิงข้อมูลชุดเดียวกันทั้งระบบ
    </p>

    <h2>1. เปิดใช้งาน Database Editor</h2>
    <p>
        เปิดได้จากคำสั่ง <strong>New Symbol</strong> / <strong>New Component</strong> ในเมนูคลิกขวาของ Database Window
        โปรแกรมจะเปิดหน้าต่างแยกต่างหาก สังเกตได้จากชื่อ <code>E3.dbe</code> บน Title Bar — โหมดนี้แก้ไข "ต้นแบบ" ในฐานข้อมูล
        โดยไม่กระทบ Device ที่วางไปแล้วในโปรเจกต์ และยังเปิดโปรเจกต์คู่ขนานไปพร้อมกันได้ (แยกสีหน้าต่างให้เห็นชัดว่าอยู่โหมดไหน)
    </p>
    <div class="note">
        <strong>ก่อนเริ่ม:</strong> อย่าสร้าง Symbol/Component/Model ใหม่ซ้ำกับที่มีอยู่แล้ว — ค้นหาในฐานข้อมูลก่อนเสมอ และถ้าต้อง
        แก้ไขของเดิม ใช้คำสั่ง <strong>Symbol/Component Edit</strong> แล้วบันทึกทับชื่อเดิม ไม่ใช่สร้างใหม่ซ้ำซ้อน
    </div>

    <h2>2. สร้าง Symbol ใหม่ (สำหรับ Schematic/Cable)</h2>
    <p><strong>Symbol Checklist:</strong></p>
    <ol class="steps">
        <li>กำหนด Symbol Properties — ชนิดและชื่อ Symbol</li>
        <li>Insert Symbol Graphic (รองรับ Import DXF/DWG) — กราฟิกแก้ไขไม่ได้อีกในโหมด Project</li>
        <li>วาง Node บนตำแหน่งที่ต้องการให้ Connection เข้ามาต่อ พร้อมกำหนดทิศทางการเชื่อมต่อ (Connection Direction)</li>
        <li>วาง Text Placeholder สำหรับข้อมูลที่ระบบ/ผู้ใช้จะเติมทีหลัง เช่น Item Designation</li>
        <li>ตรวจสอบ/กำหนด Space Requirement และ Symbol Origin (จุดอ้างอิงตอนวาง)</li>
    </ol>
    <p>
        ส่วน <strong>Component</strong> ผูก Symbol เข้ากับข้อมูลอุปกรณ์จริง (Manufacturer, Part Number, จำนวนขา) — ฐานข้อมูลของ
        E3.series รองรับ Component หลายชนิดที่มีพฤติกรรมต่างกัน เลือกใช้ให้ตรงกับลักษณะอุปกรณ์จริง:
    </p>
    <table>
        <tr><th>Component Type</th><th>ใช้กับ</th></tr>
        <tr><td>Cable / Wire Group</td><td>สายเคเบิลหรือกลุ่มสายที่มีจำนวนแกนคงที่ ดึงจากฐานข้อมูลได้ทันที</td></tr>
        <tr><td>Terminal</td><td>ขั้วต่อบน Terminal Strip</td></tr>
        <tr><td>Connector</td><td>ปลั๊ก/ขั้วต่อหลายขา รองรับ Mating Connector, Cavity Part Group</td></tr>
        <tr><td>Busbar</td><td>บัสบาร์ตัวนำกระแสรวม</td></tr>
        <tr><td>Subcircuit</td><td>วงจรย่อยสำเร็จรูปที่ผูกไว้กับ Component เพื่อดึงมาวางซ้ำได้</td></tr>
        <tr><td>Assembly / Block</td><td>กลุ่มอุปกรณ์ที่ประกอบเป็นชุดเดียว หรือ Block ที่มี Block Connector สำหรับงาน Cable Harness</td></tr>
    </table>

    <h2>3. สร้าง Model ใหม่ (สำหรับ Panel)</h2>
    <p>
        Model คือรูปทรง 2D/3D ของ Component ที่ใช้แสดงในผัง <a href="panel.html">Panel</a> — ต่างจาก Symbol ที่ใช้ใน Schematic
        เปิดจากคำสั่งเดียวกัน (New Symbol/New Component) แต่เลือกสร้าง Model ต่อในขั้นตอนถัดไป
    </p>
    <p><strong>Model Checklist:</strong></p>
    <ol class="steps">
        <li>กำหนด Model Properties</li>
        <li>กำหนด Space Requirement (พื้นที่ครอบครองบนแนวแกน X/Y)</li>
        <li>Insert Graphics — รองรับ Import STEP File สำหรับมุมมอง 3D</li>
        <li>วาง Node (Slot/Pin) และ<strong>ตรวจลำดับ Slot ให้ถูกต้อง</strong></li>
    </ol>
    <div class="tip">
        <strong>Tip:</strong> ลำดับ Slot ที่ผิดเป็นสาเหตุอันดับต้นๆ ที่ทำให้ Panel Autoconnect หาเส้นทางไม่เจอ — ตรวจ Slots/Pins Tab
        ให้ครบก่อนบันทึก Model ทุกครั้ง
    </div>

    <h2>4. ตรวจสอบฐานข้อมูลด้วย COM API (เสริม)</h2>
    <p>
        นอกจากแก้ไขในหน้าต่าง Database Editor แล้ว E3.series ยังมี COM API (E3.Application) ให้เขียน Macro ตรวจสอบข้อมูลอัตโนมัติ
        เช่น ไล่ตรวจว่า Symbol ตัวไหนในโปรเจกต์ยังไม่ผูก Part — เหมาะกับงาน QA ก่อนส่งแบบ มากกว่าการแทนที่ Database Editor
    </p>
    <pre><code>' ตัวอย่าง Macro (VBA-like) ตรวจสอบ Symbol ที่ยังไม่ผูก Part Number
Dim e3 As Object
Dim job As Object
Dim sym As Object
Dim symbols() As Long
Dim i As Integer

Set e3 = GetObject(, "CT.Application")
Set job = e3.CreateJobObject
job.GetAllSymbolIds symbols

For i = 0 To UBound(symbols)
    Set sym = e3.CreateSymbolObject
    sym.SetId symbols(i)
    If sym.GetPartId() = 0 Then
        Debug.Print "Missing part: " & sym.GetName()
    End If
Next i
</code></pre>

    <div class="page-nav">
        <a href="panel.html">← ก่อนหน้า: Panel</a>
        <a href="index.html">กลับหน้าแรก</a>
    </div>''',
}

for _slug, _page in PAGES.items():
    gs.write(f"{_slug}/index.html", gs.page_html(_page["title"], _page["body"], _slug, None))

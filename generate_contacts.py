from pathlib import Path

import segno
from PIL import Image, ImageOps


BASE_URL = "https://crbc-nigeria.github.io/crbc-contacts"
ROOT = Path(__file__).resolve().parent
CONTACTS_DIR = ROOT / "contacts"
PAGES_DIR = ROOT / "c"
QR_DIR = ROOT / "qr"
BRAND_QR_LOGO = ROOT / "assets" / "crbc-rb-logo-stacked.png"
BRAND_QR_MARK = ROOT / "assets" / "crbc-rb-mark.png"

CN_COMPANY_YI = "中国路桥尼日利亚子公司"
CN_COMPANY = "中国路桥尼日利亚有限责任公司"
EN_COMPANY = "CRBC Nigeria Ltd"
WEBSITE = "http://www.crbc.com"


CONTACTS = [
    {
        "slug": "yi-wenwen",
        "cn_name": "易文文",
        "en_name": "Allison Yi",
        "cn_title": "市场开发部门副经理",
        "en_title": "Deputy Director (Business Development)",
        "cn_company": CN_COMPANY_YI,
        "en_company": EN_COMPANY,
        "mobile": "+234 810 853 1303",
        "whatsapp": "+234 810 853 1303",
        "email": "yiww@crbc.com",
        "extra_emails": ["aweallison@gmail.com"],
    },
    {
        "slug": "zhou-hao",
        "cn_name": "周昊",
        "en_name": "Zhou Hao",
        "cn_title": "总经理 / 高级工程师",
        "en_title": "Managing Director / Senior Engineer",
        "cn_company": CN_COMPANY,
        "en_company": EN_COMPANY,
        "mobile": "+234 913 373 9488",
        "whatsapp": "+234 908 548 8888",
        "email": "zhouh@crbc.com",
        "extra_emails": [],
    },
    {
        "slug": "guo-xi",
        "cn_name": "郭喜",
        "en_name": "Ethan Guo",
        "cn_title": "副总经理 / 高级工程师",
        "en_title": "Deputy Managing Director / Senior Engineer",
        "cn_company": CN_COMPANY,
        "en_company": EN_COMPANY,
        "mobile": "+234 913 374 8207",
        "whatsapp": "+234 818 656 4319",
        "email": "guox@crbc.com",
        "extra_emails": [],
    },
    {
        "slug": "zhang-jingxuan",
        "cn_name": "张竟璇",
        "en_name": "Steven Zhang",
        "cn_title": "物资装备部经理 / 办公室主任",
        "en_title": "Supply Chain Manager / Office Director",
        "cn_company": CN_COMPANY,
        "en_company": EN_COMPANY,
        "mobile": "+234 702 558 0323",
        "whatsapp": "+234 702 558 0323",
        "email": "zhangjx@crbc.com",
        "extra_emails": [],
    },
    {
        "slug": "meng-ligang",
        "cn_name": "孟丽刚",
        "en_name": "William Meng",
        "cn_title": "副总经理",
        "en_title": "Deputy Managing Director",
        "cn_company": CN_COMPANY,
        "en_company": EN_COMPANY,
        "mobile": "+234 915 659 4034",
        "whatsapp": "+234 915 659 4034",
        "email": "menglg@crbc.com",
        "extra_emails": [],
    },
    {
        "slug": "deng-zhilin",
        "cn_name": "邓智临",
        "en_name": "Eric Deng",
        "cn_title": "财务经理",
        "en_title": "Financial Manager",
        "cn_company": CN_COMPANY,
        "en_company": EN_COMPANY,
        "mobile": "+234 809 762 7000",
        "whatsapp": "+234 809 762 7000",
        "email": "dengzl@crbc.com",
        "extra_emails": [],
    },
    {
        "slug": "fu-lei",
        "cn_name": "符磊",
        "en_name": "James Fu",
        "cn_title": "财务总监",
        "en_title": "Chief Financial Officer",
        "cn_company": CN_COMPANY,
        "en_company": EN_COMPANY,
        "mobile": "+234 916 595 9389",
        "whatsapp": "+234 916 595 9389",
        "email": "ful@crbc.com",
        "extra_emails": [],
    },
]


def compact_phone(value: str) -> str:
    return value.replace(" ", "").replace("+", "")


def split_en_name(name: str) -> str:
    parts = name.split()
    if len(parts) >= 2:
        return f"{parts[-1]};{' '.join(parts[:-1])};;;"
    return f"{name};;;;"


def split_cn_name(name: str) -> str:
    if len(name) >= 2:
        return f"{name[0]};{name[1:]};;;"
    return f"{name};;;;"


def vcard(contact: dict, lang: str) -> str:
    is_cn = lang == "cn"
    name = contact["cn_name"] if is_cn else contact["en_name"]
    title = contact["cn_title"] if is_cn else contact["en_title"]
    company = contact["cn_company"] if is_cn else contact["en_company"]
    n_value = split_cn_name(name) if is_cn else split_en_name(name)
    lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N;CHARSET=UTF-8:{n_value}",
        f"FN;CHARSET=UTF-8:{name}",
        f"ORG;CHARSET=UTF-8:{company}",
        f"TITLE;CHARSET=UTF-8:{title}",
        f"TEL;TYPE=CELL,VOICE:{contact['mobile']}",
        f"TEL;TYPE=CELL,WHATSAPP:{contact['whatsapp']}",
        f"EMAIL;TYPE=WORK:{contact['email']}",
    ]
    for email in contact["extra_emails"]:
        lines.append(f"EMAIL;TYPE=HOME:{email}")
    lines.extend(
        [
            f"URL:https://wa.me/{compact_phone(contact['whatsapp'])}",
            f"NOTE:WhatsApp: {contact['whatsapp']}",
            "END:VCARD",
            "",
        ]
    )
    return "\n".join(lines)


def page_html(contact: dict) -> str:
    cn_title_lines = contact["cn_title"].replace(" / ", "<br>")
    en_title_lines = contact["en_title"].replace(" / ", "<br>")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{contact['en_name']} / {contact['cn_name']}</title>
  <link rel="stylesheet" href="../../styles.css">
</head>
<body>
  <main>
    <img class="logo" src="../../assets/crbc-logo.png" alt="China Road and Bridge Corporation">
    <h1><span class="primary-text">{contact['en_name']}</span><span class="secondary-text">{contact['cn_name']}</span></h1>
    <p class="role"><span class="primary-text">{en_title_lines}</span><span class="secondary-text">{cn_title_lines}</span></p>
    <p class="role"><span class="primary-text">{contact['en_company']}</span><span class="secondary-text">{contact['cn_company']}</span></p>
    <a class="primary" href="../../contacts/{contact['slug']}-en.vcf" download>Add English Contact</a>
    <a class="secondary" href="../../contacts/{contact['slug']}-cn.vcf" download>添加中文联系人</a>
    <p class="meta">If the contact does not open automatically, download the card and open it from your phone.</p>
  </main>
</body>
</html>
"""


def index_html() -> str:
    links = "\n".join(
        f'    <a href="./c/{contact["slug"]}/">{contact["en_name"]} / {contact["cn_name"]}</a>'
        for contact in CONTACTS
    )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CRBC Contacts</title>
  <link rel="stylesheet" href="./styles.css">
</head>
<body>
  <main>
    <img class="logo" src="./assets/crbc-logo.png" alt="China Road and Bridge Corporation">
    <h1>CRBC Contacts</h1>
    <p class="role">请选择联系人名片。<br>Please choose a contact card.</p>
{links}
  </main>
</body>
</html>
"""


def write_styles() -> None:
    (ROOT / "styles.css").write_text(
        """html {
  background: #f6f7f9;
}
:root {
  color-scheme: light;
  font-family: Arial, "Microsoft YaHei", sans-serif;
  color: #20242a;
}
body {
  margin: 0;
  min-height: 100vh;
  display: grid;
  place-items: start center;
  padding: 18px 20px 24px;
}
main {
  width: min(520px, 100%);
  background: #fff;
  border: 1px solid #e2e6ec;
  border-radius: 8px;
  padding: 22px 24px 26px;
  box-shadow: 0 12px 36px rgba(22, 34, 51, 0.08);
}
.logo {
  display: block;
  width: min(100%, 440px);
  height: auto;
  margin: 0 auto 22px;
}
h1 {
  margin: 0 0 6px;
  font-size: 26px;
  line-height: 1.25;
}
.role {
  margin: 0 0 22px;
  color: #606874;
  line-height: 1.5;
}
.primary-text {
  display: block;
  font-family: "Times New Roman", Times, serif;
  font-weight: 700;
  color: #20242a;
}
.secondary-text {
  display: block;
  font-family: "方正仿宋_GBK", "FangSong", "仿宋", serif;
  color: #75808d;
  font-weight: 400;
}
a {
  display: block;
  padding: 15px 16px;
  margin-top: 12px;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 700;
  text-align: center;
}
.primary,
main > a {
  background: #0b5cab;
  color: #fff;
}
.secondary {
  background: #e9eef5;
  color: #1f2c3d;
}
.meta {
  margin: 20px 0 0;
  font-size: 13px;
  color: #75808d;
  line-height: 1.5;
}
""",
        encoding="utf-8",
        newline="\n",
    )


def save_qr(contact: dict) -> None:
    url = f"{BASE_URL}/c/{contact['slug']}/"
    qr = segno.make(url, error="h", micro=False)
    plain_png = QR_DIR / f"{contact['slug']}-page.png"
    branded_png = QR_DIR / f"{contact['slug']}-page-branded.png"
    qr.save(plain_png, scale=26, border=4, dark="black", light="white")
    qr.save(QR_DIR / f"{contact['slug']}-page.svg", scale=1, border=4, dark="black", light="white")
    if BRAND_QR_LOGO.exists():
        add_center_logo(plain_png, branded_png)
        add_blank_center_logo(plain_png, QR_DIR / f"{contact['slug']}-page-blank-logo.png")


def get_qr_mark() -> Image.Image:
    if BRAND_QR_MARK.exists():
        return Image.open(BRAND_QR_MARK).convert("RGBA")
    logo = Image.open(BRAND_QR_LOGO).convert("RGBA")
    mark = logo.crop((90, 0, 890, 510))
    bbox = mark.getbbox()
    if bbox:
        mark = mark.crop(bbox)
    mark.save(BRAND_QR_MARK)
    return mark


def add_center_logo(qr_path: Path, output_path: Path) -> None:
    qr_img = Image.open(qr_path).convert("RGBA")
    logo = Image.open(BRAND_QR_LOGO).convert("RGBA")

    qr_w, qr_h = qr_img.size
    badge_size = int(min(qr_w, qr_h) * 0.20)
    logo_size = int(badge_size * 0.78)

    badge = Image.new("RGBA", (badge_size, badge_size), "white")
    logo_canvas = Image.new("RGBA", (logo_size, logo_size), (255, 255, 255, 0))
    contained = ImageOps.contain(logo, (logo_size, logo_size), method=Image.Resampling.LANCZOS)
    logo_canvas.alpha_composite(
        contained,
        ((logo_size - contained.width) // 2, (logo_size - contained.height) // 2),
    )
    badge.alpha_composite(logo_canvas, ((badge_size - logo_size) // 2, (badge_size - logo_size) // 2))

    x = (qr_w - badge_size) // 2
    y = (qr_h - badge_size) // 2
    qr_img.alpha_composite(badge, (x, y))
    qr_img.convert("RGB").save(output_path, dpi=(600, 600))


def add_blank_center_logo(qr_path: Path, output_path: Path) -> None:
    qr_img = Image.open(qr_path).convert("RGBA")
    logo = get_qr_mark()

    qr_w, qr_h = qr_img.size
    blank_size = int(min(qr_w, qr_h) * 0.24)
    blank_size -= blank_size % 2
    logo_size = int(blank_size * 0.74)
    logo_size -= logo_size % 2

    x = (qr_w - blank_size) // 2
    y = (qr_h - blank_size) // 2
    qr_img.alpha_composite(Image.new("RGBA", (blank_size, blank_size), "white"), (x, y))

    contained = ImageOps.contain(logo, (logo_size, logo_size), method=Image.Resampling.LANCZOS)
    qr_img.alpha_composite(
        contained,
        (x + (blank_size - contained.width) // 2, y + (blank_size - contained.height) // 2),
    )
    qr_img.convert("RGB").save(output_path, dpi=(600, 600))


def main() -> None:
    CONTACTS_DIR.mkdir(exist_ok=True)
    PAGES_DIR.mkdir(exist_ok=True)
    QR_DIR.mkdir(exist_ok=True)
    write_styles()
    (ROOT / "index.html").write_text(index_html(), encoding="utf-8", newline="\n")
    for contact in CONTACTS:
        (CONTACTS_DIR / f"{contact['slug']}-cn.vcf").write_text(vcard(contact, "cn"), encoding="utf-8", newline="\n")
        (CONTACTS_DIR / f"{contact['slug']}-en.vcf").write_text(vcard(contact, "en"), encoding="utf-8", newline="\n")
        page_dir = PAGES_DIR / contact["slug"]
        page_dir.mkdir(exist_ok=True)
        (page_dir / "index.html").write_text(page_html(contact), encoding="utf-8", newline="\n")
        save_qr(contact)
        print(f"{contact['cn_name']} / {contact['en_name']}: {BASE_URL}/c/{contact['slug']}/")


if __name__ == "__main__":
    main()

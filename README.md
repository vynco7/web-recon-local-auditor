# 🛡️ Web Recon Local Auditor

Toolkit Python ini digunakan untuk **mengaudit keamanan web lokal** dengan cara:
- Menelusuri seluruh halaman web
- Mendeteksi file sensitif seperti `.env`, `.sql`, `.bak`
- Menyimpan semua halaman ke folder lokal `dump/`
- Memberikan ringkasan dalam tampilan CLI yang keren (pakai `rich`)

> ⚠️ Gunakan hanya untuk pengujian sistem milikmu sendiri!

---

## 🚀 Cara Jalankan

1. Clone repositori ini:
```bash
git clone https://github.com/username/web-recon-local-auditor.git
cd web-recon-local-auditor
Install dependency:

bash
Salin
Edit
pip install -r requirements.txt
Jalankan tools:

bash
Salin
Edit
python web_recon_local_auditor.py
📂 Output
Semua HTML halaman akan disimpan di folder dump/

File sensitif akan dideteksi dan ditampilkan

💻 Contoh Tampilan CLI
bash
Salin
Edit
┌────────────────────────────────────────────┐
│   🛡️ WEB RECON LOCAL AUDITOR v1            │
├────────────────────────────────────────────┤
│ 🌐 Target      : http://localhost:8000      │
│ 📁 Output      : ./dump/                    │
│ ⚠️ Sensitif    : .env, .sql ditemukan       │
└────────────────────────────────────────────┘
📦 Requirement
Python 3.7+

requests

beautifulsoup4

rich

⚖️ Legal & Etis
Toolkit ini hanya untuk:

Pengujian web pribadi

Audit lab pentest lokal

Pendidikan & pelatihan

Dilarang menggunakan tools ini untuk:

Mengakses sistem orang lain tanpa izin

Melakukan eksploitasi atau injeksi aktif


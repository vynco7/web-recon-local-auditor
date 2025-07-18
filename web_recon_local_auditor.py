import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import os
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

SENSITIVE_PATTERNS = [
    r"\.env$", r"\.git", r"\.bak$", r"\.sql$", r"\.zip$", r"\.tar\.gz$", r"\.db$",
    r"config\.php$", r"wp-config\.php$"
]

visited = set()
queue = deque()
found_files = []

def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https")

def normalize_url(base, link):
    return urljoin(base, link.split("#")[0])

def is_sensitive(path):
    return any(re.search(pat, path, re.IGNORECASE) for pat in SENSITIVE_PATTERNS)

def save_page(url, html):
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        path = "index"
    filename = f"dump/{path.replace('/', '_')}.html"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    console.print(f"[green]📄 Disimpan: {filename}[/green]")

def crawl(start_url, limit=100):
    queue.append(start_url)
    domain = urlparse(start_url).netloc
    count = 0

    console.print(Panel.fit("🔍 Memulai Audit...", title="Web Recon Auditor", style="bold cyan"))

    while queue and count < limit:
        url = queue.popleft()
        if url in visited or not is_valid_url(url):
            continue

        try:
            res = requests.get(url, timeout=5)
            visited.add(url)
            count += 1

            console.print(f"[blue]🌐 Mengakses: {url}[/blue]")
            save_page(url, res.text)

            if is_sensitive(url):
                console.print(f"[red]⚠️ File sensitif terdeteksi: {url}[/red]")
                found_files.append(url)

            soup = BeautifulSoup(res.text, "html.parser")
            for tag in soup.find_all("a", href=True):
                link = normalize_url(url, tag['href'])
                if domain in link and link not in visited:
                    queue.append(link)

        except Exception as e:
            console.print(f"[yellow]⚠️ Gagal akses: {url} - {e}[/yellow]")

def show_summary():
    console.print("\n[bold cyan]🔍 RINGKASAN HASIL AUDIT:[/bold cyan]")
    table = Table(title="File Sensitif Terdeteksi")
    table.add_column("URL", style="magenta")
    if found_files:
        for f in found_files:
            table.add_row(f)
        console.print(table)
    else:
        console.print("[green]✅ Tidak ditemukan file sensitif.[/green]")

    console.print(f"[blue]🔗 Total halaman dikunjungi: {len(visited)}[/blue]")

def main():
    console.print(Panel.fit("🛡️ WEB RECON LOCAL AUDITOR v1", style="bold green"))
    start_url = console.input("🌍 Masukkan URL target (contoh: http://localhost:8000): ").strip()

    if not is_valid_url(start_url):
        console.print("[red]❌ URL tidak valid.[/red]")
        return

    os.makedirs("dump", exist_ok=True)
    crawl(start_url)
    show_summary()

if __name__ == "__main__":
    main()

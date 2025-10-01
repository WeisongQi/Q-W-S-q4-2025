import os
from datetime import date, datetime

# 1. 创建日期格式的目录
# 1. Erstellen eines Verzeichnisses mit Datumsformat
# folder_name = f"Aufgabe-{date.today().strftime('%d%m%y')}"
# os.makedirs(folder_name, exist_ok=True)

# === 配置区域 ===
# === Konfigurationsbereich ===
config = {
    "prefix": "Aufgabe",  # 目录前缀 / Verzeichnis-Präfix
    # "date_format": "%Y-%m-%d",  # 日期格式 / Datumsformat
    "with_timestamp": False,  # 是否添加时间戳 / Zeitstempel anhängen?
    "base_dir": "C:/Coding/Q-W-S-q3-2025",  # 基础路径 / Basisverzeichnis
    "custom_suffix": "_v1",  # 自定义后缀 / Benutzerdefiniertes Suffix
}
# 可自定义的日期格式选项
# Anpassbare Datumsformat-Optionen
date_formats = {
    "ddmmyy": "%d%m%y",  # 230625（默认）/ Standard
    "ddmmyyyy": "%d%m%Y",  # 23062025
    "ddmmm_yy": "%d%b_%y",  # 23Jun_25
    "yymmdd": "%y%m%d",  # 250623
    "yyyy-mm-dd": "%Y-%m-%d",  # 2025-06-23
}

selected_format = (
    "ddmmyy"  # 在此修改日期格式 / Hier das gewünschte Date Format einstellen
)
# ================

# 生成目录名
# Verzeichnisname generieren
folder_name = (
    config["prefix"] + "-" + date.today().strftime(date_formats[selected_format])
)

if config["with_timestamp"]:
    # 添加时间戳（小时和分钟）/ Zeitstempel (Stunden und Minuten) anhängen
    folder_name += "_" + datetime.now().strftime("%H%M")

# folder_name += config["custom_suffix"]  # 可选：添加自定义后缀 / Optional: Suffix anhängen

# 处理基础路径
# Basisverzeichnis prüfen und ggf. erstellen
if not os.path.exists(config["base_dir"]):
    os.makedirs(config["base_dir"], exist_ok=True)

# 拼接完整路径并创建目录
# Vollständigen Pfad zusammenbauen und Verzeichnis erstellen
full_path = os.path.join(config["base_dir"], folder_name)
os.makedirs(full_path, exist_ok=True)

print(f"Index: {full_path}")

# 2. 创建 readme.md
# 2. readme.md im neuen Verzeichnis erstellen
with open(os.path.join(folder_name, "readme.md"), "w") as f:
    f.write("# Aufgabe Heute\n")

# 3. 用 VS Code 打开文件 (Windows系统)
# 3. Datei mit VS Code öffnen (nur Windows)
os.system(f"code {os.path.join(folder_name, 'readme.md')}")

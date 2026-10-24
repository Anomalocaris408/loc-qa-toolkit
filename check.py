import csv
import re

PLACEHOLDER = re.compile(r"\{[^}]*\}|%[sdf]")

def load_rows(path):
    with open(path, encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))

def check_placeholders(row):
    src = sorted(PLACEHOLDER.findall(row["source"]))
    tgt = sorted(PLACEHOLDER.findall(row["source"]))
    if src != tgt:
        return f"占位符不一致：原文 {src}, 译文 {tgt}"
    return None

def main():
    rows = load_rows("sample_data/sample.csv")
    problems = 0
    for row in rows:
        msg = check_placeholders(row)
        if msg:
            print(f"{row['key']}: {msg}")
            problems += 1
    print(f"共检查 {len(rows)} 条，发现 {problems} 个问题")

main()
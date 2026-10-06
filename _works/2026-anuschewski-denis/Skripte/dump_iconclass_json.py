"""
Load the complete iconclass category data from SQLite and text file sources and write it into a JSON file

To be used with official iconclass data GitHub repo: https://github.com/iconclass/data
Check out linked repo, change into directory and use `python make_sqlite.py && python dump_iconclass_json.py`
"""

import json
import os
import sqlite3


def parse_keywords_from_files(keyword_dir="kw"):
    """Helper method to parse keyword data from text files inside `keyword_dir`"""

    keywords = {}  # notation -> { lang: [keyword1, keyword2, ...] }
    print(f"[+] Parse keywords from '{keyword_dir}'...")
    keyword_count = 0

    for root, _, files in os.walk(keyword_dir):
        for fname in files:
            # Determine language from directory (e.g. kw/de/... -> 'de')
            rel_path = os.path.relpath(root, keyword_dir)
            lang = rel_path.split(os.sep)[0]
            if not lang or lang == ".":
                continue

            fpath = os.path.join(root, fname)

            # Read file line by line
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    # Split by separator "|"
                    parts = line.split("|", maxsplit=1)
                    if len(parts) < 2:
                        continue

                    notation_key = parts[0].strip()
                    keyword = parts[1].strip()

                    if notation_key not in keywords:
                        keywords[notation_key] = {}
                    if lang not in keywords[notation_key]:
                        keywords[notation_key][lang] = []

                    # Append keyword per language
                    if keyword not in keywords[notation_key][lang]:
                        keywords[notation_key][lang].append(keyword)
                        keyword_count += 1

    print(f"[+] {keyword_count} keywords parsed for {len(keywords)} notations.")
    return keywords


db_path="iconclass.sqlite"
output_path="iconclass.json"
keyword_lookup = parse_keywords_from_files()

print(f"[+] Connect to database in '{db_path}'...")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Load modifier keys from SQLite
print("[+] Load modifier keys...")
cursor.execute("""
    SELECT k.code, k.suffix, t.language, t.text
    FROM keys k
    LEFT JOIN texts t ON t.ref = k.id
""")

modifier_lookup = {}
for code, suffix, lang, text in cursor.fetchall():
    # Create complete modifier key (e.g. code='11k', suffix='1' -> key = '11k(+1)')
    key_id = f"{code}(+{suffix})" if suffix else code

    if key_id not in modifier_lookup:
        modifier_lookup[key_id] = {"base_code": code, "suffix": suffix, "text": {}}

    if lang and text:
        if lang not in modifier_lookup[key_id]["text"]:
            modifier_lookup[key_id]["text"][lang] = []

        # Add text if not already present for language
        if text not in modifier_lookup[key_id]["text"][lang]:
            modifier_lookup[key_id]["text"][lang].append(text)

# Load notations from SQLite
print("[+] Load notations and metadata...")
cursor.execute("""
    SELECT n.id, n.notation, n.children, n.key, t.language, t.text
    FROM notations n
    LEFT JOIN texts t ON t.ref = n.id
""")

full_data = {}

# Traverse metadata row by row grouped by `notation`
for n_id, notation, children_str, key_str, lang, text in cursor.fetchall():
    if notation not in full_data:
        # Try to parse children from JSON inside `children_str` (default is empty list)
        try:
            children = (
                json.loads(children_str)
                if children_str and children_str.startswith("[")
                else (
                    [
                        c.strip()
                        for c in children_str.split("|")
                        if c.strip()
                    ]
                    if children_str
                    else []
                )
            )
        except Exception:
            children = []

        # Try to parse keys from JSON inside `key_str` (default is list with key content)
        raw_keys = []
        if key_str:
            try:
                raw_keys = (
                    json.loads(key_str)
                    if key_str.startswith("[")
                    else [
                        k.strip() for k in key_str.split(";") if k.strip()
                    ]
                )
            except Exception:
                raw_keys = [key_str]

        resolved_keys = {}
        for k in raw_keys:
            # 1st try: direct key lookup
            if k in modifier_lookup:
                resolved_keys[k] = modifier_lookup[k]
            else:
                # 2nd try: match via base_code or suffix search
                matched = False
                for key_id, data in modifier_lookup.items():
                    if (
                            data["suffix"] == k
                            or data["base_code"] == k
                            or key_id.endswith(f"(+{k})")
                    ):
                        resolved_keys[key_id] = data
                        matched = True
                if not matched:
                    resolved_keys[k] = {"suffix": k, "text": {}}

        full_data[notation] = {
            "children": children,
            "is_leaf": len(children) == 0,
            "text": {},
            "keywords": keyword_lookup.get(notation, {}),
            "modifiers": resolved_keys,
        }

    # Set text data afterwards grouped by `lang`
    if lang and text:
        full_data[notation]["text"][lang] = text

conn.close()

print(f"[+] Write JSON dump into '{output_path}'...")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(full_data, f, ensure_ascii=False, indent=2)

print(f"[✓] Done! {len(full_data)} notations incl. metadata successfully exported.")

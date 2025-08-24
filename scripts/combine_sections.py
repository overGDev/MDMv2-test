#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Alvaro Orozco
import yaml
from pathlib import Path

SCHEMA_FILE = "schema.yaml"
OUTPUT_FILE = "README.md"

def load_schema():
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def build_document(sections, level=1):
    content = ""
    for section in sections:
        content += f"{'#' * level} {section['title']}\n\n"
        if 'children' in section and section['children']:
            content += build_document(section['children'], level + 1)
    return content

def main():
    if not Path(SCHEMA_FILE).exists():
        print(f"Error: {SCHEMA_FILE} no existe.")
        return

    sections = load_schema()
    document_content = build_document(sections)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(document_content)

    print(f"Documento generado correctamente: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

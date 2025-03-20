from os import path
import os
import shutil
from md_to_blocks import markdown_to_blocks
from md_to_html import markdown_to_html_node

def main():
    copy_static_to_public()

    title = extract_title("# test")
    print(title)

    from_path = "./content/index.md"
    to_path = "./public/"
    template_path = "./template.html"
    generate_page(from_path, template_path, to_path)

def copy_static_to_public():
    public, static = "./public/", "./static/"
    if not path.exists(static):
        raise ValueError(f"{static} path doesnt exist")
    if path.exists(public):
        shutil.rmtree(public)
        print("delete public for recreate it")

    shutil.copytree(static, public)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block[2:].strip()
    raise ValueError("No h1 header found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as md_file:
        md_content = md_file.read()
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    title = extract_title(md_content)
    md_to_html = markdown_to_html_node(md_content).to_html()

    html_to_dest_path = update_template_placeholders(template_content, title, md_to_html)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    dest_file_path = os.path.join(dest_path, "index.html")
    with open(dest_file_path, "w") as html_result:
        html_result.write(html_to_dest_path)

def update_template_placeholders(template_content, title, md_to_html):
    processed_template = template_content.replace("{{ Title }}", title)
    processed_template = processed_template.replace("{{ Content }}", md_to_html)
    return processed_template

main()

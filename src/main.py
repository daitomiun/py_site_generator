from os import path
import os
import shutil
from md_to_blocks import markdown_to_blocks
from md_to_html import markdown_to_html_node

dir_path_static = "./static"
dir_content = "./content"
dir_path_public = "./public"
template_path = "./template.html"

def main():
    print("Deleting public directory and recreating it...")
    copy_static_to_public()

    print("Generating page...")
    generate_pages_recursive(
        dir_path_content=dir_content,
        template_path=template_path, 
        dest_dir_path=dir_path_public
    )

def copy_static_to_public():
    if not path.exists(dir_path_static):
        raise ValueError(f"{dir_path_static} path doesnt exist")
    if path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        print("delete public for recreate it")

    shutil.copytree(dir_path_static, dir_path_public)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    object_contents = os.listdir(dir_path_content)
    for object_content in object_contents:
        if os.path.isfile(os.path.join(dir_path_content, object_content)):
            generate_page(
                from_path=os.path.join(dir_path_content, "index.md"), 
                template_path=template_path, 
                dest_path=os.path.join(dest_dir_path)
            )
        else:
            print(f"generate page recursive: {object_content}")
            generate_pages_recursive(
                dir_path_content=os.path.join(dir_path_content, object_content),
                template_path=template_path,
                dest_dir_path=os.path.join(dest_dir_path, object_content)
            )

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
    print(f"DONE: Page Generated from {from_path} to {dest_path} using {template_path}")

def update_template_placeholders(template_content, title, md_to_html):
    processed_template = template_content.replace("{{ Title }}", title)
    processed_template = processed_template.replace("{{ Content }}", md_to_html)
    return processed_template

main()

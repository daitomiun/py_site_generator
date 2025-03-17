from os import path
import shutil

def main():
    copy_static_to_public()


def copy_static_to_public():
    public, static = "./public/", "./static/"
    if not path.exists(static):
        raise ValueError(f"{static} path doesnt exist")
    if path.exists(public):
        shutil.rmtree(public)
        print("delete public for recreate it")

    shutil.copytree(static, public)

main()

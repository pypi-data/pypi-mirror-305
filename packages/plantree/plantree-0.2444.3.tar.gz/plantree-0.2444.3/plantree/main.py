from importlib import resources
from pathlib import Path
from shutil import copy, copytree
from subprocess import call
from sys import argv
from tomllib import load

from pybrary import Rex

import plantree


root = resources.files(plantree) / '../projects'


def get_projects():
    projects = {
        p.name: p.resolve()
        for p in root.glob('*')
        if p.is_dir()
    }
    return projects


def replace(txt, replacements):
    changed = txt
    for rex, value in replacements:
        if rex.find(changed):
            changed = rex.replace(value, changed)
    return changed != txt and changed


def rename(path, replacements):
    if renamed := replace(path.name, replacements):
        print('rename', path)
        path.rename(path.with_name(renamed))
        return True
    return False


def edit_file(path, replacements):
    try:
        txt = path.read_text()
    except Exception as x:
        print(f'\nread {path} ! {x}\n')
        return

    if changed := replace(txt, replacements):
        print('edit', path)
        with open(path, 'w') as out:
            out.write(changed)


def rename_dirs(root, replacements):
    go = True
    while go:
        go = False
        for path, dirs, files in root.walk():
            for d in dirs:
                go = go or rename(path / d, replacements)


def rename_files(root, replacements):
    for path, dirs, files in root.walk():
        for f in files:
            rename(path / f, replacements)


def edit_files(root, replacements):
    for path, dirs, files in root.walk():
        for f in files:
            edit_file(path / f, replacements)


def edit_config():
    path = root / 'config.toml'
    copy(path, '/tmp')
    call(['vim', '/tmp/config.toml'])


def apply_config(name):
    with open('/tmp/config.toml', 'rb') as inp:
        config = load(inp)['config']
    replacements = {
        (Rex(fr'(?<!_)_{key.upper()}_(?!_)'), value)
        for key, value in config.items()
    }
    root = Path(name).rename(config['name'])
    rename_dirs(root, replacements)
    rename_files(root, replacements)
    edit_files(root, replacements)


def plant(name):
    print(f"\nInit {name}\n")
    path = get_projects()[name]
    edit_config()
    copytree(path, name)
    apply_config(name)


def main():
    plant(argv[2] if len(argv)==3 else 'default')

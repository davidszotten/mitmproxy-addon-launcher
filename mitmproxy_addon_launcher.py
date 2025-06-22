import sys
from importlib import metadata


def run(name):
    (script_ep,) = metadata.entry_points(group="console_scripts", name=name)
    function = script_ep.load()
    sys.argv[0] = name

    addon_files = get_addons()
    for addon_file in addon_files:
        sys.argv.extend(["--script", addon_file])

    sys.exit(function())


def get_addons():
    addon_eps = metadata.entry_points(group="mitmproxy_addon_launcher.addon_script")
    addon_files = [ep.load().__file__ for ep in addon_eps]
    return addon_files


def main():
    run("mitmproxy")


def main_web():
    run("mitmweb")


def main_dump():
    run("mitmdump")

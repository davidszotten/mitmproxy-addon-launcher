# mitmproxy-addon-launcher

Load mitmproxy/mitmweb addons from entry points

## Usage:

For mitmproxy cli:

```
uvx --with=<library-with-addon> mitmproxy-addon-launcher <any args to mitmproxy>
```

or for `mitmweb`/`mitmdump`:

```
uvx \
    --from=mitmproxy-addon-launcher \
    --with=<library-with-addon> \
    mitmweb-addon-launcher <any args to mitmproxy>
```

## Creating an addon packege

Create an addon as usual. Include it into a library and add an entry-point with the group `mitmproxy_addon_launcher.addon_script`

In `pyproject.toml`:

```
[project.entry-points."mitmproxy_addon_launcher.addon_script"]
my_addon = 'my_addon_package.addon_module'
```

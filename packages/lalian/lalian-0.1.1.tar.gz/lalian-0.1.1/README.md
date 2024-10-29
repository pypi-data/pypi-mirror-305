# Lalian

Create a pseudo-executable with embedded Python code using [zipimport](https://docs.python.org/3/library/zipimport.html). Inspired by the approach used in the [yt-dlp Makefile](https://github.com/yt-dlp/yt-dlp/blob/2a246749ec5ead2c6b485e702a1c54c79bd0e51a/Makefile#L83-L102).

```
$ mkdir out; python3 -m lalian lalian out/lalian
$ ls out/
lalian  lalian.bat
$ out/lalian --help
usage: lalian [-h] package basename

positional arguments:
  package
  basename

options:
  -h, --help  show this help message and exit
```

You can also install it with `pipx`:

```
$ pipx install lalian
```

Currently, this approach works only if the target package has no external dependencies. If external dependencies are required, they must be installed in the global Python environment.

import pathlib
import tempfile
import zipfile


def find(root: pathlib.Path) -> "tuple[pathlib.Path, ...]":
    packages = set(
        init_py.parent
        for init_py in root.rglob("__init__.py")
        if not init_py.parent.name.startswith("__")
    )
    # Sort by depth, then alphabetically
    sorted_ = sorted(
        packages,
        key=lambda p: (len(p.parts), p),
    )
    return tuple(sorted_)


def create_zip(package_root: pathlib.Path) -> bytes:
    with tempfile.TemporaryFile() as tf:
        with zipfile.ZipFile(tf, "w", zipfile.ZIP_DEFLATED) as z:
            # Preserve the directory structure
            packages = find(package_root)
            for package in packages:
                for module in package.glob("*.py"):
                    z.write(module, module.relative_to(package_root.parent))

            # Copy entry point to the root
            package_main = package_root.joinpath("__main__.py")
            z.write(package_main, package_main.relative_to(package_root))
        tf.seek(0)
        return tf.read()

import pathlib
import tempfile
import zipfile


def find(root: pathlib.Path) -> "tuple[pathlib.Path, ...]":
    modules = set(
        init_py.parent
        for init_py in root.rglob("__init__.py")
        if not init_py.parent.name.startswith("__")
    )
    # Sort by depth, then alphabetically
    sorted_ = sorted(
        modules,
        key=lambda p: (len(p.parts), p),
    )
    return tuple(sorted_)


def create_zip(module_root: pathlib.Path) -> bytes:
    with tempfile.TemporaryFile() as tf:
        with zipfile.ZipFile(tf, "w", zipfile.ZIP_DEFLATED) as z:
            # Preserve the directory structure
            modules = find(module_root)
            for module in modules:
                for py in module.glob("*.py"):
                    z.write(py, py.relative_to(module_root.parent))

            # Copy entry point to the root
            module_main = module_root.joinpath("__main__.py")
            z.write(module_main, module_main.relative_to(module_root))
        tf.seek(0)
        return tf.read()

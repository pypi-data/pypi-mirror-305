import argparse
import pathlib

import lalian.constants
import lalian.module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("module", type=pathlib.Path)
    parser.add_argument("basename")
    args = parser.parse_args()

    sh = pathlib.Path(args.basename)
    bat = sh.with_suffix(".bat")

    module_zip = lalian.module.create_zip(args.module)
    for out in (
        (sh, lalian.constants.SHEBANG),
        (bat, lalian.constants.BATCH_SHEBANG),
    ):
        with open(out[0], "wb") as b:
            b.write(out[1])
            b.write(module_zip)


if __name__ == "__main__":
    main()

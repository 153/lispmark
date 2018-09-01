#!/usr/bin/env python3
# simple parse tool to generate .html from .lm file 
import sys
import parse

def main():
        if len(sys.argv) == 1:
            fn = input("file: ")
        else:
            fn = sys.argv[1]
        with open(fn + ".lm", "r") as f:
            f = f.read()
        f = "".join(["(html", f, ")"])
        lm = parse.eval_input(f)
        if len(sys.argv) == 1:
            print(lm)
            wri = input("Write file?")
            if wri not in ["0", "n"]:
                with open(fn + ".html", "w") as nf:
                    nf.write(lm)
        else:
            with open(fn + ".html", "w") as nf:
                nf.write(lm)

main()

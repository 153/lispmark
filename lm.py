#!/usr/bin/env python3
# simple parse tool to generate .html from .lm file 

import parse

def main():
        fn = input("file: ")
        with open(fn + ".lm", "r") as f:
	        f = f.read()
        f = "".join(["(html", f, ")"])
        lm = parse.eval_input(f)
        print(lm)
        wri = input("Write file?")
        if wri not in ["0", "n"]:
	        with open(fn + ".html", "w") as nf:
		        nf.write(lm)

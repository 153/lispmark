Lispmark is a new markup language in the spirit of
Sexpcode, CURL, Bach, and Arc. It aims to replace
XML-based markup with SEXP-based syntax, and currently
compiles to HTML.

Usage from python3: `import parse`  
`parse.eval_input("(p my input)")`

-----
![](https://i.imgur.com/eZ5qvMK.png) 

-----
Very alpha

* tags are ( parenthetically wrapped)
* parse.py handles parsing 
* parse.eval_input() takes a string like "(p my input)" wrap all text in parens ( )

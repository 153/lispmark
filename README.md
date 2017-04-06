Lispmark is a new markup language in the spirit of
Sexpcode, CURL, Bach, and Arc. It aims to replace
XML-based markup with SEXP-based, and currently
compiles to HTML.

Very alpha

* tags are ( parenthetically wrapped)
* parse.py handles parsing 
* parse.eval_input() takes a string like "(p my input)" (wrap all text in single bracket)
* index.py3 is a simple web interface for viewing lispmark code

View demo.lm and demo.html to see an example
#!/usr/bin/env python3
import webtools as wt
import parse

def get_inp():
    print(wt.new_form())
    print("<textarea name='my' cols=70 rows=8>" + wt.get_form('my'),
          "</textarea>")
    print("<p>", wt.put_form('submit', '', 'Submit'))

def main():
    print(wt.head())
    parse.css_spoiler()
    print("""<pre>
    tags available: b, i, u, o, s, code, tt,
    sp, sup, sub, q, h1, h2, h3, ul, ol, li,
    table, tr, th, td, br, hr, p, img, url, 
    link, anc

    Try (link http://google.com/ google), 
        (img src caption), or (sp spoiler text)
</pre>""")
    get_inp()
    my = wt.get_form("my").replace("\(", "&#40;").replace("\)", "&#41;")
    if not my:
        with open('demo.lm', 'r') as my:
            my = my.read().replace("\(", "&#40;").replace("\)", "&#41;")
    print("<hr><pre>" + my, "</pre><hr>")
    print(parse.eval_input(my))

main()

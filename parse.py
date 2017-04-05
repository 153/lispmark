#/usr/bin/env python3

entity = ["quot", "amp", "lt", "gt", "le", "ge", "hellip",
          "nbsp", "ensp", "emsp", "ndash", "mdash",
          "hearts", "diams", "clubs", "spades", "loz",
          "cent", "pound", "yen", "euro", 
          "copy", "reg", "trade",  "para", "sect", "dagger",
          "frac14", "frac12", "frac34",
          "micro", "lambda", "divide", "times", "fnof",
          "forall", "empty", "isin", "notin", "sum",
          "radic", "infin", "there4", "oplus", "otimes",
          "cong", "asymp", "equiv",
          "aelig", "THORN", "szlig", ]
single = ["br", "hr", "p"]
wrap = ["b", "i", "u", "o", "s", "code",
        "tt", "spoiler", "sup", "sub",
        "blockquote", "h1", "h2", "h3",
        "ul", "ol", "li", "table", "tr",
        "td", "th"]
arg1 = {"url":"<a href='{0}'>{0}</a>",
        "anc":"<a name='{0}'></a>"
}
arg2 = {"link":"<a href='{0}'>{1}</a>",
        "img":"<img src='{0}' title='{1}'></img>"
}
for tag in wrap:
    arg1[tag] = str("<" + tag + ">{" + "0}</" + tag + ">")
for tag in single:
    arg1[tag] = str("<" + tag + ">{" + "0}")

arg1["sp"] = "<span class='spoiler'>{0}</span>"
arg1["q"] = "<blockquote>{0}</blockquote>"
    
def tokenize(inp=""): # Thanks Peter Norvig, lis.py
    return inp.replace('(', ' ( ').replace(')', ' ) ').split()

def make_list(tokens):
    token = tokens.pop(0)
    if '(' == token:
        tmp = []
        while tokens[0] != ')':
            tmp.append(make_list(tokens))
        tokens.pop(0)
        return tmp
    elif ')' == token:
        return "?"
    else:
        return token

def split_functions(inp=""): # Thanks Peter Norvig, lis.py
    return make_list(tokenize(inp))

def markup_strings(inp=""):
    if type(inp) is str:
        inp = inp[0].split(" ")
    if len(inp) < 2 and inp[0] in single:
        return f"<{inp[0]}>"
    if inp[0] == "sym":
        return do_sym(inp[1])
    if inp[0] in arg1.keys():
        inp[1] = " ".join(inp[1:])
    elif len(inp) > 3:
        inp[2] = " ".join(inp[2:])
    elif len(inp) < 3:
        inp.append(inp[1])

    if inp[0] in arg1:
        return arg1[inp[0]].format(inp[1])
    elif inp[0] in arg2:
        return arg2[inp[0]].format(inp[1], inp[2])
    return f"<{inp[0]}>{inp[1]}</{inp[0]}>"

def parse_list(inp=[]):
    parsed =[]
    for n, i in enumerate(inp):
        if type(i) is list:
            parsed.append(parse_list(i))
        else:
            parsed.append(i)
    return markup_strings(parsed)


def eval_input(inp=""):
    return parse_list(split_functions(inp))

def do_sym(inp):
    if inp in entity:
        return f"&{inp};"
    return f"&amp;{inp};"

my_page = """
(p 
 (b Welcome to my page)
 (hr (link . Here) / (link .. Up) / (link / Top) (hr))
 (p This is the page.)
 (p It's a document composed in (i Lispmark,)
    with (b HTML-like) tag names.)

 (p It currently supports:)
 (ul
  (li Basic formatting 
    (ul 
      (li (sym hellip) like (b bold,) (i italics,) (u underline))
      (li (sym hellip) (sup superscript,) (sub subscript))
      (li (sym hellip) (code code,) (s strikethrough))
    ))
  (li List Processing)
  (li Higher-arrity functions
    (ul
     (li Such as (link http://google.com/ links))
     (li and (img rss.png) images)))
  (li Special HTML symbols, such as (sym forall), (sym sum),
      (sym frac14), (sym infin))
 )
 (p Work in development.)
 (q  bob (sup (sym lambda)))
)
"""

def css_spoiler():
    print("""<style>
.spoiler {
color: #000; background-color: #000;
}
.spoiler:hover {
color:#fff}</style>""")

def show_entity():
    print("<hr><table border='2' style='border-collapse:collapse'><tr>")
    for n, e in enumerate(entity):
        if not (n % 6):
            print("<tr>")
        print(f"<td>{e}<td>{do_sym(e)}")

if __name__ == "__main__":
    print(f"<pre>{my_page}</pre><hr>{eval_input(my_page)}")

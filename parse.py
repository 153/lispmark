#/usr/bin/env python3
# usage: import parse; parse.eval_input("(my input)")
# be sane and wrap your parse.eval_input with ( )
# 2018.03.22

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
          "aelig", "THORN", "szlig",
          "uarr", "larr", "rarr", "darr"]
single = ["br", "hr", "p"]
wrap = ["b", "i", "u", "o", "s", "code",
        "tt", "sup", "sub", "div", "span",
        "blockquote", "h1", "h2", "h3", "h4",
        "ul", "ol", "li",
        "html", "body", "head", "title",
        "table", "tr", "td", "th"]
arg1 = {"url":"<a href='{0}'>{0}</a>",
        "anc":"<a name='{0}'></a>",
        "m":"<pre><code>{0}</code></pre>",
        "q": "<blockquote>{0}</blockquote>",
        "style": "<link rel='stylesheet' type='text/css' href='{0}'>",
        "sp": "<span class='spoiler'>{0}</span>",
        "/": "&lpar;{0}&rpar;",
        "'": "{0}",
        "!": "<!-- {0} -->"}
arg2 = {"link":"<a href='{0}'>{1}</a>",
        "img":"<img src='{0}' title='{1}'></img>"}
arg3 = {}

for tag in single:
    arg1[tag] = str("<" + tag + ">{" + "0}")
for tag in wrap:
    arg1[tag] = str("<" + tag + ">{" + "0}</" + tag + ">")


args = [i for i in arg1.keys()]
x = [args.append(i) for i in arg2.keys()]

# We call eval_input(input) which calls a
# parse_list() on split_functions(input).
#
# split_functions(input) returns
#     a make_list() of tokenize(input).
# tokenize(input) replaces ( and ) with " ( " and " ) "
#     after adding the contents of parens to list.
# make_list(tokens) adds to contents of (parens) to a list.
# parse_list() ensures that each item in the make_list is ran
#     through markup_strings(parsed) from the inside-out.
#
# markup_strings(input) sends a list through the (sym) symbol
#     dictionary, runs input through the (def) define macro,
#     tries to run items through (,) the map function,
#      runs inp[0] through arg1 if it's in arg1,
#      returning arg1[inp[0]].format(inp[1])
#      or runs inp[0] through arg2 if it's in arg2,
#      returning arg2[inp[0]] formatting inp[1] and inp[2],
#     otherwise returning (text in parens). 
# css_spoiler()  makes sure that spoilers work 

def css_spoiler():
    print("""<style>\n
.spoiler {color: #000; background-color: #000;
}\n.spoiler:hover {
color:#fff;\n}</style>""")

def tokenize(inp=""): # Thanks Peter Norvig, lis.py
    return inp.replace('(', ' ( ').replace(')', ' ) ').split()

def make_list(tokens): # Thanks Peter Norvig, lis.py
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
    if inp[0] == ",":
        newlist = [] # real hacky shit, currently only accepts 1 field 
        for i in inp[2:]:
            newlist.append(inp[1].format(i))
        return " ".join(newlist)
    if inp[0] == "sym":
        return do_sym(inp[1])
    elif inp[0] == "def":
        return do_def(inp[1:])
    if len(inp) < 2:
        inp.append(inp[0])
    if inp[0] in arg1.keys():
        inp[1] = " ".join(inp[1:])
        return arg1[inp[0]].format(inp[1])
    elif inp[0] in arg2.keys():
        if len(inp) > 3:
            inp[2] = " ".join(inp[2:])
        elif len(inp) < 3:
            inp.append(inp[1])
        return arg2[inp[0]].format(inp[1], inp[2])
    return "&lpar;" + " ".join(inp) + "&rpar;"

def parse_list(inp=[]):
    parsed =[]
    for n, i in enumerate(inp):
        if type(i) is list:
            parsed.append(parse_list(i))
        else:
            parsed.append(i)
    return markup_strings(parsed)

def eval_input(inp=""):
    return parse_list(split_functions(inp))\
        .replace("\\\\", "&#92;").replace('\ ', '')

def do_sym(inp):
    if inp in entity:
        return f"&{inp};"
    return f"&amp;{inp};"

def do_def(inp=[]):
    inp = [i.replace('&gt;', ">").replace('&lt;', "<") \
           for i in inp]
    if len(inp) < 2:
        return None
    elif len(inp) > 2:
        inp[1] = " ".join(inp[1:])
    if inp[0] in args:
        return " "
    if "{2}" in inp[1]:
        arg3[inp[0]] = inp[1]
    elif "{1}" in inp[1]:
        arg2[inp[0]] = inp[1]
    elif "{0}" in inp[1]:
        arg1[inp[0]] = inp[1]
    else:
        single.append(inp[0])
    return ' '

def show_entity():
    print("<table><tr>")
    for n, e in enumerate(entity):
        if not (n % 8):
            print("<tr>")
        print(f"<td>{e}<td>{do_sym(e)}")
    print("</table>")

from IPython.core.display import display, HTML, Javascript
import pandas.core.series as s
from datetime import date

d3 = """<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.9/d3.js"></script>"""
d3sg = """<script src="https://rawgit.com/jstoxrocky/d3sg/master/d3sg.js"></script>"""
d3sg_style = """<link href="https://rawgit.com/jstoxrocky/d3sg/master/d3sg_style.css" type="text/css" rel="stylesheet">"""
display(HTML(d3+d3sg+d3sg_style))

class chart():
    
    def __init__(self):
        self.lines = []

    def render_js(self):
        js = """var ch = new chart('ipython');"""
        js = js + "".join(self.lines)
        js += """element.append(ch.svg.node());"""
        return js
            
    def line(self, x, y, label=''):

        if isinstance(x, s.Series):
            if isinstance(x.values[0], date):
                x = x.map(str)
            x = x.tolist()
        if isinstance(y, s.Series):
            y = y.tolist()

        curr_line = """ch.line({x}, {y}, '{label}');""".format(x=x, y=y, label=label)
        self.lines.append(curr_line)
        return Javascript(self.render_js())
    
    
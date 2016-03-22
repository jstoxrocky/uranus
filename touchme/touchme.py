from IPython.display import HTML, Javascript

def load():
    d3 = """<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.9/d3.js"></script>"""
    d3sg = """<script src="https://rawgit.com/jstoxrocky/d3sg/master/d3sg.js"></script>"""
    d3sg_style = """<link href="https://rawgit.com/jstoxrocky/d3sg/master/d3sg_style.css" type="text/css" rel="stylesheet">"""
    return HTML(d3+d3sg+d3sg_style)

class chart():
    
    def __init__(self):
        self.lines = []

    def render_js(self):
        js = """var ch = new chart('ipython');"""
        js = js + "".join(self.lines)
        js += """element.append(ch.svg.node());"""
        return js
            
    def line(self, x, y, label=''):
        curr_line = """ch.line({x}, {y}, '{label}');""".format(x=x, y=y, label=label)
        self.lines.append(curr_line)
        return Javascript(self.render_js())
    
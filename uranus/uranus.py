from IPython.core.display import display, HTML, Javascript
import pandas.core.series as s
from datetime import date
import json

d3 = """<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.9/d3.js"></script>"""
d3sg = """<script src="https://rawgit.com/jstoxrocky/d3sg/master/d3sg.js"></script>"""
display(HTML(d3+d3sg))

class chart():
    
    def __init__(self, gif=None):
        self.lines = []
        self.gif = gif
        d3sg_style = """<link href="https://rawgit.com/jstoxrocky/d3sg/master/d3sg_style.css" type="text/css" rel="stylesheet">"""
        display(HTML(d3sg_style)) # Not sure why but we lose the css if its above with the js stuff
        
    def render_js(self):
        if self.gif:
            js = """var ch = new chart('ipython', '{gif}');""".format(gif=self.gif)
        else:
            js = """var ch = new chart('ipython');"""
        js = js + "".join(self.lines)
        js += """element.append(ch.svg.node());"""
        return js
            
    def line(self, x, y, label='', alpha=1.0, add_legend=True, color_from=None):
        """
        Add a line to the chart object.
        Input:
            x: pandas.Series or list, containing datetime.date objects or strings of the form: 'YYYY-mm_dd'.
            y: pandas.Series or list, containing numerical values.
            label: string, to be used in the legend and tooltip.
            alpha: float, opacity: [0.0, 1.0].
            add_legend: boolean, either adds or removes this line from the legend.
            color_from: string, using the label from another line you can copy its color onto this line.
        """
        # pandas.Series to list
        if isinstance(x, s.Series):
            x = x.tolist()
        # datetime.date to str
        if isinstance(x[0], date):
            x = [str(dt) for dt in x]
        # pandas.Series to list
        if isinstance(y, s.Series):
            y = y.tolist()

        kwargs = {'alpha':alpha, 'add_legend':add_legend,}
        if color_from:
            kwargs['color_from'] = color_from

        curr_line = """ch.line({x}, {y}, '{label}', {kwargs});""".format(x=x, y=y, label=label, kwargs=json.dumps(kwargs))
        self.lines.append(curr_line)
        return Javascript(self.render_js())
    
    
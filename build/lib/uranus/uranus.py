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
        self.title = None
        self.subtitle = None
        self.ylabel = None
        self.xlabel = None
        self.ymin = None
        self.gif = gif
        d3sg_style = """<link href="https://rawgit.com/jstoxrocky/d3sg/master/d3sg_style.css" type="text/css" rel="stylesheet">"""
        display(HTML(d3sg_style)) # Not sure why but we lose the css if its above with the js stuff
        
    def render_js(self):
        if self.gif:
            js = """var ch = new chart('ipython', '{gif}');""".format(gif=self.gif)
        elif self.title or self.subtitle or self.ylabel or self.xlabel:
            js = """var ch = new chart('ipython_report');"""
        else:
            js = """var ch = new chart('ipython');"""

        if self.title:
            js += """ch.set_title('{title}');""".format(title=self.title)
        if self.subtitle:
            js += """ch.set_subtitle('{subtitle}');""".format(subtitle=self.subtitle)
        if self.ylabel:
            js += """ch.set_ylabel('{ylabel}');""".format(ylabel=self.ylabel)
        if self.xlabel:
            js += """ch.set_xlabel('{xlabel}');""".format(xlabel=self.xlabel)

        js += "".join(self.lines)

        if self.ymin is not None:
            js += """ch.set_ymin({ymin});""".format(ymin=self.ymin)

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
    
    def scatter(self, x, y, label='', url='', size=20):
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

        kwargs = {'url':url, 'size':size}
        curr_line = """ch.scatter({x}, {y}, '{label}', {kwargs});""".format(x=x, y=y, label=label, kwargs=json.dumps(kwargs))
        self.lines.append(curr_line)
        return Javascript(self.render_js())

    def set_title(self, title):
        self.title = title
        return Javascript(self.render_js())

    def set_subtitle(self, subtitle):
        self.subtitle = subtitle
        return Javascript(self.render_js())

    def set_ylabel(self, ylabel):
        self.ylabel = ylabel
        return Javascript(self.render_js())

    def set_xlabel(self, xlabel):
        self.xlabel = xlabel
        return Javascript(self.render_js())

    def set_ymin(self, ymin):
        self.ymin = ymin
        return Javascript(self.render_js())



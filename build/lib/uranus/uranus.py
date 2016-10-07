import jinja2
from IPython.display import HTML, Javascript, display
import pandas.core.series as s
from datetime import date
import json
from itertools import count

D3_URL = "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.9/d3.min.js"
D3SG_URL = "https://rawgit.com/jstoxrocky/d3sg/master/d3sg.js"


REQUIREJS_JS = jinja2.Template("""


  require.config({paths: {d3: "{{ d3_url[:-3] }}"}});
  require(["d3"], function(d3){
    window.d3 = d3;
    $.getScript("{{ d3sg_url }}", function(){
        
        var cssId = 'myCss';  // you could encode the css path itself to generate id..
        if (!document.getElementById(cssId))
        {
            var head  = document.getElementsByTagName('head')[0];
            var link  = document.createElement('link');
            link.id   = cssId;
            link.rel  = 'stylesheet';
            link.type = 'text/css';
            link.href = 'https://rawgit.com/jstoxrocky/d3sg/master/d3sg_style.css';
            link.media = 'all';
            head.appendChild(link);
        }
        document.getElementById("{{id}}").innerHTML = "";
        var ch = new chart('{{chart_style}}');
        {{lines}}
        {{title}}
        {{subtitle}}
        {{ylabel}}
        {{xlabel}}
        {{ymin}}
        {{ymax}}
        
        document.getElementById("{{id}}").appendChild(ch.svg.node())
        
    });
  });

""")


class chart():
    _ids = count(0)
    
    def __init__(self, gif=None):
        self.id = self._ids.next()
        self.lines = []
        self.title = ""
        self.subtitle = ""
        self.ylabel = ""
        self.xlabel = ""
        self.ymin = ""
        self.ymax = ""
        self.gif = gif
        display(HTML("<div id='{id}'></div>".format(id=hash(self.id))))

    def render_js(self):
        
        title = self.title
        subtitle = self.subtitle
        ylabel = self.ylabel
        xlabel = self.xlabel
        ymin = self.ymin
        ymax = self.ymax
        
        if self.gif:
            chart_style = self.gif
        elif self.title or self.subtitle or self.ylabel or self.xlabel:
            chart_style = "ipython_report"
        else:
            chart_style = "ipython"

        if self.title:
            title = """ch.set_title('{title}');""".format(title=self.title)
        if self.subtitle:
            subtitle = """ch.set_subtitle('{subtitle}');""".format(subtitle=self.subtitle)
        if self.ylabel:
            ylabel = """ch.set_ylabel('{ylabel}');""".format(ylabel=self.ylabel)
        if self.xlabel:
            xlabel = """ch.set_xlabel('{xlabel}');""".format(xlabel=self.xlabel)

        lines = "".join(self.lines)

        if self.ymin or self.ymin == 0:
            ymin = """ch.set_ymin({ymin});""".format(ymin=self.ymin)
        if self.ymax or self.ymin == 0:
            ymax = """ch.set_ymax({ymax});""".format(ymax=self.ymax)
        
        js = REQUIREJS_JS.render(d3_url=D3_URL, 
                        d3sg_url=D3SG_URL,
                        lines = lines,
                        title = title,
                        subtitle = subtitle,
                        ylabel = ylabel,
                        xlabel = xlabel,
                        ymin = ymin,
                        ymax = ymax,
                        chart_style = chart_style,
                        id = self.id)
        
        return Javascript(js)
    
            
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
        return self.render_js()


    def bar(self, x, y, label='', alpha=1.0, add_legend=True, color_from=None):
        """
        Add a bar to the chart object.
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

        curr_line = """ch.bar({x}, {y}, '{label}', {kwargs});""".format(x=x, y=y, label=label, kwargs=json.dumps(kwargs))
        self.lines.append(curr_line)
        return self.render_js()
    

    def scatter(self, x, y, label='', url='', size=20):
        """
        Add a scatter to the chart object.
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
        return self.render_js()

    def set_title(self, title):
        self.title = title
        return self.render_js()

    def set_subtitle(self, subtitle):
        self.subtitle = subtitle
        return self.render_js()

    def set_ylabel(self, ylabel):
        self.ylabel = ylabel
        return self.render_js()

    def set_xlabel(self, xlabel):
        self.xlabel = xlabel
        return self.render_js()

    def set_ymin(self, ymin):
        self.ymin = ymin
        return self.render_js()

    def set_ymax(self, ymax):
        self.ymax = ymax
        return self.render_js()

    def set_ylim(self, ymin, ymax):
        self.ymin = ymin
        self.ymax = ymax
        return self.render_js()



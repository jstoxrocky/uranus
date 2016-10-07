# Uranus

![alt tag](https://68.media.tumblr.com/96ed9c344078766b91a1972ef90aa9e3/tumblr_nrpl86ESnc1tchrkco1_500.gif)

<h4>Uranus: Interactive Charting for Jupyter Notebooks</h4>

Uranus is an interactive charting library built in d3.js designed to be used easily and intuitively within the Jupyter (IPython) framework. Gif images can now be used as backgrounds for charts as well. 

<h3>Simple Example</h3>
```python
from uranus import uranus
    
dt = ['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04', '2016-01-05', '2016-01-06', '2016-01-07', '2016-01-08', '2016-01-09', '2016-01-10', '2016-01-11', '2016-01-12', '2016-01-13', '2016-01-14', '2016-01-15', '2016-01-16', '2016-01-17', '2016-01-18', '2016-01-19', '2016-01-20', '2016-01-21', '2016-01-22', '2016-01-23', '2016-01-24', '2016-01-25', '2016-01-26', '2016-01-27', '2016-01-28', '2016-01-29', '2016-01-30', '2016-01-31', '2016-02-01', '2016-02-02', '2016-02-03', '2016-02-04', '2016-02-05', '2016-02-06', '2016-02-07', '2016-02-08', '2016-02-09', '2016-02-10', '2016-02-11', '2016-02-12', '2016-02-13', '2016-02-14', '2016-02-15', '2016-02-16', '2016-02-17', '2016-02-18', '2016-02-19', '2016-02-20', '2016-02-21', '2016-02-22', '2016-02-23', '2016-02-24', '2016-02-25', '2016-02-26', '2016-02-27', '2016-02-28', '2016-02-29', '2016-03-01', '2016-03-02', '2016-03-03', '2016-03-04', '2016-03-05', '2016-03-06', '2016-03-07', '2016-03-08', '2016-03-09', '2016-03-10', '2016-03-11', '2016-03-12', '2016-03-13', '2016-03-14', '2016-03-15', '2016-03-16', '2016-03-17', '2016-03-18', '2016-03-19', '2016-03-20', '2016-03-21', '2016-03-22', '2016-03-23', '2016-03-24', '2016-03-25', '2016-03-26', '2016-03-27', '2016-03-28', '2016-03-29', '2016-03-30', '2016-03-31', '2016-04-01']
neptune = [33, 116, 67, 109, 64, 152, 193, 171, 155, 79, 112, 14, -20, 44, 79, 59, 150, 68, 65, 30, 68, 31, 47, 103, 144, 204, 140, 95, 27, 113, 87, 56, 133, 85, 129, 172, 228, 162, 72, 95, 149, 228, 275, 329, 360, 287, 309, 266, 252, 259, 222, 204, 290, 268, 239, 204, 205, 263, 221, 144, 231, 170, 245, 294, 209, 146, 172, 107, 50, -47, -115, -124, -207, -162, -139, -97, -173, -246, -264, -249, -311, -361, -358, -258, -266, -196, -166, -218, -243, -322, -359, -285]
neptune_rolling_mean = [33.0, 74.5, 72.0, 81.25, 77.799999999999997, 90.166666666666671, 104.85714285714286, 124.57142857142857, 130.14285714285714, 131.85714285714286, 132.28571428571428, 125.14285714285714, 100.57142857142857, 79.285714285714292, 66.142857142857139, 52.428571428571431, 62.571428571428569, 56.285714285714285, 63.571428571428569, 70.714285714285708, 74.142857142857139, 67.285714285714292, 65.571428571428569, 58.857142857142854, 69.714285714285708, 89.571428571428569, 105.28571428571429, 109.14285714285714, 108.57142857142857, 118.0, 115.71428571428571, 103.14285714285714, 93.0, 85.142857142857139, 90.0, 110.71428571428571, 127.14285714285714, 137.85714285714286, 140.14285714285714, 134.71428571428572, 143.85714285714286, 158.0, 172.71428571428572, 187.14285714285714, 215.42857142857142, 246.14285714285714, 276.71428571428572, 293.42857142857144, 296.85714285714283, 294.57142857142856, 279.28571428571428, 257.0, 257.42857142857144, 251.57142857142858, 247.71428571428572, 240.85714285714286, 233.14285714285714, 239.0, 241.42857142857142, 220.57142857142858, 215.28571428571428, 205.42857142857142, 211.28571428571428, 224.0, 216.28571428571428, 205.57142857142858, 209.57142857142858, 191.85714285714286, 174.71428571428572, 133.0, 74.571428571428569, 27.0, -23.428571428571427, -71.142857142857139, -106.28571428571429, -127.28571428571429, -145.28571428571428, -164.0, -184.0, -190.0, -211.28571428571428, -243.0, -280.28571428571428, -292.42857142857144, -295.28571428571428, -285.57142857142856, -273.71428571428572, -260.42857142857144, -243.57142857142858, -238.42857142857142, -252.85714285714286, -255.57142857142858]
    
ch = uranus.chart()
ch.line(dt, neptune, 'Neptune')
ch.line(dt, neptune_rolling_mean, '7 Day Rolling Mean', alpha=0.3, color_from='Neptune', add_legend=False)
```

![alt tag](https://rawgit.com/jstoxrocky/uranus/master/uranus/uranus.gif)

<h3>Support for GIF backgrounds!</h3>

![alt tag](https://rawgit.com/jstoxrocky/uranus/master/uranus/uranus_gif.gif)

![alt tag](https://68.media.tumblr.com/f88c22b3b8a29f048e78c2bd280dd9b9/tumblr_o4b2lpUOoU1qd5mq1o1_500.jpg)

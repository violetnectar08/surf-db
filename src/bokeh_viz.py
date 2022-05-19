# This file is for bokeh visualizations
#
#
########################################################################################################################
# Imports
from bokeh.plotting import figure, show

########################################################################################################################
# Define two lists containing the data for a line chart

x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

# Use the figure() function to create the plot
# title: the title of the line chart (optional)
# x_axis_label: text label to put on the chart's x-axis (optional)
# y_axis_label

p = figure(title='Multiple Line Example',
           x_axis_label='x',
           y_axis_label='y')

# Add a line graph to the plot using the line(0 function
p.line(x, y1, legend_label="Temp.", color="blue", line_width=2)
p.line(x, y2, legend_label='Rate', color='red', line_width=2)
p.line(x, y3, legend_label='Objects', color='green', line_width=2)

# Use show() function to generate graph and open web browser to display
show(p)

#!/usr/bin/env python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the PyMVPA package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""
Self-organizing Maps
====================
.. index:: mapper, self-organizing map, SOM, SimpleSOMMapper
This is a demonstration of how a self-organizing map (SOM), also known
as a Kohonen network, can be used to map high-dimensional data into a
two-dimensional representation. For the sake of an easy visualization
'high-dimensional' in this case is 3D.
In general, SOMs might be useful for visualizing high-dimensional data
in terms of its similarity structure. Especially large SOMs (i.e. with
large number of Kohonen units) are known to perform mappings that
preserve the topology of the original data, i.e. neighboring data
points in input space will also be represented in adjacent locations
on the SOM.
`The following code shows the 'classic' color mapping example, i.e. the
SOM will map a number of colors into a rectangular area.
"""

from mvpa2.suite import *

"""
First, we define some colors as RGB values from the interval (0,1),
i.e. with white being (1, 1, 1) and black being (0, 0, 0). Please
note, that a substantial proportion of the defined colors represent
variations of 'blue', which are supposed to be represented in more
detail in the SOM.
"""

import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('output.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

# %DV of nutrients for food items
nutrients = np.array(
            [columns['apple'], columns['banana'], columns['beef'],
              columns['butter'], columns['cheese'], columns['chex-mix'],
              columns['commodity-beef'], columns['egg'], columns['gogurt'],
              columns['greek-yogurt'], columns['margarine'], columns['pepsi']])


# store the names of the food items for visualization later on
food_names = \
        ['apple', 'banana', 'beef', 'butter', 'cheese',
         'chex-mix', 'commodity-beef', 'egg', 'gogurt',
         'greek-yogurt', 'margarine', 'pepsi']
            

"""
Now we can instantiate the mapper. It will internally use a so-called
Kohonen layer to map the data onto. We tell the mapper to use a
rectangular layer with 20 x 30 units. This will be the output space of
the mapper. Additionally, we tell it to train the network using 400
iterations and to use custom learning rate.
"""

som = SimpleSOMMapper((30, 40), 400, learning_rate=0.05)

"""
Finally, we train the mapper with the previously defined 'color' dataset.
"""

som.train(nutrients)

"""
Each unit in the Kohonen layer can be treated as a pointer into the
high-dimensional input space, that can be queried to inspect which
input subspaces the SOM maps onto certain sections of its 2D output
space.  The color-mapping generated by this example's SOM can be shown
with a single matplotlib call:
"""

pl.imshow(som.K, origin='lower')

"""
And now, let's take a look onto which coordinates the initial training
prototypes were mapped to. The get those coordinates we can simply feed
the training data to the mapper and plot the output.
"""

mapped = som(nutrients)

pl.title('Food SOM')
# SOM's kshape is (rows x columns), while matplotlib wants (X x Y)
for i, m in enumerate(mapped):
    pl.text(m[1], m[0], food_names[i], ha='center', va='center',
           bbox=dict(facecolor='white', alpha=0.5, lw=0))

"""
The text labels of the original training colors will appear at the 'mapped'
locations in the SOM -- and should match with the underlying color.
"""

# show the figure
if cfg.getboolean('examples', 'interactive', True):
    pl.show()

"""
The following figure shows an exemplary solution of the SOM mapping of the
3D color-space onto the 2D SOM node layer:
.. image:: ../pics/ex_som.*
   :align: center
   :alt: Color-space mapping by a self-organizing map.
"""

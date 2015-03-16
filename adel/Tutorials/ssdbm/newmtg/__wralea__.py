
# This file has been generated at Sat Mar 14 00:19:37 2015

from openalea.core import *


__name__ = 'alinea.adel.tutorials.ssdbm.mtg'

__editable__ = True
__description__ = ''
__license__ = ''
__url__ = ''
__alias__ = ['ssbm.mtg', 'ssdbm']
__version__ = ''
__authors__ = 'C. Pradal, C. Fournier, S. Cohen-Boulakia'
__institutes__ = 'INRIA'
__icon__ = ''


__all__ = ['algo_union']



algo_union = Factory(name='union',
                authors='C. Pradal, C. Fournier, S. Cohen-Boulakia (wralea authors)',
                description='',
                category='Unclassified',
                nodemodule='openalea.mtg.algo',
                nodeclass='union',
                inputs=[{'name': 'g1', 'desc': 'MTG'}, {'name': 'g2', 'desc': 'MTG'}],
                outputs=[{'name': 'g', 'desc': 'MTG'}],
                widgetmodule=None,
                widgetclass=None,
               )


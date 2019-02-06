import sys
import os
import sqlite3
from cravat import BaseAnnotator
from cravat import InvalidData
from cravat.util import get_ucsc_bins

class CravatAnnotator (BaseAnnotator):

    def annotate(self, input_data):
        out = {}
        
        chrom = input_data['chrom']
        pos = input_data['pos']
        
        out = {'feature': []}
        
        bins = get_ucsc_bins(pos)
        pos = str(pos)
        for bin in bins:
            query = 'select class, name from enhancer ' +\
                'where binno=' + str(bin) + ' and ' +\
                'chrom="' + chrom + '" and ' +\
                'start<=' + pos + ' and end>=' + pos
            self.cursor.execute(query) 
            results = self.cursor.fetchall()
            
            if len(results) == 0:
                continue
            
            for result in results:
                (feature) = result
                out['feature'].append(feature)
        
        out['feature'] = ','.join(out['feature'])
        
        return out
        
if __name__ == '__main__':
    module = CravatAnnotator(sys.argv)
    module.run()

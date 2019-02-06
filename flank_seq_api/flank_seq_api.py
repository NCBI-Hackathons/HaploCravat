import sys
from cravat import BaseAnnotator
from cravat import InvalidData
import sqlite3
import os
import requests

class CravatAnnotator(BaseAnnotator):

    def setup(self): 
        self.server_url = 'https://rest.ensembl.org'
    
    def annotate(self, input_data, secondary_data=None):
        out = {}
        chrom = input_data['chrom']
        start = input_data['pos']
        ref_bases = input_data['ref_base'].replace('-','')
        alt_bases = input_data['alt_base'].replace('-','')
        end=start+len(ref_bases)+1
        nflank = self.conf['options']['flanking_bases']
        full_url = '{base}/sequence/region/human/{chrom}:{start}..{end}:1?expand_5prime={nflank}&expand_3prime={nflank}&content-type=text/plain'.format(
            base = self.server_url,
            chrom = chrom,
            start = start,
            end = end,
            nflank = nflank,
        )
        r = requests.get(full_url)
        if r.ok:
            ref_seq = r.text
            alt_seq = ref_seq[:nflank] + alt_bases + ref_seq[nflank+len(ref_bases):]
            out['ref_seq'] = ref_seq
            out['alt_seq'] = alt_seq
        return out
 
    
    def cleanup(self):
        pass
        
if __name__ == '__main__':
    annotator = CravatAnnotator(sys.argv)
    annotator.run()

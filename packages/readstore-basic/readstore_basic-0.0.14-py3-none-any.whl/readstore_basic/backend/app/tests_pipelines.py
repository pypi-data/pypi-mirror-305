# readstore-basic/backend/app/tests_pipelines.py

import unittest
from typing import Tuple
import datetime
        
class PipelinesTestCase(unittest.TestCase):
    def test_qc_fastq(self):
        
        test_path = '/home/nonroot/backend/test_data/Chromium_3p_GEX_Human_PBMC_S1_L001_R2_001.fastq'
        
        import pipelines
        
        tic = datetime.datetime.now()
        res = pipelines.qc_fastq(test_path)
        toc = datetime.datetime.now()
        
        print(f"Time taken: {toc - tic}")
        
        print(res)
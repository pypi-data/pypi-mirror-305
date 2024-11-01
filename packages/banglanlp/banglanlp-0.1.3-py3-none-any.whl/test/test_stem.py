import unittest
from banglanlp.rootfinder import load_dataset
import pkg_resources
import pandas as pd

class TestStemmer(unittest.TestCase):
    
    def test_load_dataset1(self):
        # dataset1.csv লোড করতে পারছে কিনা পরীক্ষা করে
        data = load_dataset("dictহ.json")
        self.assertIsNotNone(data)  # ডেটা ফাইলটি খালি নয় কিনা পরীক্ষা
        self.assertGreater(len(data), 0)  # ডেটাতে কিছু ডেটা আছে কিনা পরীক্ষা
        

    def test_load_dataset2(self):
        # dataset2.csv লোড করতে পারছে কিনা পরীক্ষা করে
        data = load_dataset("dictঅ.json")
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)
        
if __name__ == "__main__":
    unittest.main()

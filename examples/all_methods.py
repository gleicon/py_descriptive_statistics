import sys
sys.path.append("..")

from py_descriptive_statistics import Enum

enum = Enum([2,6,9,3,5,1,8,3,6,9,2])
    
print enum.number()
print enum.sum()
print enum.mean()
print enum.median()
print enum.variance()
print enum.standard_deviation()
print enum.percentile(70)
print enum.percentile(95)
print enum.percentile(99)


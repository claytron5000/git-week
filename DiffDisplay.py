from fabulous.color import red, yellow, green
import math
from itertools import repeat

class DiffDisplay:
    def __init__(self, diff_string):
        diff = diff_string.split(",")
        self.extractDiffTypes(diff)

    def extractDiffTypes(self, diff_array):
        for diff in diff_array:
            # print(diff)
            if "changed" in diff:
                self.changed = int(''.join(filter(str.isdigit, diff)))
            if "insertion" in diff:
                self.insertion = int(''.join(filter(str.isdigit, diff)))
            if "deletion" in diff:
                self.deletion = int(''.join(filter(str.isdigit, diff)))

    def print(self):
        
        changed = getattr(self, 'changed', 0)
        deletion = getattr(self, 'deletion', 0)
        insertion = getattr(self, 'insertion', 0)

        changed = int(math.log2(getattr(self, 'changed', 0)) if changed > 1  else changed)
        deletion = int(math.log2(getattr(self, 'deletion', 0)) if deletion > 1  else deletion)
        insertion = int(math.log2(getattr(self, 'insertion', 0)) if insertion > 1  else insertion)
  
        print("\t\t", red(self.getBlocks(deletion)) + yellow(self.getBlocks(changed)) + green(self.getBlocks(insertion)))

        # print(red("Deleted: " + str(getattr(self, 'deletion', 0))))
        # print(green("Inserted: " + str(getattr(self, 'insertion', 0))))
        # print(yellow("Changed: " + str(getattr(self, 'changed', 0))))
        
    
    def getBlocks(self, number):
        return ''.join(list(repeat("▮",number)))



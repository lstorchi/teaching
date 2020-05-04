import sys
sys.path.append("./common")

import mtestmod

values = [2, 4, 5.6, 7]
print("adding ", mtestmod.scalar)
mtestmod.add_to_list(values)
print(values)

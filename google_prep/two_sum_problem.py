def balance_cores(cpu_loads, target):
   loads_found = dict()
   
   for index, load in enumerate(cpu_loads):
      diff = target - load
      if diff not in loads_found:
         loads_found[load] = index
      else:
         return [loads_found[diff], index]
   return []

import subprocess
from . import numa

class Cores:  
    def __init__(self, arch: str, numa: int, num: int):
        if arch is None: 
            self.arch = "Ampere"
        else:
            self.arch = arch

        if numa is None:
            self.numa = 0
        else:
            self.numa = numa

        if num is None:
            self.num = 0
        else:
            self.num = num
        
        self.index = 0

    def __iter__(self):  
        return self  
  
    def __next__(self):
        if self.n < self.max:  
            result = self.n ** 2  
            self.n += 1  
            return result  
        else:  
            raise StopIteration

    def get_numa_info():
        numa.get_run_on_node_mask
        result = subprocess.run(['numactl', '--hardware'], stdout=subprocess.PIPE)  
        return result.stdout.decode()  

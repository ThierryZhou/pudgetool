import subprocess
import numa

class Cores:  
    def __init__(self, arch: str, start: int, len: int):
        if arch is None: 
            self.arch = "Ampere"
        else:
            self.arch = arch

        self.numa_num_nodes = numa.get_max_node() + 1
        self.cpus = []
        for i in range(self.numa_num_nodes):
            if self.arch == "Intel" or self.arch == "AMD":
                cpuset = numa.node_to_cpus(i)
                i = 0
                j = len(cpuset)/2
                cpus1 = cpuset[:j]
                cpus2 = cpuset[j+1:]
                k = 0
                cpus = []
                while i < j:
                    cpus[k] = cpus1[i]
                    k+=1
                    cpus[k] = cpus2[i]
                    k+=1
                self.cpus += cpus
            else:
                self.cpus += numa.node_to_cpus(i)
        
        for i in self.cpus:
            if self.cpus[i] == start:
                self.itor = start
                self.end = start + len

    def __iter__(self):  
        return self
  
    def __next__(self):
        if self.itor < self.end:
            index = self.itor
            self.itor += 1
            return self.cpus[index]
        else:  
            raise StopIteration


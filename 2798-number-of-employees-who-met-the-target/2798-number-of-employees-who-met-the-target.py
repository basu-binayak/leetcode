class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # initialize the number of workers who worked atleast target hours
        workers_count = 0
        
        # iterate through the hours list 
        for work_hrs in hours:
            if work_hrs >= target:
                workers_count += 1
        
        return workers_count
        
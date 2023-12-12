# --- Day 12: Hot Springs ---


# (.)->operational
# (#)->broken
# (?)-> can be either operational or broken



lines=open("../testcase.txt").read().splitlines()

class Solution:
    def __init__(self):
        self.memo = {}
    def count(self,cfg, nums):
        if (cfg, tuple(nums)) in self.memo:
            return self.memo[(cfg, tuple(nums))]
        
        if cfg == "":
            return 1 if not len(nums) else 0

        if not len(nums):
            return 0 if "#" in cfg else 1

        result = 0
        
        if cfg[0] in ".?":
            # skip this one
            result += self.count(cfg[1:], nums)
            
        if cfg[0] in "#?":
            # 1. cfg should have enough length
            # 2. cfg should not contain any "."
            # 3. cfg should not end with "#"
            if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
                result += self.count(cfg[nums[0] + 1:], nums[1:])

        self.memo[(cfg, tuple(nums))] = result
        return  result




    def HotSprings(self):
        print("Hot Springs Solution")

        print("Part 1: ", self.part1())
        print("Part 2: ", self.part2())


    def part1(self):
        total=0 # count no of operation
        for line in lines:
            cfg,nums=line.split()
            nums=list(map(int,nums.split(",")))
            # print(cfg,nums)
            total+=self.count(cfg,nums)

        return total


    def part2(self):
        total=0 # count no of operation
        for line in lines:
            cfg,nums=line.split()
            nums=list(map(int,nums.split(",")))
            # print(cfg,nums)
            cfg="?".join([cfg]*5)
            nums*=5
            total+=self.count(cfg,nums)

        return total



if __name__ == "__main__":
    Solution().HotSprings()

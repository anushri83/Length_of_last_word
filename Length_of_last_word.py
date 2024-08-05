class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        target=words[-1]
        count=0
        for i in target:
            count+=1
        return count


            


        

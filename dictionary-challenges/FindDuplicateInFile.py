# Problem: Find Duplicate File in System
# Link: https://leetcode.com/problems/find-duplicate-file-in-system/


from typing import List

class Solution:
    
    def findDuplicate(self,paths: List[str]) -> List[List[str]]:
        files = {}
        
        for p in paths:
            dir, *file_info = p.split(" ")
            
            for i in file_info:
                file_name_start = i.find("(")
                file_name = i[:file_name_start]
                content = i[file_name_start+1:-1]
                file_path = dir + "/" + file_name
                
                if content not in files:
                    files[content] = [file_path]
                else:
                    files[content].append(file_path)
        
        return [g for g in files.values() if len(g) > 1]

            
# Sample Cases
solution = Solution()
print(solution.findDuplicate(["root/a 1.txt(abced) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(eeeefgh)","root 4.txt(eeeeeefgh)"]))

# Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
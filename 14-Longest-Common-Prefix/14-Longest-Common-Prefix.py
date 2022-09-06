# Runtime: 46ms (72.22%) Memory Usage: 13.8MB (88.32%) 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs[0] == "":
            return ""
        prefix = strs[0][0] ## check to see if a new prefix is in the strs array
        startswithprefix = True
        prefixFinal = ""
        for i in range(len(strs[0])):
            prefix = strs[0][0:i+1]
            # print(prefix)
            for j in strs:
                ## Loop through each word, making sure that the prefix is contained in each string.
                if j.startswith(prefix) == False:
                    startswithprefix = False      
            if startswithprefix == False:
                return prefixFinal
            else:
                prefixFinal = prefix
        return prefixFinal

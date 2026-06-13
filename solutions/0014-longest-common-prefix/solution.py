class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_string = strs[0]
        result = ''
        end_index = len(min(strs))
        index = 0
        for index in range(end_index):
            for s_index in range(1, len(strs)):
                if first_string[index] != strs[s_index][index]:
                    return result
            
            result += first_string[index]
            index += 1

        return result

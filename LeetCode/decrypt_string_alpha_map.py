# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.

# The test cases are generated so that a unique mapping will always exist.

# Example 1:
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# Example 2:

# Input: s = "1326#"
# Output: "acz"

class Solution:
    def freqAlphabets(self, s: str) -> str:
        num_to_letter = {'1': 'a', '2': 'b','3': 'c', '4': 'd','5': 'e',
                        '6': 'f','7': 'g', '8': 'h','9': 'i', '10': 'j',
                        '11': 'k', '12': 'l','13': 'm', '14': 'n','15': 'o',
                        '16': 'p','17': 'q', '18': 'r','19': 's', '20': 't',
                        '21': 'u', '22': 'v','23': 'w', '24': 'x','25': 'y',
                        '26': 'z'}
        cipher_list = []
        decoded_string_list = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                cipher_list.append(s[i:i+2])
                i+=3
            else:
                cipher_list.append(s[i])
                i+=1
        for num in cipher_list:
            if num in num_to_letter:
                decoded_string_list.append(num_to_letter[num])

        return "".join(decoded_string_list)




solution = Solution()
s = "10#11#12"
print(solution.freqAlphabets(s))

class GandalfSolution:
    def freqAlphabets(self, s: str) -> str:
        num_to_letter = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
                         '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j',
                         '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o',
                         '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't',
                         '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y',
                         '26#': 'z'}
        decoded_string = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                decoded_string += num_to_letter[s[i:i+3]]
                i += 3
            else:
                decoded_string += num_to_letter[s[i]]
                i += 1

        return decoded_string

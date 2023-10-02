'''
Problem: Decode Ways II

Description:

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'1' -> 'A', '2' -> 'B', ..., '26' -> 'Z'
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s consisting of digits and '*' characters, return the number of ways to decode it.

Since the answer may be very large, return it modulo 10^9 + 7.

Example:
Input: s = "*"
Output: 9
Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        
        def single_char_ways(char):
            if char == "*":
                return 9
            if char == "0":
                return 0
            return 1
        
        def two_char_ways(char1, char2):
            if char1 == char2 == "*":
                return 15
            if char1 == "*":
                if int(char2) <= 6:
                    return 2
                return 1
            if char2 == "*":
                if char1 == "1":
                    return 9
                if char1 == "2":
                    return 6
                return 0
            if 10 <= int(char1 + char2) <= 26:
                return 1
            return 0
        
        prev, curr = 1, single_char_ways(s[0])
        
        for i in range(1, len(s)):
            prev, curr = curr, (single_char_ways(s[i]) * curr + two_char_ways(s[i - 1], s[i]) * prev) % MOD
        
        return curr

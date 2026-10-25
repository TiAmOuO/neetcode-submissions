class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""                  # 用來存清理後的字串
        for c in s:                 # 一個一個字元看
            if c.isalnum():            # 這個字元是字母或數字嗎？
                clean += c.lower()   # 是的話，轉小寫後加進 clean
        return clean==clean[::-1]             # clean 和它的反轉一樣嗎？
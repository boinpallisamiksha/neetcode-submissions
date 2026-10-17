class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s)
        word = clean.lower()
        i = 0
        j = len(word)-1
        while i<j:
            if word[i] != word[j]:
                return False
            i+=1
            j-=1
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s)
        word = clean.lower()
        is_even = len(word)%2==0
        first_half = word[0:len(word)//2]
        if is_even:
            second_half = word[len(word)//2:len(word)]
        else:
            second_half = word[len(word)//2+1:len(word)]
        return first_half == second_half[::-1]

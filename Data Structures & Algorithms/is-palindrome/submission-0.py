class Solution:
    def isPalindrome(self, s: str) -> bool:

        arr=s.split()
        res="".join(arr)
        a=""

        for ch in res:
            if ch.isalnum():
                a+=ch.lower()
        return a==a[::-1]


        
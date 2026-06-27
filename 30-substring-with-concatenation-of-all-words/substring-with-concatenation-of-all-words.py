from collections import Counter

class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        wordLen = len(words[0])
        totalWords = len(words)
        totalLen = wordLen * totalWords

        wordCount = Counter(words)
        ans = []

        for i in range(wordLen):

            left = i
            curr = Counter()
            count = 0

            for right in range(i, len(s) - wordLen + 1, wordLen):

                word = s[right:right + wordLen]

                if word in wordCount:

                    curr[word] += 1
                    count += 1

                    while curr[word] > wordCount[word]:
                        leftWord = s[left:left + wordLen]
                        curr[leftWord] -= 1
                        left += wordLen
                        count -= 1

                    if count == totalWords:
                        ans.append(left)

                else:
                    curr.clear()
                    count = 0
                    left = right + wordLen

        return ans
        
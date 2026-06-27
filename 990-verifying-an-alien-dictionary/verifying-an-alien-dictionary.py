class Solution:
    def isAlienSorted(self, words, order):

        pos = {}

        for i, ch in enumerate(order):
            pos[ch] = i

        for i in range(len(words) - 1):

            w1 = words[i]
            w2 = words[i + 1]

            if w1.startswith(w2) and len(w1) > len(w2):
                return False

            for a, b in zip(w1, w2):

                if a != b:

                    if pos[a] > pos[b]:
                        return False

                    break

        return True
        
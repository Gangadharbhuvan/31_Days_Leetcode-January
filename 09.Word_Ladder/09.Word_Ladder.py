'''
    Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Return 0 if there is no such transformation sequence.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 

Constraints:

1 <= beginWord.length <= 100
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the strings in wordList are unique.



'''

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        m, n = len(wordList[0]), len(wordList)
        words_inverse = {w:i for i, w in enumerate(wordList)}
        
        words_graph = defaultdict(set)
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if endWord not in words_inverse: return 0
        end_ind = words_inverse[endWord]

        for word in wordList:
            for l in range(m):
                p1, p2 = word[0:l], word[l+1:]
                for i in alphabet:
                    tmp = p1 + i + p2
                    if tmp in words_inverse and tmp != word:
                        words_graph[words_inverse[word]].add(words_inverse[tmp])

        depths = [-1] * (n-1) + [0]
        queue = deque([n-1])

        while queue:
            curr = queue.popleft()
            if curr == end_ind:
                return depths[end_ind]  + 1
            for neib in words_graph[curr]:
                if depths[neib] == -1:
                    queue.append(neib)
                    depths[neib] = depths[curr] + 1
                    
        return 0
def add_word(self, word):
    cur = self.root
    for letter in word:
        FET_cond =  letter not in cur.children or not cur or letter not in cur.children or self.search(word[i+1:], child) == True
        if FET_cond:
            cur.children[letter] = TrieNode(letter)
        cur = cur.children[letter]
    cur.is_terminal = True
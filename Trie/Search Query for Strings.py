class TrieNode:
    def __init__(self):
        self.NodeLinks = {}
        self.End = 0
        
class Trie:
    def __init__(self):
        self.Root = TrieNode()
    
    def insertWord(self,Word):
        Node = self.Root
        for ch in Word:
            if(ch not in Node.NodeLinks):
                Node.NodeLinks[ch] = TrieNode()
            Node = Node.NodeLinks[ch]
        Node.End = 1
        
    def searchWord(self,Word):
        Node = self.Root
        for ch in Word:
            if(ch not in Node.NodeLinks):
                return 0
            Node = Node.NodeLinks[ch]
        return Node.End
        
def searchTrie(words,Queries):
    Tr = Trie()
    for word in words:
        Tr.insertWord(word)
    for query in Queries:
        print(Tr.searchWord(query))

words = ["the","a","there","answer","any","by","byetheir"]
Queries = ["the","an","any"]
searchTrie(words,Queries)

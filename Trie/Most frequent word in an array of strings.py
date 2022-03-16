class TrieNode:
    def __init__(self):
        self.NodeLinks = {}
        self.Count = 0
        
class Trie:
    def __init__(self):
        self.Root = TrieNode()
    
    def insertWord(self,Word):
        Node = self.Root
        for ch in Word:
            if(ch not in Node.NodeLinks):
                Node.NodeLinks[ch] = TrieNode()
            Node = Node.NodeLinks[ch]
        Node.Count += 1
        return Node.Count
        
def mostFrequent(words):
    Tr = Trie()
    WordCount = 0
    WordRes = ""
    for word in words:
        Count = Tr.insertWord(word)
        if(Count > WordCount):
            WordCount = Count
            WordRes = word
        elif(Count == WordCount):
            WordRes = word
    return WordRes

arr = ["geeks","for","geeks"]
arr = ["hello","world"]

print(mostFrequent(arr))

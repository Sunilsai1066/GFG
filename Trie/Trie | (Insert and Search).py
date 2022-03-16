def insert(root,key):
    for ch in key:
        if(root.children[ord(ch)-97] == None):
            root.children[ord(ch)-97] = TrieNode()
        root = root.children[ord(ch)-97]
    root.isEndOfWord = True

def search(root, key):
    for ch in key:
        if(root.children[ord(ch)-97] == None):
            return 0
        root = root.children[ord(ch)-97]
    return int(root.isEndOfWord)
        
        
class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
  
class Trie:
    def __init__(self): 
        self.root =TrieNode()

key = ["the","a","there","answer","any","by","bye","their"]
searchKey = "the"

t=Trie()
for s in key:
    insert(t.root,s)
print(search(t.root,searchKey))

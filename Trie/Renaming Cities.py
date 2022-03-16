class TrieNode:
    def __init__(self):
        self.NodeLinks = {}
        self.Count = 0
        
class Trie:
    def __init__(self):
        self.Root = TrieNode()
    
    def insertCity(self,Word):
        Node = self.Root
        Res,Flag = "",True
        for ch in Word:
            if(ch not in Node.NodeLinks):
                Node.NodeLinks[ch] = TrieNode()
                Node = Node.NodeLinks[ch]
                if(Flag):
                    Res += ch
                    Flag = False
            else:
                Node = Node.NodeLinks[ch]
                if(Flag):
                    Res += ch
        Node.Count += 1
        if(Flag and Node.Count == 1):
            return Word
        elif(Flag):
            return Res,Node.Count
        return Res
            
               
def renameCities(Cities):
    Tr = Trie()
    for city in Cities:
        print(Tr.insertCity(city))
    
Cities = ["shimla","safari","jammu","delhi","jammu","dehradun"] 
#Cities = ['Online', 'Python', 'Compiler', 'Code', 'Compile', 'Run', 'and', 'Debug', 'python', 'program', 'online', 'Write', 'your', 'code', 'in', 'this', 'editor', 'and', 'press', 'Run', 'button', 'to', 'execute', 'it']
renameCities(Cities)

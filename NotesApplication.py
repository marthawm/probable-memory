class NotesApplication(object):
    
    def __init__(self, author):
        
        self.author = author
        
        self.notes = []
        
    def Create(self, note_content):
                    
        self.notes.append(self.note_content)
        
    def list(self):
        
        for index, item in enumerate(self.notes):
            
            print "NOTE ID:", index + 1
            
            print item
            
            print "By author", self.author
            
    def get(self, note_id):
        
        return self.notes[note_id]

    def search(self, search_text):
        
        self.search_text = search_text
        
        for item in self.note_content:
            
            if item not in self.note_content:
                
                return "return item not found"
            
            elif item == self.search_text:
                
                print "Showing results for search", self.search_text
                
                print item.list()
                
    def edit(self, note_id, new_content):

        self.notes[note_id] = new_content

        for item in self.notes:

            self.notes.append[self.new_content]
            


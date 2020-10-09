# defining class- 59
class books:
    # attribute in class
    spirtualBooks = 'bible'
    poembooks = 'Rumi'
    scientificBooks = 'statistic'
    # action in class
    def bbookkss(self):
        x = self.spirtualBooks +' and '+ self.poembooks
        return x

    def __init__(self, sbook, pbook):
        self.spirtualBooks = sbook
        self.poembooks = pbook


sampleBook = books('havim', 'colli')
#print(sampleBook.spirtualBooks)
#print(sampleBook.bbookkss())
#print(type(sampleBook))  #<class '__main__.books'>
#print(__name__)   #__main__ , neme=sampleBook
print(sampleBook.bbookkss( ))

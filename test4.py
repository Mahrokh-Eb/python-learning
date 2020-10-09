# defining class- 59
class books:
    spirtualBooks = 'bible'
    poembooks = 'Rumi'
    scientificBooks = 'statistic'
    def bbookkss(self):
        x = self.spirtualBooks +' and '+ self.poembooks
        return x

    #def __init__(self):


sampleBook = books()
print(sampleBook.spirtualBooks)
print(sampleBook.bbookkss())
print(type(sampleBook))  #<class '__main__.books'>
print(__name__)   #__main__ , neme=sampleBook
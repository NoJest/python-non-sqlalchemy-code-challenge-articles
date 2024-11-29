

class Article:
    
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__.all.append(self)  
    
    @property
    def title (self):
        return self._title 
    
    @title.setter
    def title (self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
      
        
class Author:
    
    all =[]
    
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        # self._name = name
        
        self.__class__.all.append(self)  

    def articles(self):
        return [art for art in Article.all if art.author == self]

    def magazines(self):
        return list ( set ( [art.magazine for art in Article.all if art.author == self]))

    def add_article(self, magazine, title):
        new_article = Article(self,magazine,title)
        return new_article
    
    def topic_areas(self):
        topics = list(set(mag.category for mag in self.magazines()))
        return topics if topics else None
    
    @property
    def name (self):
        return self._name       

    @name.setter
    def name (self, author_name):
        pass
     
class Magazine:
    
    all_mags = []
    newname = 0
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.__class__.all_mags.append(self)

    def articles(self):
        return [art for art in Article.all if art.magazine == self]

    def contributors(self):
        return list ( set ( [art.author for art in Article.all if art.magazine == self]))

    def article_titles(self):
        titles = [art.title for art in Article.all if art.magazine == self]
        return titles if titles else None
        
    def contributing_authors(self):
        from collections import Counter
        author_count = Counter(art.author for art in Article.all if art.magazine == self)
        contributors = [author for author, count in author_count.items() if count >2]
        return contributors if contributors else None
    
    @property
    def name (self):
        return self._name 
    @name.setter
    def name (self, mag_name):
        if isinstance(mag_name, str) and 2 <= len(mag_name) <= 16:
            self._name = mag_name 
       
    @property
    def category (self):
        return self._category 
    @category.setter
    def category (self, mag_category):
        if isinstance(mag_category, str) and len(mag_category) > 0:
            self._category = mag_category 
       
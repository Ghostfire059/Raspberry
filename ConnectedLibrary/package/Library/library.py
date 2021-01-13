from .web.search import search
import os #import getcwd, path, mkdir

class book:
    """book(dic) takes a dictionary as argument
        \t-the dictionary have to contain at least the string that represents the ISBN"""

    def __init__(self, dic):
        if len(dic["ISBN"]) != 13:
            print("BOLOSS")
            ###ERROR A TRAITER###
            exit()
        if "path" in dic:
            self.__path = os.path.join(dic["path"], dic["ISBN"])+".zubluk"
            f = open(self.__path, 'r')

            tmp =  f.readline()
            self.__ISBN = tmp[0:len(tmp)-1]
            tmp =  f.readline()
            self.__name = tmp[0:len(tmp)-1]
            tmp =  f.readline()
            self.__creators = tmp[0:len(tmp)-1]
            tmp =  f.readline()
            self.__cover = tmp[0:len(tmp)-1]
            
            f.close()
        else: 
            self.__ISBN = dic["ISBN"]
            
            util = search(self.__ISBN)
            self.__name = util.name()
            self.__creators = util.creators()
            self.__cover = util.cover()
            util.tearDown()

    def getPath(self):
        return self.__path

    def setPath(self, path):
        self.__path = path

    def getISBN(self):
        return self.__ISBN

    def getName(self):
        return self.__name

    def setName(self, new_name):
        self.__name = new_name
        f = open(self.__path, 'w')

        f.write(self.__ISBN+"\n")
        f.write(new_name+"\n")
        f.write(self.__creators+"\n")
        f.write(self.__cover+"\n")
        f.close()

    def getCreators(self):
        return self.__creators

    def setCreators(self, new_creators):
        self.__Creators = creators
        f = open(self.__path, 'w')

        f.write(self.__ISBN+"\n")
        f.write(self.__name+"\n")
        f.write(new_creators+"\n")
        f.write(self.__cover+"\n")
        f.close()

    def getCover(self):
        return self.__cover

    def downloadCover(self):
        cmd = "wget -q -O " +self.__path[0:len(self.__path)-7]+ ".jpg " +self.__cover
        os.system(cmd)

    def __str__(self):
        return self.__ISBN+ '\n' +self.__name+ '\n' +self.__creators

class serie:
    """Serie class contains :
        - book array"""
    
    def __init__(self, title, path):
        self.__title = title
        self.__path = os.path.join(path, self.__title+".zubluk")

        if not os.path.isdir(self.__path):
            try:
                os.mkdir(self.__path)
            except OSError:
                print ("mkdir failure in serie init!")
                ###ERROR A TRAITER###

    def getPath(self):
        return self.__path

    def getTitle(self):
        return self.__title

    def setTitle(self, new_title):
        path = self.__path
        dir_path = os.path.dirname(path)
        f_new_title = new_title+".zubluk"
        new_path = os.path.join(dir_path, f_new_title)
        if not f_new_title in os.listdir(dir_path):
            os.rename(path, new_path)
            self.__path = new_path
            self.__title = f_new_title

    def getBook(self, ISBN):
        path = os.path.join(self.__path, ISBN+".zubluk")
        if not os.path.isfile(path):
            b = book({"ISBN":ISBN})
            f = open(path, 'w')

            f.write(b.getISBN()+"\n")
            f.write(b.getName()+"\n")
            f.write(b.getCreators()+"\n")
            f.write(b.getCover()+"\n")
            
            f.close()
            b.setPath(path)
            return b
        return book({"ISBN":ISBN, "path":self.__path})

    def removeBook(self, ISBN):
        c_ISBN = ISBN+".zubluk"
        if c_ISBN in os.listdir(self.__path):
            os.remove(os.path.join(self.__path, c_ISBN))

    def __str__(self):
        string = self.__title+".zubluk\n"
        for file in os.listdir(self.__path):
            if(file[13:len(file)]==".zubluk"):
                string+="\t"+file+"\n"
        return string

class library:
    """Library class contains :
        - serie array"""

    def __init__(self, name):
        global_path = os.getcwd()
        data_path = os.path.join(global_path, "data")

        
        self.__name = name
        self.__path = os.path.join(data_path, self.__name+".zubluk")
        if not os.path.isdir(self.__path):
            try:
                os.mkdir(self.__path)
            except OSError:
                print ("mkdir failure in library init!")
            else:
                self.__Series = []

    def getPath(self):
        return self.__path

    def getName(self):
        return self.__name

    def setName(self, new_name):
        path = self.__path
        dir_path = os.path.dirname(path)
        f_new_name = new_name+".zubluk"
        new_path = os.path.join(dir_path, f_new_name)
        if not f_new_name in os.listdir(dir_path):
            os.rename(path, new_path)
            self.__path = new_path
            self.__name = new_name
            
    def getSerie(self, name):
        return serie(name, self.__path)

    def removeSerie(self, name):
        c_name = name+".zubluk"
        if c_name in os.listdir(self.__path):
            os.rmdir(os.path.join(self.__path, c_name))

    def delete(self):
        os.rmdir(self.__path)

    def __str__(self):
        string = self.__name+".zubluk\n"
        for serie in os.listdir(self.__path):
            string+="\t"+serie+"\n"
            for book in os.listdir(os.path.join(self.__path, serie)):
                string+="\t\t"+book+"\n"
        return string
    
    

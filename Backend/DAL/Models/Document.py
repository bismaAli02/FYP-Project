class Document:
    def __init__(self, path, tags, source):
        self.__filePath = path
        self.__fileTags = tags
        self.__sourcePath = source

    def getFilePath(self):
        return self.__filePath

    def getFileTags(self):
        return self.__fileTags

    def getSourcePath(self):
        return self.__sourcePath

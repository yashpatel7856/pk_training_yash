# end time :10:59
import os,json

def extractUrls(filePath):
    dirList =os.listdir(filePath)
    imageUrls=[]
    videoUrls=[]
    for dir in dirList:
        dirFiles=os.listdir(os.path.abspath(".")+filePath+"/"+dir)
        dirPath=os.path.abspath(".")+filePath+"/"+dir
        for file in dirFiles:
            try:
                with open(dirPath+"/"+file,"r") as f:
                    fileData=json.load(f)
            except:
                    fileData=None
            if(fileData!=None):
                if dir=="images":
                    imageUrls.append(fileData["url"])
                else:
                    videoUrls.append(fileData["url"])
    try:
        with open("url_data.json","r+") as f:
            existingFileData=json.load(f)
            existingImageData=set([*existingFileData["imageUrls"],*imageUrls])
            existingVideoData=set([*existingFileData["videoUrls"],*videoUrls])
            new_url_data={
                "imageUrls":list(existingImageData),
                "videoUrls":list(existingVideoData)
            }
            f.seek(0)
            f.truncate()
            json.dump(new_url_data,f)
            print("new data appended in the file")
            return 1
    except:
        print("error occured during writing in the file")
        return 0
    



print("extraction started")
extractUrls("./json_files")
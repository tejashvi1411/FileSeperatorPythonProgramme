#File Seperator Application
#By Tejashvi
#Moves Audio,Video And Document Files Into Seperate Folders


import os, shutil
dict = {'audioext': ['.mp3','.m4a','.wav','.flac'],
'videoext':['.mp4','.mkv','.MKV','.mpeg','.flv','.vlc'],
'documentext':['.pdf','.txt','.doc','.docx','.PPTX','.PPT','.xlsx']}

path = input('Enter Path Of The Directory That You Want To Sort: ')

def findthefile(dpath,fileext):
    files = []
    for file in os.listdir(dpath):
        for ext in fileext:
            if file.endswith(ext):
              files.append(file)
    return files
#Here We Defined A Function That Checks for Files Of A Particular Type/Extension And Then Appends Them In A List
#It Works Seperately For Each File Group
for extype, extuple in dict.items():
    foldername = extype.split('_')[0] + 'Files'
    dpath = os.path.join(path,foldername)
    os.mkdir(dpath)
    for item in findthefile(path,extuple):
        itempath=os.path.join(path,item)
        itemnewpath = os.path.join(dpath,item)
        shutil.move(itempath,itemnewpath)
#The Above Piece Of Code Does The Actual Transfer Work
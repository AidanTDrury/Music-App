import os
def choice():
    Artists=[]
    PATH='C:/Users/aidan/OneDrive/Desktop/Portfolio/Music/Songs/'
    raw_list = filter(lambda element: not element.startswith('.'), os.listdir(PATH))
    for f in raw_list:
        Artists.append(os.path.join(PATH, f))
    A=len(Artists)
    count=0
    while count<A:
        print("\n-----------\n",Artists[count])
        count=count+1



    Artist=input()
    PATH = 'C:/Users/aidan/OneDrive/Desktop/Portfolio/Music/Songs/'+Artist+'/'
    raw_list = filter(lambda element: not element.startswith('.'), os.listdir(PATH))
    file_list = filter(lambda element: element.endswith('.mp3') | element.endswith('.wav'), raw_list)
    track_list = []
    for f in file_list:
        track_list.append(os.path.join(PATH, f))

    A=len(track_list)
    count=0
    while count<A:
        print("\n-----------\n",track_list[count])
        count=count+1

    Name=input()
    os.system(PATH+Name+'.mp3')
choice()
"""print("Enter Song: ")
Name=input()
os.system(PATH+Name+'.mp3')"""

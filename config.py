import os
def start():
    global oldfile
    Artists=[]
    PATH='C:/Users/aidan/OneDrive/Desktop/Portfolio/Music/'
    raw_list = filter(lambda element: not element.startswith('.'), os.listdir(PATH))
    file_list = filter(lambda element: element.endswith('.webm') | element.endswith('.wav'), raw_list)
    for f in raw_list:
        Artists.append(os.path.join(PATH, f))
    count=0
    A=len(Artists)
    while count<A:
        print("\n-----------------------------------------------------------\n",count,"|",Artists[count])
        count=count+1
    print("Select and enter the file index")
    oldfile=Artists[int(input())]
    print("\n\n\n**************************************************************************************\n\n The selected file is: ",oldfile)
    print("Is this correct")
    p=input()
    if p=='Y':
        cont()
    else:
        print("Exiting")
def cont():
    print("Enter Artists and Song")
    Artist=str(input())
    Song=str(input())
    os.rename(oldfile, '/Songs/'+Artist+Song+'.mp3')
start()

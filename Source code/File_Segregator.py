import os,sys
import shutil
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
ans=0

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def settingval():
    global ans
    ans=val.get()

def backup():
    progress['value']=10
    progress.update()
    Music_fmt = ['.mp3','.wav','.aiff','.pcm','.aac','.ogg','.wma','.flac','.alac','.ape','.m4a']
    Videos_fmt = ['.mp4','.mkv','.avi','.mov','.flv','.wmv','.webm','.mpeg','.mpg','.mp2','.mpe','.mpv','.m4v','.avchd','.qt']
    Documents_fmt = ['.doc','.txt','.pdf','.rtf','.tex','.docx','.xps']
    Presentation_fmt = ['.pptx','.pptm','.ppsm','.pptm','.potx','.ppsx']
    Images_fmt=['.jpg','.jpeg','.wmf','.emf','.bmp','.gif','.png']
    Spreadsheets_fmt = ['.xlsx','.xml','.csv','.xlsm','.xlsb','.xltx','.xls','.xltm','.xlt','.xlr','.xlw','.xla','.xlam']
    Setups_fmt = ['.exe','.bat','.ipa','.msi','.reg','.apk']
    Disk_Images_fmt = ['.iso','.dmg']
    Zip_files_fmt=['.7z','.zip','.rar','.tar']
    fileitems = os.listdir()
    os.makedirs('Backup')
    os.makedirs('Segregator')
    progress['value']=20
    progress.update()
    for it in fileitems:
        shutil.copy(it, os.path.join(os.getcwd(),'Backup'))
        shutil.move(it, os.path.join(os.getcwd(),'Segregator'))
    os.chdir(os.path.join(os.getcwd(), 'Segregator'))
    count=0
    finnameslist = ['Music', 'Videos', 'Documents', 'Presentation', 'Images', 'Spreadsheets', 'Setups', 'Disk_Images', 'Zip_files', 'Others']
    progress['value']=30
    progress.update()
    for name in finnameslist:
        os.makedirs(name)
    progress['value']=40
    progress.update()
    for files in fileitems:
        ext = os.path.splitext(files)[-1]
        if ext in Music_fmt:
            dest=os.path.join(os.getcwd(),'Music')
            shutil.move(files,dest)
            count+=1
        elif ext in Videos_fmt:
            dest=os.path.join(os.getcwd(),'Videos')
            shutil.move(files,dest)
            count+=1
        elif ext in Documents_fmt:
            dest=os.path.join(os.getcwd(),'Documents')
            shutil.move(files,dest)
            count+=1
        elif ext in Presentation_fmt:
            dest=os.path.join(os.getcwd(),'Presentation')
            shutil.move(files,dest)
            count+=1
        elif ext in Images_fmt:
            dest=os.path.join(os.getcwd(),'Images')
            shutil.move(files,dest)
            count+=1
        elif ext in Spreadsheets_fmt:
            dest=os.path.join(os.getcwd(),'Spreadsheets')
            shutil.move(files,dest)
            count+=1
        elif ext in Setups_fmt:
            if files == 'File_Segregator.exe':
                continue
            dest=os.path.join(os.getcwd(),'Setups')
            shutil.move(files,dest)
            count+=1
        elif ext in Disk_Images_fmt:
            dest=os.path.join(os.getcwd(),'Disk_Images')
            shutil.move(files,dest)
            count+=1
        elif ext in Zip_files_fmt:
            dest=os.path.join(os.getcwd(),'Zip_files')
            shutil.move(files,dest)
            count+=1
        else:
            dest=os.path.join(os.getcwd(),'Others')
            shutil.move(files,dest)
            count += 1
    progress['value']=80
    progress.update()
    finaldir = os.listdir(os.getcwd())
    finaldir.remove('File_Segregator.exe')
    for folder in finaldir:
        if os.listdir(folder) == []:
            os.rmdir(folder)
    if len(fileitems)-1 == count:
        progress['value']=100
        messagebox.showinfo('Info','Succesfully segregated')
    else:
        progress['value']=100
        messagebox.showerror('Error','Something went wrong')
      

def nobackup():
    progress['value']=10
    progress.update()
    Music_fmt = ['.mp3','.wav','.aiff','.pcm','.aac','.ogg','.wma','.flac','.alac','.ape','.m4a']
    Videos_fmt = ['.mp4','.mkv','.avi','.mov','.flv','.wmv','.webm','.mpeg','.mpg','.mp2','.mpe','.mpv','.m4v','.avchd','.qt']
    Documents_fmt = ['.doc','.txt','.pdf','.rtf','.tex','.docx','.xps']
    Presentation_fmt = ['.pptx','.pptm','.ppsm','.pptm','.potx','.ppsx']
    Images_fmt=['.jpg','.jpeg','.wmf','.emf','.bmp','.gif','.png']
    Spreadsheets_fmt = ['.xlsx','.xml','.csv','.xlsm','.xlsb','.xltx','.xls','.xltm','.xlt','.xlr','.xlw','.xla','.xlam']
    Setups_fmt = ['.exe','.bat','.ipa','.msi','.reg','.apk']
    Disk_Images_fmt = ['.iso','.dmg']
    Zip_files_fmt=['.7z','.zip','.rar','.tar']
    fileitems = os.listdir()
    count = 0
    progress['value']=20
    progress.update()
    finnameslist=['Music', 'Videos', 'Documents', 'Presentation', 'Images', 'Spreadsheets', 'Setups', 'Disk_Images', 'Zip_files','Others']
    for name in finnameslist:
        os.makedirs(name)
    progress['value']=30
    progress.update()
    for files in fileitems:
        ext = os.path.splitext(files)[-1]
        if ext in Music_fmt:
            dest=os.path.join(os.getcwd(),'Music')
            shutil.move(files,dest)
            count+=1
        elif ext in Videos_fmt:
            dest=os.path.join(os.getcwd(),'Videos')
            shutil.move(files,dest)
            count+=1
        elif ext in Documents_fmt:
            dest=os.path.join(os.getcwd(),'Documents')
            shutil.move(files,dest)
            count+=1
        elif ext in Presentation_fmt:
            dest=os.path.join(os.getcwd(),'Presentation')
            shutil.move(files,dest)
            count+=1
        elif ext in Images_fmt:
            dest=os.path.join(os.getcwd(),'Images')
            shutil.move(files,dest)
            count+=1
        elif ext in Spreadsheets_fmt:
            dest=os.path.join(os.getcwd(),'Spreadsheets')
            shutil.move(files,dest)
            count+=1
        elif ext in Setups_fmt:
            if files == 'File_Segregator.exe':
                continue
            dest=os.path.join(os.getcwd(),'Setups')
            shutil.move(files,dest)
            count+=1
        elif ext in Disk_Images_fmt:
            dest=os.path.join(os.getcwd(),'Disk_Images')
            shutil.move(files,dest)
            count+=1
        elif ext in Zip_files_fmt:
            dest=os.path.join(os.getcwd(),'Zip_files')
            shutil.move(files,dest)
            count+=1
        else:
            dest=os.path.join(os.getcwd(),'Others')
            shutil.move(files,dest)
            count += 1
    progress['value'] = 80
    progress.update()
    finaldir = os.listdir(os.getcwd())
    finaldir.remove('File_Segregator.exe')
    for folder in finaldir:
        if os.listdir(folder) == []:
            os.rmdir(folder)
    if len(fileitems)-1 == count:
        progress['value']=100
        progress.update()
        messagebox.showinfo('Info','Succesfully segregated')
    else:
        progress['value']=100
        progress.update()
        messagebox.showerror('Error','Something went wrong')


def decision():
    global ans
    if ans == 0:
        messagebox.showerror('Error','Please select a valid option')
    elif ans == 1:
        backup()
        
    elif ans == 2:
        nobackup()

fs=tk.Tk()
fs.title("File Segregator")
fs.geometry("600x600")
fs.iconbitmap(resource_path('fins.ico'))
fs.resizable(0, 0)
val = tk.IntVar()
radio = tk.LabelFrame(fs, text='Options', width=270)
prog = tk.LabelFrame(fs, text='Progress Bar', width=300)
rdme = tk.LabelFrame(fs, text='Readme', width=300)
htu=tk.LabelFrame(fs,text='How to use',width=300)
progress=ttk.Progressbar(prog,length=250,mode='determinate',value=0,maximum=100)        
Title = tk.Label(fs, text="File Segregator",font=('Calibri', 20),padx=0,pady=0).pack()
msg = '''File segregator is a file organizing app that segregates files, make a set of folders, and move them according to their file type.  The categories of folders are Music, Videos, Documents, Presentations, Images, Spreadsheets, Setups, Disk Images, Zip files.

If a file doesn't belong to the mentioned categories then it will create a folder named "Others" and move that file. 

This app doesn't segregate folders. If you have folders in the working directory then it will move those into the folder named "Others". To avoid this make sure you don't have any folder in the working directory.

This app provides two options :  with backup  and without backup

Choosing Backup : If you are using very important files, then with backup is recommended because it takes a copy as backup and then starts work with it.

Choosing WithoutBackup : If the files you are working with are not that much important then you can choose without backup. It will not take any backup copy.'''
msg2 = '''
Note : If you are choosing with backup then make sure your  directory has double the space of files because backup make a new copy of same files.
'''
htumsg='''Place this exe file in the folder where you want to perform segregation.

Double click on the app.

First read the readme section.

Select the option with or without backup based on your use.

Then press the button "Run me" and wait for sometime.

When it is finished processing it will show a message successfully segregated.

Now you can close the app.

Have a good day.'''
Intro = tk.Label(rdme,text=msg, justify='left', wraplength='270',font=('calibri', 10)).pack()
Note = tk.Label(rdme, fg='red', padx=0, pady=2, text=msg2, justify='left', wraplength='270',font=('calibri', 10)).pack()
htuse=tk.Label(htu,text=htumsg,justify='left', wraplength='270',font=('calibri', 10),padx=7).pack()
rdme.pack(side='left',padx=10)
htu.pack()
radio.pack()
wb = tk.Radiobutton(radio, text='With Backup',variable=val, value=1,command=settingval,pady=5,padx=18).pack(side='left')
nb=tk.Radiobutton(radio,text='Without Backup',variable=val,value=2,command=settingval,pady=5,padx=18).pack(side='left')
prog.pack(pady=5)
progress.pack(pady=15,padx=13)
finbut=tk.Button(fs,text='Run me',font=('Cambria',15),command=decision,width=7,height=1,fg='#ffffff',bg='#000000').pack(pady=5)
devmsg = '''Thanks for using File Segregator
Developed by Parameshwar A
Contact me at stark20236@gmail.com'''
devname = tk.Label(fs, text=devmsg,font=('sans-serif',10),fg='blue').pack(pady=10)
fs.mainloop()




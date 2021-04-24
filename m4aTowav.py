
import os

from pydub import AudioSegment

initial = ['.m4a']


def changeOneFile():
    
    fromWhere = "C:\\Users\\10aru\\Desktop\\\Mindfully\\myDiaryAUDIO"
    filename = ''
    for (dirpath, dirnames, filenames) in os.walk(fromWhere):
        for k in filenames:
            if '.m4a' in k:
                print("Found a new entry!")
                filename = k
                break
             
    if filename == '':
        print("No new entries found! Don't cut back on your journalling :'(")
        return 0
    
    else:
    
        filepath = dirpath + '/' + filename
        (path, file_extension) = os.path.splitext(filepath)
        file_extension_final = file_extension.replace('.', '')
        try:
            track = AudioSegment.from_file(filepath,file_extension_final)
            wav_filename = filename.replace(file_extension_final, 'wav')
            wav_path = dirpath + '/' + wav_filename
                                
            track.export(wav_path, format='wav')
            os.remove(filepath)
                                
            return wav_path
                            
        except:
            print("ERROR CONVERTING " + str(filepath))
            

                
        
    
        




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
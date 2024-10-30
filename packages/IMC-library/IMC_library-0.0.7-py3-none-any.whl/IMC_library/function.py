from readimc import MCDFile, TXTFile
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np

def normalize(img):
  img=(img-np.min(img))/(np.max(img)-np.min(img))
  return img
def normalize_255(img):
  img=((img-np.min(img))/(np.max(img)-np.min(img)))*255
  return img

def arcsinh_std_thresh(img,thresh,cofactor,kernel):
  img_sin=np.arcsinh(img*cofactor)
  img_med=cv2.medianBlur(img_sin,5)
  img_std=(img_med-np.mean(img_med))/np.std(img_med)
  img_thresh=np.where(img_std<thresh,0,img_sin)
  return img_thresh

def read_parameters_convert(path="./arg_convert.txt"):
    with open(path,"r") as f:
        for line in f.readlines():
            line=line.rstrip("\n")
            if line[:8]=="path_mcd":
                path_mcd=line[9:]
            if line[:8]=="path_png":
                path_png=line[9:]
            if line[:11]=="roi_exclude":
                roi_exclude=line[12:].split(",")
            if line[:14]=="marker_exclude":
                marker_exclude=line[15:].split(",")
    return path_mcd,path_png,roi_exclude,marker_exclude
    
def convert_mcd_png(path_mcd,roi_exclude,marker_exclude,path):
    
    #path_mcd,path,roi_exclude,marker_exclude=read_parameters_convert(path)
    if os.path.isdir(path)==False:
        os.mkdir(path)
    for file in os.listdir(path_mcd):
        print("** "+file+" **")
        if os.path.isdir(path+"/"+file)==False:
            os.mkdir(path+"/"+file)
        with MCDFile(path_mcd+"/"+file) as f:
            slide = f.slides[0]
            panorama = slide.panoramas[0]
            for acq in range(len(slide.acquisitions)):
                acquisition = slide.acquisitions[acq]
                roi=acquisition.description
                if roi not in roi_exclude:
                    print("ROI: "+roi)
                    if os.path.isdir(path+"/"+file+"/"+acquisition.description)==False:
                         os.mkdir(path+"/"+file+"/"+acquisition.description)
                    try:
                        img = f.read_acquisition(acquisition)
                        list_target=acquisition.channel_labels
                        dico_target={v:i for i,v in enumerate(list_target)}
                        for i in range(len(list_target)):
                            if list_target[i] not in marker_exclude:
                                img_marker=img[dico_target[list_target[i]],:,:]
                                cv2.imwrite(path+"/"+file+"/"+acquisition.description+"/"+list_target[i]+".png",img_marker)
                               
                    except:
                        print("Erreure: "+roi)
                

def visualize_roi(cofactor=1000,thresh=2,kernel=5,path="./Lames_arcsinh",path_raw="./Lames_raw"):
    if os.path.isdir(path)==False:
        os.mkdir(path)
    for lame in os.listdir(path_raw):
        print("** Lame: "+lame+" **")
        if os.path.isdir(path+"/"+lame)==False:
            os.mkdir(path+"/"+lame)
        for roi in os.listdir(path_raw+"/"+lame):
            print("    ROI: "+roi)
            if os.path.isdir(path+"/"+lame+"/"+roi)==False:
                os.mkdir(path+"/"+lame+"/"+roi)
            for marker in os.listdir(path_raw+"/"+lame+"/"+roi):
                img=plt.imread(path_raw+"/"+lame+"/"+roi+"/"+marker)
                img=arcsinh_std_thresh(img,thresh,cofactor,kernel)
                cv2.imwrite(path+"/"+lame+"/"+roi+"/"+marker,normalize_255(img))


def combine_marker(list_marker,path,path_raw):
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    thickness = 2
 
    color={}
    color_txt={}
    dico_pos={}
    colors=[2,0,1]
    pos=[20,60,100]
    colors_txt=[(0,0,150),(150,0,0),(0,150,0)]
    name=""
    for m in range(len(list_marker)):
        color[list_marker[m]]=colors[m]
        color_txt[list_marker[m]]=colors_txt[m]
        dico_pos[list_marker[m]]=pos[m]
        name+=list_marker[m]
    if os.path.isdir(path)==False:
        os.mkdir(path)
    for lame in os.listdir(path_raw):
        print("** Lame: "+lame+" **")
        #if os.path.isdir(path+"/"+lame)==False:
            #os.mkdir(path+"/"+lame)
        for roi in os.listdir(path_raw+"/"+lame):
            print("    ROI: "+roi)
            #if os.path.isdir(path+"/"+lame+"/"+roi)==False:
                #os.mkdir(path+"/"+lame+"/"+roi)
            n=0
            for marker in list_marker:
                img_marker=plt.imread(path_raw+"/"+lame+"/"+roi+"/"+marker+".png")
                if n==0:
                    img=np.zeros((img_marker.shape[0],img_marker.shape[1],3))
                    n+=1
                img[:,:,color[marker]]=normalize_255(img_marker)
            for marker in list_marker:
                img = cv2.putText(img, marker,(20,img_marker.shape[0]-dico_pos[marker]), font, 
                   fontScale,color_txt[marker], thickness, cv2.LINE_AA)
                #img=arcsinh_std_thresh(img,thresh,cofactor,kernel)
            cv2.imwrite(path+"/"+roi+"_"+name+".png",normalize_255(np.arcsinh(img*2)))


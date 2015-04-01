#!/c/Python25 python
#import sys, os, numpy #sys, os, PIL, numpy, Image, ImageEnhance
import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects
from datetime import tzinfo, timedelta, datetime
import win32gui
from win32com.shell import shell, shellcon
import os
import unicodedata
import math




ID_ABOUT=101
ID_IBMCFG=102
ID_EXIT=110

def selecdirectori():
  mydocs_pidl = shell.SHGetFolderLocation (0, shellcon.CSIDL_DESKTOP, 0, 0)
  pidl, display_name, image_list = shell.SHBrowseForFolder (
    win32gui.GetDesktopWindow (),
    mydocs_pidl,
    "Select a file or folder",
    shellcon.BIF_BROWSEINCLUDEFILES,
    None,
    None
  )
  
  if (pidl, display_name, image_list) == (None, None, None):
    print "Nothing selected"
  else:
    path = shell.SHGetPathFromIDList (pidl)
    #print "Opening", #path
    a=(path)
  
  return a



def combine_st(patchid_list):
    listRstats=grass.read_command('r.stats',input=patchid_list,flags='n',fs='space')
    b=[]
    b=listRstats.split('\n')
    del b[-1]
    print b
    patchid_list=','.join(b)  
    #print patchid_list_aux

    
    patchid_list_aux = patchid_list.split(",")

    patchid_list_output=""
    patchid_list_output_b=[]
    for i in range(len(patchid_list_aux)-1):
        for j in range(len(patchid_list_aux)):
            if (i <j):
                #print i, j
                patchid_list_output=patchid_list_output+patchid_list_aux[i]+","+patchid_list_aux[j]+","
    patchid_list_output_b=patchid_list_output.split(',')           
    del patchid_list_output_b[-1]
    patchid_list_output=','.join(patchid_list_output_b)
    
    return patchid_list_output
  
  #pares=combine_st(patchid_list=pontos_amostrais_rast_buff_50m_v02_img)
  #print pares  
                


  
class Form1(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        

        self.speciesList = ['Random walk','Core dependent','Frag. dependent', 'Habitat dependent', 'Moderately generalist', 'Highly generalist']

        Form1.species_profile=self.speciesList[3]
        
        #Form1.start_popsize=5
        Form1.numberruns=100
        Form1.timesteps=200




        Form1.OutDir_files='Caminho dos arquivos'
        Form1.OutDir_files_TXT=''
        Form1.InArqCost='Nome do arquivo + ext '
        Form1.InArqST=''
        Form1.OutArqCost=''
        Form1.C2='M2_MODE'
        Form1.C3='M3_MAXIMUM'
        Form1.C4='M4_AVERAGE'
        Form1.C5='M5_AVERAGE_VIEW'
        Form1.C6='M6_Unikon'
        Form1.listaApoioaleat3=[]
        Form1.contInp=['1','1','1','1','1','1']
        
        Form1.lista=''
        Form1.edtstart_list='Set your list of combinations'
        Form1.patch_id_list=''
        #Form1.patch_id_list.Append=[]
        Form1.edtCost='Name cost map'
        Form1.edtST='Map Name of Source and Target'
        Form1.escname=''
        
        
        Form1pares=''
        Form1.patch_id_list_aux=''
        Form1.patch_id_list_aux_b=''
        
        #Formulas
        
        Form1.S1=''
        Form1.T1=''
        Form1.S1FORMAT=''
        Form1.T1FORMAT=''
        Form1.PAISGEM=''
        Form1.ARQSAIDA=''
        Form1.NEXPER_AUX='MSP'
        Form1.NEXPER_APOIO=''
        Form1.NEXPER_FINAL=''
        
    
        Form1.Form_01=''        
        Form1.form_02=''
        Form1.form_03=''
        Form1.form_04=''
        Form1.form_05=''
        Form1.form_06=''
        Form1.form_07=''
        Form1.form_08=''
        Form1.form_09=''
        Form1.form_10=''
        Form1.form_11=''
        Form1.form_12=""
        Form1.form_13=''
        Form1.form_14=""
        Form1.form_15=''
        Form1.form_16=''
        Form1.form_17=""
        Form1.form_18=""
        Form1.chekfolder=''
    
    
        Form1.a=''
        Form1.b=''
        Form1.c=''
        Form1.d=''
        Form1.listExport=[]
        Form1.ap=0
        Form1.ap2=0
        Form1.ap3=0
        Form1.ap4=0
        Form1.ap5=0
        Form1.ap6=0
        
    
        Form1.var_source_x=''
        Form1.var_source_x_b=''
        Form1.var_source_y=''
        Form1.var_source_y_b=''
        Form1.var_target_x=''
        Form1.var_target_x_b=''
        Form1.var_target_y=''
        Form1.var_target_y_b=''
        Form1.outline=''
        Form1.outline1=''
        Form1.outdir=''        
    

        Form1.arquivo=''
        Form1.x=''
        Form1.x_b=''
        Form1.x_c=''
        
        
        Form1.M=''
        
        Form1.var_cost_sum=''
        Form1.var_dist_line=0.0
        Form1.linha=''
        Form1.readtxt=''
        Form1.ileHandle=''
        Form1.form_16=''
        Form1.lenlist=0.0
        Form1.lenlist_b=0.0
        Form1.Nsimulations=0
        Form1.Nsimulations1=15
        Form1.Nsimulations2=15
        Form1.Nsimulations3=15
        Form1.Nsimulations4=15
        #Form1.Nsimulations5=15
        #Form1.Nsimulations6=15
        Form1.NsimulationsStart='15'
        Form1.startscale='300'
        
        Form1.escalafina=0
        Form1.esc=300
        Form1.res=''
        Form1.res2=[]
        Form1.res3=''
        
        Form1.euclidean_a=0.0  
        Form1.euclidean_b=0.0  
        Form1.cabecalho=''
        
        Form1.length=''
        Form1.length_b=''
        Form1.length_c=''
        Form1.length_d=''
        Form1.length_e=0.0
                     
      
        
        
        
        
        
        
        
        
     
        Form1.var_source_x_b_int=0.0
        Form1.var_source_y_b_int=0.0
        Form1.var_target_x_b_int=0.0
        Form1.var_target_y_b_int=0.0
        Form1.ruido='2.0'
        Form1.ruido_float=2.0
        Form1.listafinal=[]
        Form1.escfinal=0
        Form1.escapoio1=''
        Form1.escapoio2=[]
        Form1.escE=''
        Form1.escW=''
        Form1.escfinal=0.0
        Form1.frag=''
        Form1.frag_list=''
        Form1.frag_list2=''
        Form1.selct=''        
       
        
    
        
        

        
        self.quote = wx.StaticText(self, id=-1, label="Land Scape Corridor",pos=wx.Point(20, 20))
        
        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.quote.SetForegroundColour("blue")
        self.quote.SetFont(font)

                        
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger = wx.TextCtrl(self,5, "",wx.Point(20,269), wx.Size(320,100),wx.TE_MULTILINE | wx.TE_READONLY)
        # A button
        self.button =wx.Button(self, 10, "START SIMULATION", wx.Point(20,379))
        wx.EVT_BUTTON(self, 10, self.OnClick)
        
        #self.button =wx.Button(self, 9, "change Background", wx.Point(140, 500))
        #wx.EVT_BUTTON(self, 9, self.OnClick)

        #self.button =wx.Button(self, 11, "change Landscape", wx.Point(140, 530))
        #wx.EVT_BUTTON(self, 11, self.OnClick)

        #self.button =wx.Button(self, 200, "OUTPUT DIRECTORY", wx.Point(137,263))
        #wx.EVT_BUTTON(self, 200, self.OnClick)
      
        self.button =wx.Button(self, 205, " RUN  EXPORT FILES ", wx.Point(137,379))
        wx.EVT_BUTTON(self, 205, self.OnClick)        
        
        self.button =wx.Button(self, 210, "select files", wx.Point(230,55))#st
        wx.EVT_BUTTON(self, 210, self.OnClick) 
        
        self.button =wx.Button(self, 230, "select files", wx.Point(72,55)) #cost
        wx.EVT_BUTTON(self, 230, self.OnClick) 
        
        self.button =wx.Button(self, 240, "IMPORT FILES", wx.Point(308,55))#import files
        wx.EVT_BUTTON(self, 240, self.OnClick)         
        
        
        self.button =wx.Button(self, 250, "READ LIST TXT", wx.Point(322,125))#import files
        
        wx.EVT_BUTTON(self, 250, self.OnClick)           

        self.button =wx.Button(self, 260, "COMBINE ALL", wx.Point(418,125))#import files
        wx.EVT_BUTTON(self, 260, self.OnClick) 
        
        
        self.button =wx.Button(self, 8, "EXIT", wx.Point(260, 379))
        wx.EVT_BUTTON(self, 8, self.OnExit)

        ##------------ LElab_logo
        imageFile = 'logo_lab.png'
        im1 = Image.open(imageFile)
        jpg1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, jpg1, (348,270), (jpg1.GetWidth(), jpg1.GetHeight()), style=wx.SUNKEN_BORDER)
        
        
        # the edit control - one line version.
        self.lblname = wx.StaticText(self, -1, "Cost Map:",wx.Point(20,58))
        self.lblname2 = wx.StaticText(self, -1, "Target Source:",wx.Point(155,60))
        self.lblname2 = wx.StaticText(self, -1, "Variability:",wx.Point(400,60))
        self.lblname = wx.StaticText(self, -1, "Use existing map:",wx.Point(20,100))
        self.lblname = wx.StaticText(self, -1, "M1:",wx.Point(20,190))
        self.lblname = wx.StaticText(self, -1, "M2:",wx.Point(70,190))
        self.lblname = wx.StaticText(self, -1, "M3:",wx.Point(120,190))
        self.lblname = wx.StaticText(self, -1, "M4:",wx.Point(170,190))
        #self.lblname = wx.StaticText(self, -1, "M5:",wx.Point(220,190))
        #self.lblname = wx.StaticText(self, -1, "M6:",wx.Point(270,190))
        self.lblname = wx.StaticText(self, -1, "Name Output corridor:",wx.Point(20,160))
        self.lblname = wx.StaticText(self, -1, "Scale unit (M) :",wx.Point(330,160))
        self.editname = wx.TextCtrl(self, 180, Form1.edtstart_list, wx.Point(126,126), wx.Size(195,-1))
        
        self.editname = wx.TextCtrl(self, 185, 'Proposed name of the cost map', wx.Point(130,155), wx.Size(195,-1))
        self.editname = wx.TextCtrl(self, 186, '2.0', wx.Point(455,55), wx.Size(30,-1))
        self.editname = wx.TextCtrl(self, 265, Form1.edtCost, wx.Point(110,97), wx.Size(195,-1))
        self.editname = wx.TextCtrl(self, 266, Form1.edtST, wx.Point(308,97), wx.Size(195,-1))
        self.editname = wx.TextCtrl(self, 190, Form1.NsimulationsStart, wx.Point(40,187), wx.Size(25,-1))
        self.editname = wx.TextCtrl(self, 191, Form1.NsimulationsStart, wx.Point(90,187), wx.Size(25,-1))
        self.editname = wx.TextCtrl(self, 192, Form1.NsimulationsStart, wx.Point(140,187), wx.Size(25,-1))
        self.editname = wx.TextCtrl(self, 193, Form1.NsimulationsStart, wx.Point(190,187), wx.Size(25,-1))
        #self.editname = wx.TextCtrl(self, 194, Form1.NsimulationsStart, wx.Point(240,187), wx.Size(25,-1))
        #self.editname = wx.TextCtrl(self, 195, Form1.NsimulationsStart, wx.Point(290,187), wx.Size(25,-1))
        self.editname = wx.TextCtrl(self, 196, Form1.startscale, wx.Point(405,155), wx.Size(50,-1))
                
       
        
        wx.EVT_TEXT(self, 180, self.EvtText)
       
        wx.EVT_TEXT(self, 185, self.EvtText)
        wx.EVT_TEXT(self, 186, self.EvtText)
        wx.EVT_TEXT(self, 190, self.EvtText)
        wx.EVT_TEXT(self, 191, self.EvtText)
        wx.EVT_TEXT(self, 192, self.EvtText)
        wx.EVT_TEXT(self, 193, self.EvtText)
        wx.EVT_TEXT(self, 194, self.EvtText)
        wx.EVT_TEXT(self, 195, self.EvtText)
        wx.EVT_TEXT(self, 196, self.EvtText)
        wx.EVT_TEXT(self, 265, self.EvtText)
        wx.EVT_TEXT(self, 266, self.EvtText)
        #wx.EVT_CHAR(self.editname, self.EvtChar)
        

        Form1.lista = wx.StaticText(self, -1, "Enter a list manually :",wx.Point(20,130)) #lista
        #Form1.edtstart_list = wx.TextCtrl(self, 30, str(Form1.lista ), wx.Point(90, 120), wx.Size(35,-1))
        #wx.EVT_TEXT(self, 30, self.EvtText)
        #wx.EVT_CHAR(Form1.edtstart_popsize, self.EvtChar)
        
        
        # the combobox Control

        #self.lblspeciesList = wx.StaticText(self,-1,"Species Profile:",wx.Point(20, 150))
        #self.editspeciesList=wx.ComboBox(self, 93, Form1.species_profile, wx.Point(100, 150), wx.Size(120, -1),
        #self.speciesList, wx.CB_DROPDOWN)
        #wx.EVT_COMBOBOX(self, 93, self.EvtComboBox)
        #wx.EVT_TEXT(self, 93, self.EvtText)
        
        # Checkbox

        #self.insure = wx.CheckBox(self, 94, "Plot movements",wx.Point(10,180))
        #wx.EVT_CHECKBOX(self, 94,   self.EvtCheckBox)

       # self.insure = wx.CheckBox(self, 95, "Prob.Death",wx.Point(260,180))
       # wx.EVT_CHECKBOX(self, 95,   self.EvtCheckBox)        
        
        # Radio Boxes
        self.dispersiveList = ['1', '2', '3',         ]
        #rb = wx.RadioBox(self, 92, "chose form list", wx.Point(20, 210), wx.DefaultSize,
        #                self.dispersiveList, 2, wx.RA_SPECIFY_COLS)
       # wx.EVT_RADIOBOX(self, 92, self.EvtRadioBox)


    def EvtRadioBox(self, event):
        a='7iuoui'
        self.logger.AppendText('Dispersive behaviour: %s\n' % a)
        
    def EvtComboBox(self, event):
        if event.GetId()==93:   #93==Species Profile Combo box
            Form1.species_profile=event.GetString()
            self.logger.AppendText('Species Profile: %s\n' % event.GetString())
        else:
            self.logger.AppendText('EvtComboBox: NEED TO BE SPECIFYED' )
        
        
       
    def OnClick(self,event):
        #self.logger.AppendText(" Runing simulation %d\n" )#%event.GetId())
        
        
        if event.GetId()==240: #Run import
          grass.run_command ('r.in.gdal', flags='o' ,input=Form1.InArqCost,output=Form1.OutArqCost,overwrite=True, verbose = False)
          grass.run_command ('r.in.gdal', flags='o' ,input=Form1.InArqST,output= Form1.OutArqST,overwrite=True, verbose = False)
          grass.run_command('g.region', rast=Form1.OutArqCost,verbose=False)
          self.logger.AppendText('importing rasters... \n')
       
        if event.GetId()==260: #comnine list
          self.logger.AppendText('generating combinations... \n')
          Form1.patch_id_list_aux=combine_st(patchid_list=Form1.OutArqST)
          Form1.patch_id_list_aux_b=Form1.patch_id_list_aux.split(',')
          Form1.lenlist=len(Form1.patch_id_list_aux_b)
          Form1.lenlist_b=Form1.lenlist/2
          #print Form1.lenlist
          
        
          self.logger.AppendText('waiting ... \n')
          d= wx.MessageDialog( self, `Form1.lenlist_b`+" Combitarions simulate ? \n","", wx.YES_NO)
                            # Create a message dialog box
          retCode=d.ShowModal() # Shows 
           # finally destroy it when finished.
          d.Close(True)  # Close the frame. 

          if (retCode == wx.ID_YES):
            Form1.patch_id_list=Form1.patch_id_list_aux.split(',')
            self.logger.AppendText('\n created list \n')
            #print Form1.patch_id_list
            
              
          else:
              print ""
              self.logger.AppendText('not accepted \n')
          d.Destroy()

        
         
        
          
        #if event.GetId()==200:   #200==Select directori
        #  Form1.OutDir_files=selecdirectori()
        #  print Form1.OutDir_files
          
          
        if event.GetId()==205:   #200==Select directori
          self.logger.AppendText('Please select the directory... \n')
        
          p=grass.mlist_grouped ('rast', pattern='*MSP*') ['PERMANENT']
          j=len(p)
          #print j
          self.logger.AppendText('Foud: '+`j`)
          d= wx.MessageDialog( self, `j`+" Files \n Export files?  \n"
                               ,"", wx.YES_NO)
          # Create a message dialog box
          retCode=d.ShowModal() # Shows 
          # finally destroy it when finished.
          d.Close(True)  # Close the frame. 
          
          if (retCode == wx.ID_YES):
            Form1.OutDir_files=selecdirectori()
            os.chdir(Form1.OutDir_files)
            for i in p:
              grass.run_command('g.region', rast=i,verbose=False)
              grass.run_command('r.out.gdal',input=i, out=i+'.tif',format='GTiff',nodata=-9999)
              #print i
              self.logger.AppendText('Exporting:\n '+i +"\n" )
            else:
              #print "no"
              self.logger.AppendText('Export canceled \n' )
              d.Destroy()   
                    
                    

                                                
                    
        if event.GetId()==210:   #210==Select files st
          self.logger.AppendText("Waiting ... :\n")
          Form1.InArqST=selecdirectori()
          Form1.OutArqST=Form1.InArqST.split('\\');Form1.OutArqST=Form1.OutArqST[-1].replace('.','_')
          print   Form1.OutArqST
          self.logger.AppendText('Selected File: \n '+Form1.OutArqST)
         
          
                  
        if event.GetId()==230:   #230==Select files cost
          self.logger.AppendText("Waiting ... :\n")
          Form1.InArqCost=selecdirectori()
          print Form1.InArqCost 
          Form1.OutArqCost=Form1.InArqCost.split('\\');Form1.OutArqCost=Form1.OutArqCost[-1].replace('.','_')
          print Form1.OutArqCost
          self.logger.AppendText('Selected File: \n'+Form1.OutArqCost)
          Form1.OutArqCost
          Form1.NEXPER_FINAL=Form1.OutArqCost+'_'+Form1.NEXPER_AUX
          
        if event.GetId()==250:
          self.logger.AppendText("Waiting ... :\n")
          Form1.readtxt=selecdirectori()
          Form1.fileHandle = open (Form1.readtxt, 'r' )
          Form1.patch_id_list=Form1.fileHandle.read() 
          Form1.patch_id_list_aux_b=Form1.patch_id_list.split(',')
          print Form1.patch_id_list_aux_b
          self.logger.AppendText("TXT Combinations \n"+`Form1.patch_id_list_aux_b`)
          
      

        if event.GetId()==10:   #10==START
          
         
          
          self.logger.AppendText("Checking the list \n")
          Form1.lenlist=len(Form1.patch_id_list_aux_b)
         
          
          if  Form1.lenlist <= 1: 
            d= wx.MessageDialog( self, " Incorrect list \n"
                                             ,"", wx.OK)
            # Create a message dialog box
            d.ShowModal() # Shows it
            d.Destroy() # finally destroy it when finished.
            #frame.Close(True)  # Close the frame. 
            self.logger.AppendText(" Check list.. \n")
            
          elif Form1.lenlist > 1 and int (Form1.lenlist)%2 ==1 :
            
            d= wx.MessageDialog( self, "incorrect list \n Numbers odd patch, check the list \n  "
                                 ,"", wx.OK)
            # Create a message dialog box
            d.ShowModal() # Shows it
            d.Destroy() # finally destroy it when finished.
              #frame.Close(True)  # Close the frame. 
          else:
            Form1.patch_id_list=Form1.patch_id_list_aux.split(',')
            self.logger.AppendText(" ok list \n")
            self.logger.AppendText(" waiting... \n")
            
           
            
           
            d= wx.MessageDialog( self, " Select the output folder for'\n' text files \n"
                               ,"", wx.OK)
            # Create a message dialog box
            d.ShowModal() # Shows it
            d.Destroy() # finally destroy it when finished.
            Form1.OutDir_files_TXT=selecdirectori()
            self.logger.AppendText(" Selected output folder: \n"+Form1.OutDir_files_TXT)
            
          
            self.logger.AppendText(" running...: \n")
          self.logger.AppendText("\n creating list: \n"+`Form1.patch_id_list_aux_b`+'\n')   
          Form1.S1=""
          Form1.T1=""
          Form1.C2=Form1.C2+''
          Form1.C3=Form1.C3+''
          Form1.C4=Form1.C4+''
          
          
          
          Form1.res=grass.read_command('g.region',flags='m')
          Form1.res2=Form1.res.split('\n')
          Form1.res3=Form1.res2[5]
          Form1.res3=float(Form1.res3.replace('ewres=',''))
          Form1.escfina1=(Form1.esc*2)/Form1.res3
          
          if Form1.escfina1%2==0:
            Form1.escfina1=int(Form1.escfina1)
            Form1.escfina1=Form1.escfina1+1
          else:
            Form1.escfina1=int(round(Form1.escfina1, ndigits=0))
              
          
          grass.run_command('g.region', rast=Form1.OutArqCost, res=Form1.res3)
          grass.run_command('r.neighbors',input=Form1.OutArqCost,out=Form1.C2, method='mode',size=Form1.escfina1,overwrite = True)
          grass.run_command('r.neighbors',input=Form1.OutArqCost,out=Form1.C3, method='average',size=Form1.escfina1,overwrite = True)
          grass.run_command('r.neighbors',input=Form1.OutArqCost,out=Form1.C4, method='maximum',size=Form1.escfina1,overwrite = True)
          
          
          Form1.escfinal=0
          Form1.escapoio1=grass.read_command('g.region',flags='m')
          Form1.escapoio2=Form1.escapoio1.split("\n")
          Form1.escE=Form1.escapoio2[3]
          Form1.escW=Form1.escapoio2[2]
          Form1.escE=float(Form1.escE.replace("e=",''))
          Form1.escW=float(Form1.escW.replace("w=",''))
          Form1.escfinal=(Form1.escE-Form1.escW)/30          
          
          
          
          grass.run_command('g.region', rast=Form1.OutArqCost, res=Form1.escfinal)
          grass.run_command('r.neighbors', input=Form1.OutArqCost,out='apoio1',method='average', size=3,overwrite = True)    
          Form1.form_11='apoio2=apoio1*1.0'
#         print Form1.form_11          
          grass.mapcalc(Form1.form_11, overwrite = True, quiet = True)
          Form1.form_12='apoio2b=0.1+(((apoio2-298.3)/246.4)^2)^0.5'
          grass.mapcalc(Form1.form_12, overwrite = True, quiet = True)
          grass.run_command('g.region', rast=Form1.OutArqCost)
          
          Form1.form_13="apoio2c=apoio2b*"+`Form1.ruido_float`
          grass.mapcalc(Form1.form_13, overwrite = True, quiet = True)
          Form1.form_13="apoio2d="+Form1.OutArqCost+"-apoio2c"
          grass.mapcalc(Form1.form_13, overwrite = True, quiet = True)
          Form1.form_13="M5_AVERAGE_VIEW=((apoio2d)^2)^0.5"
          
          
                
          
          #print Form1.form_13
          grass.mapcalc(Form1.form_13, overwrite = True, quiet = True)
          
          
         
          Form1.listafinal=[]
          
          for i in range(Form1.Nsimulations1):
            Form1.listafinal.append(Form1.OutArqCost)
            Form1.listaApoioaleat3.append('')
          for i in range(Form1.Nsimulations2):
            Form1.listafinal.append(Form1.C2)
            Form1.listaApoioaleat3.append('')
          for i in range(Form1.Nsimulations3):
            Form1.listafinal.append(Form1.C3)
            Form1.listaApoioaleat3.append('')
          for i in range(Form1.Nsimulations4):
            Form1.listafinal.append(Form1.C4)  
            Form1.listaApoioaleat3.append('')
          
            
            
          
            
            
          
          grass.run_command('g.region', rast=Form1.OutArqCost, res=Form1.res3)
          Form1.Nsimulations=Form1.Nsimulations1+Form1.Nsimulations2+Form1.Nsimulations3+Form1.Nsimulations4
          #patch_id_list          
          while (len(Form1.patch_id_list)>1):
            Form1.S1=Form1.patch_id_list[0]
            Form1.T1=Form1.patch_id_list[1]
            Form1.S1FORMAT='000000'+Form1.S1
            Form1.S1FORMAT=Form1.S1FORMAT[-5:]
            Form1.T1FORMAT='000000'+Form1.T1
            Form1.T1FORMAT=Form1.T1FORMAT[-5:]
            #print Form1.S1FORMAT, Form1.T1FORMAT
            #print Form1.S1 , Form1.T1 
            del Form1.patch_id_list[0:2]
            
            Form1.PAISGEM='EXPERIMENTO'
            Form1.ARQSAIDA=Form1.PAISGEM+'_s'+Form1.S1FORMAT+'_t'+Form1.T1FORMAT
              
            self.logger.AppendText(" suing pair: \n"+Form1.S1FORMAT+'&'+Form1.T1FORMAT+ '\n')  
            Form1.S1=(int(str(Form1.S1)))
            Form1.T1=(int(str(Form1.T1)))
            Form1.form_02='source=if('+Form1.OutArqST+'!='+`Form1.S1`+',null(),'+`Form1.S1`+ ')'
            Form1.form_03='target=if('+Form1.OutArqST+'!='+`Form1.T1`+',null(),'+`Form1.T1`+ ')'
            #print Form1.form_02
            os.chdir(Form1.OutDir_files_TXT)
            grass.mapcalc(Form1.form_02, overwrite = True, quiet = True)
            grass.mapcalc(Form1.form_03, overwrite = True, quiet = True)
            
            #grass.run_command('g.mremove',vect='*', flags='f')
            grass.run_command('g.region', rast=Form1.OutArqST,verbose=False)
            
            grass.run_command('r.to.vect', input='source', out='source_shp', feature='area',verbose=False, overwrite = True ) 
            grass.run_command('r.to.vect', input='target', out='target_shp', feature='area',verbose=False, overwrite = True ) 
            grass.run_command ('v.db.addcol', map='source_shp', columns='x double precision,y double precision', overwrite = True)
            grass.run_command ('v.db.addcol', map='target_shp', columns='x double precision,y double precision', overwrite = True)
            
            grass.read_command ('v.to.db', map='source_shp', option='coor', columns="x,y", overwrite = True)
            grass.read_command ('v.to.db', map='target_shp', option='coor', columns="x,y", overwrite = True)
            
            Form1.a='' 
            Form1.a=grass.read_command('v.db.select', map='source_shp', flags='c',overwrite = True);
            Form1.var_source_x= Form1.a.split('|');
            Form1.var_source_x_b=str( Form1.var_source_x[3]); 
            Form1.var_source_x_b=Form1.var_source_x_b.replace('\n','')
            
            Form1.b=''
            Form1.b=grass.read_command('v.db.select', map='source_shp', flags='c',overwrite = True);
            Form1.var_source_y= Form1.b.split('|');
            Form1.var_source_y_b=str(Form1.var_source_y[4]);
            Form1.var_source_y_b=Form1.var_source_y_b.replace('\n','')
           
            Form1.c=''
            Form1.c=grass.read_command('v.db.select', map='target_shp', flags='c',overwrite = True)
            Form1.var_target_x= Form1.c.split('|')
            Form1.var_target_x_b=str(Form1.var_target_x[3])
            Form1.var_target_x_b=Form1.var_target_x_b.replace('\n','')
           
            Form1.d=''
            Form1.d=grass.read_command('v.db.select', map='target_shp', flags='c',overwrite = True)
            Form1.var_target_y= Form1.d.split('|')
            Form1.var_target_y_b=str( Form1.var_target_y[4])
            
            #print Form1.d
            #print Form1.var_target_y
            #print Form1.var_target_y_b
            Form1.var_target_y_b=Form1.var_target_y_b.replace('\n','')
            
            grass.run_command('g.region', rast=Form1.OutArqCost,verbose=False)
            
            
           
            Form1.mapa_corredores="corredores_s"+Form1.S1FORMAT+"_t"+Form1.T1FORMAT+'_COM0'
            Form1.mapa_corredores_sem0=Form1.NEXPER_FINAL+'_'+'S_'+Form1.S1FORMAT+"_T_"+Form1.T1FORMAT
            Form1.chekfolder=os.path.exists('Line_'+Form1.mapa_corredores_sem0)
            
            if Form1.chekfolder==False:
              os.mkdir('Line_'+Form1.mapa_corredores_sem0)
              Form1.outdir=Form1.OutDir_files_TXT+'\Line_'+Form1.mapa_corredores_sem0
            else:
              d= wx.MessageDialog( self, " Existing folder please select another location to save the lines \n"
                                   ,"", wx.OK)
              # Create a message dialog box
              d.ShowModal() # Shows it
              d.Destroy()              
              Form1.outdir=selecdirectori()            
            Form1.form_04='mapa_corredores=0'
            grass.mapcalc(Form1.form_04, overwrite = True, quiet = True)
            Form1.form_16='corredores_aux=0'
            grass.mapcalc(Form1.form_16, overwrite = True, quiet = True)
                            
            
              
              
              
            Form1.arquivo = open(Form1.mapa_corredores_sem0+'.txt','w')
            Form1.cabecalho='EXPERIMENT'','+'M'+','+'SIMULATION'+','+'LENGTHVECT'+','+'COST'+','+'Coord_source_x'+','+'Coord_source_y'+','+'Coord_target_x'+','+'Coord_target_y'+','+'Euclidean_Distance' '\n'
            Form1.arquivo.write(Form1.cabecalho)
            
            cont=0
            for i in range(Form1.Nsimulations):
              Form1.form_08='mapa_custo='+Form1.listafinal[cont]
              grass.mapcalc(Form1.form_08, overwrite = True, quiet = True)              
                       
              c=i+1
              
              
              #y=x/2
              print "------------------------------------------------------------------"
              print "=====> rodando : ",`c` 
              self.logger.AppendText('=======> runing :'+`c`+ '\n' )
              grass.run_command('r.mask',input='source')
              grass.run_command('g.region', vect='source_shp',verbose=False,overwrite = True)
              grass.run_command('v.random', output='temp_point1_s',n=30,overwrite = True)
              grass.run_command('v.select',ainput='temp_point1_s',binput='source_shp',output='temp_point2_s',operator='overlap',overwrite = True)
              grass.run_command('v.db.addtable', map='temp_point2_s',columns="temp double precision")
              grass.run_command('v.db.connect',flags='p',map='temp_point2_s')
              Form1.frag=grass.read_command('v.db.select',map='temp_point2_s',column='cat')
              Form1.frag_list=Form1.frag.split('\n')
              Form1.frag_list2=int(Form1.frag_list[1])              
              Form1.selct="cat="+`Form1.frag_list2`
              grass.run_command('v.extract',input='temp_point2_s',output='pnts_aleat_S',where=Form1.selct,overwrite = True)
              grass.run_command('r.mask',flags='r')
              
              
              grass.run_command('r.mask',input='target')
              grass.run_command('g.region', vect='target_shp',verbose=False,overwrite = True)
              
              grass.run_command('v.random', output='temp_point1_t',n=30,overwrite = True)
              grass.run_command('v.select',ainput='temp_point1_t',binput='target_shp',output='temp_point2_t',operator='overlap',overwrite = True)
              grass.run_command('v.db.addtable', map='temp_point2_t',columns="temp double precision")
              grass.run_command('v.db.connect',flags='p',map='temp_point2_t')
            
              Form1.frag=grass.read_command('v.db.select',map='temp_point2_t',column='cat')
              Form1.frag_list=Form1.frag.split('\n')
              Form1.frag_list2=int(Form1.frag_list[1])              
              Form1.selct="cat="+`Form1.frag_list2`
              grass.run_command('v.extract',input='temp_point2_t',output='pnts_aleat_T',where=Form1.selct,overwrite = True)            
            
            
              
              grass.run_command('r.mask',flags='r')
                
              grass.run_command('g.region', rast=Form1.OutArqCost,verbose=False)
              Form1.form_05='corredores_aux=mapa_corredores'
                
              grass.mapcalc(Form1.form_05, overwrite = True, quiet = True)
              if Form1.listaApoioaleat3[i]=='M6_Unikon' :
                
               
                grass.run_command('r.random.surface', out='aleat', high=100,overwrite = True)
                Form1.form_06='aleat2=1+((aleat/100.0)*'+`Form1.ruido_float`+')'
                grass.mapcalc(Form1.form_06, overwrite = True, quiet = True)
                Form1.form_07='custo_aux=mapa_custo*aleat2'  
                grass.run_command('g.region', rast='source,target',res=Form1.escfinal,verbose=False)
                grass.run_command('r.random.surface', out='aleat_Gros', high=100,overwrite = True)
                Form1.form_15='aleat2_Gros=1+((aleat_Gros/100.0)*'+`Form1.ruido_float`+')'
                grass.mapcalc(Form1.form_15, overwrite = True, quiet = True)
                grass.run_command('g.region', rast='source,target',verbose=False)
                
                Form1.form_16='custo_aux=mapa_custo*aleat2*aleat2_Gros'  
                grass.mapcalc(Form1.form_16, overwrite = True, quiet = True) 
                Form1.form_18='M6=mapa_custo*aleat2*aleat2_Gros'  
                grass.mapcalc(Form1.form_18, overwrite = True, quiet = True)                   
                
              else :  

                  grass.run_command('r.random.surface', out='aleat', high=100,overwrite = True)
                  Form1.form_06='aleat2=1+((aleat/100.0)*'+`Form1.ruido_float`+')'
                  grass.mapcalc(Form1.form_06, overwrite = True, quiet = True)
                  Form1.form_07='custo_aux=mapa_custo*aleat2'
                  grass.mapcalc(Form1.form_07, overwrite = True, quiet = True)    
              
              
              
             
                
              grass.run_command('g.region', rast=Form1.OutArqCost,verbose=False) 
              grass.run_command('r.cost', flags='k', input='custo_aux', out='custo_aux_cost', start_points='pnts_aleat_S', stop_points='pnts_aleat_T',overwrite = True)
              grass.run_command('r.drain', input='custo_aux_cost', out='custo_aux_cost_drain', vector_points='pnts_aleat_T', overwrite = True)
              grass.run_command('r.series',input='corredores_aux,custo_aux_cost_drain', output='mapa_corredores', method='sum',overwrite = True)
              Form1.form_09='custo_aux_cost_drain_sum=custo_aux_cost_drain*'+Form1.listafinal[0]
              
              grass.mapcalc(Form1.form_09, overwrite = True, quiet = True)  
             
              
              #calculando custo
              Form1.x=grass.read_command('r.univar', map='custo_aux_cost_drain_sum')
              #print Form1.x
              Form1.x_b=Form1.x.split('\n')
              #Form1.x_b=Form1.x.repleace('\n',',')
              #print Form1.x_b
              Form1.x_c=str(Form1.x_b[14])
              Form1.var_cost_sum=Form1.x_c[5:8]
              
                           
              
              
              
              #print 
              grass.run_command('g.region', rast=Form1.OutArqCost,verbose=False)
              Form1.form_10=Form1.mapa_corredores_sem0+'=if(mapa_corredores==0,null(),mapa_corredores)' 
              
              
                  
                  
                  
              grass.mapcalc(Form1.form_10, overwrite = True, quiet = True)
             #calculando a distancia
              Form1.length=grass.read_command('r.univar', map='custo_aux_cost_drain')
              #print Form1.x
              Form1.length_b=Form1.length.split('\n')
              Form1.length_c=str(Form1.length_b[14])
              Form1.length_d=Form1.length_c[5:9]
              Form1.length_e=float(Form1.length_d)
              Form1.var_dist_line=Form1.res3*Form1.length_e
              
              Form1.var_source_x_b_int=float(Form1.var_source_x_b)
              Form1.var_source_y_b_int=float(Form1.var_source_y_b)
              Form1.var_target_x_b_int=float(Form1.var_target_x_b)
              Form1.var_target_y_b_int=float(Form1.var_target_y_b)
             
              
              Form1.euclidean_a =float((Form1.var_source_x_b_int-Form1.var_target_x_b_int)**2 + (Form1.var_source_y_b_int-Form1.var_target_y_b_int)**2)
              Form1.euclidean_b= Form1.euclidean_a**0.5
              if Form1.listafinal[cont]==Form1.OutArqCost:
                Form1.M="M1"
              if Form1.listafinal[cont]=='M2_MODE':
                Form1.M="M2"
              if Form1.listafinal[cont]=='M3_MAXIMUM':
                Form1.M="M3"              
              if Form1.listafinal[cont]=='M4_AVERAGE':
                Form1.M="M4"              
              if Form1.listafinal[cont]=='M5_AVERAGE_VIEW':
                Form1.M="M5"                
              if Form1.listafinal[cont]=='M6_Unikon':
                Form1.M="M6"                
                   
                              
              
              
              
              
              
              Form1.linha=Form1.listafinal[cont].replace("@PERMANENT",'')+','+Form1.M+','+`c`+','+ `Form1.var_dist_line`+','+ `Form1.var_cost_sum`+','+ `Form1.var_source_x_b`+','+ `Form1.var_source_y_b`+','+ `Form1.var_target_x_b`+','+ `Form1.var_target_y_b`+','+ `Form1.euclidean_b`+ "\n"
              Form1.linha=Form1.linha.replace('\'','')
              #PAISGEM+var_dist_line ` `+var_cost_sum+` `+var_source_x+` `+var_source_y+` `+var_target_x+` ` var_target_y`
              Form1.var_dist_line=0.0
              Form1.var_cost_sum=0.0
              #linha=$ARQSAIDA$" simulacao="$i$" lengthvect="$var_dist_line$"  somarast="$var_cost_sum$" source_x="$var_source_x$" source_y="$var_source_y$" target_x="$var_target_x$" target_y="$var_target_y   
              
              #print Form1.linha
              Form1.arquivo.write(Form1.linha)
              Form1.linha=""
              print "MAP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"+Form1.listafinal[cont]
              #declarar isso 
              Form1.outline1='000000'+`c`
              #Form1.outline='000000'+`i`
              Form1.outline1=Form1.outline1[-3:]
              Form1.outline1=Form1.mapa_corredores_sem0+"_"+Form1.M+"_"+"_SM_"+Form1.outline1
              
              grass.run_command('r.to.vect', input='custo_aux_cost_drain', out=Form1.outline1, feature='line',verbose=False, overwrite = True )
              grass.run_command ('v.db.addcol', map=Form1.outline1, columns='dist double precision', overwrite = True)
              grass.read_command ('v.to.db', map=Form1.outline1, option='length', type='line', col='dist', units='me', overwrite = True)
              os.chdir(Form1.outdir)
              grass.run_command('v.out.ogr', input=Form1.outline1,dsn=Form1.outline1+'.shp',verbose=False,type='line')              
              grass.run_command('g.remove',vect=Form1.outline1, flags='f')              
              cont=cont+1
              
              
             
            Form1.listExport.append(Form1.mapa_corredores_sem0)  
            self.logger.AppendText(" removing auxiliary files...: \n")  
            grass.run_command('g.remove',vect='temp_point1_s,temp_point2_s,temp_point1_t,temp_point2_t,pnts_aleat_S,pnts_aleat_T,source_shp,target_shp,custo_aux_cost_drain_sem0_line', flags='f')
            grass.run_command('g.remove',rast='mapa_custo,mapa_corredores,custo_aux_cost_drain,source,target,custo_aux_cost_drain_sum,custo_aux_cost_drain_sem0,custo_aux_cost,custo_aux,corredores_aux,aleat,aleat2,aleat2_Gros,aleat3,aleat_Gros,apoio1', flags='f')
            grass.run_command('g.remove',rast='apoio2,apoio2b,apoio2c,apoio2d', flags='f')
            Form1.arquivo.close()
            grass.run_command('g.region', rast=Form1.OutArqCost,verbose=False)
            
            p=grass.mlist_grouped ('rast', pattern='*MSP*') ['PERMANENT']
          
          
          j=len(Form1.listExport)
          #print j
          self.logger.AppendText(" waiting ...: \n")  
          d= wx.MessageDialog( self, `j`+" Files \n successful! \n want to export the files??  \n"
                               ,"", wx.YES_NO)
          # Create a message dialog box
          retCode=d.ShowModal() # Shows 
          # finally destroy it when finished.
          d.Close(True)  # Close the frame. 
            
          if (retCode == wx.ID_YES):
            Form1.OutDir_files=selecdirectori()
            os.chdir(Form1.OutDir_files)
            self.logger.AppendText(" exporting all files ... \n") 
            for i in Form1.listExport:
              grass.run_command('r.out.gdal',input=i, out=i+'.tif',format='GTiff',nodata=-9999)
              #print i
              
                
          else:
            #print "no"
            self.logger.AppendText(" finalized \n") 
            d.Destroy()
                
       
        
          
          
                
            
        
      
        
        
     
          
                

                    
    def EvtText(self, event):
        #self.logger.AppendText('EvtText: %s\n' % event.GetString())

            
        if event.GetId()==180: #180=lista
          Form1.patch_id_list_aux=event.GetString()
          Form1.patch_id_list_aux_b=Form1.patch_id_list_aux.split(',')
          
              
          
          #print Form1.patch_id_list_aux_b
        if event.GetId()==186: #180=base name use
          Form1.ruido=event.GetString()
          Form1.ruido_float=float(Form1.ruido)        
        
        if event.GetId()==185: #183base name use
          Form1.NEXPER_APOIO=event.GetString()
          Form1.NEXPER_FINAL=Form1.NEXPER_AUX+"_"+Form1.NEXPER_APOIO
          Form1.NEXPER_FINAL=Form1.NEXPER_FINAL.replace('@PERMANENT','')
          self.logger.AppendText('Excerpt basename \n'+Form1.NEXPER_FINAL+ '\n')
          #print Form1.NEXPER_FINAL
            
        
        if event.GetId()==190: #190=numero de simulacoes
          Form1.Nsimulations1=int(event.GetString())
        if event.GetId()==191: #191=numero de simulacoes
          Form1.Nsimulations2=int(event.GetString())  
        if event.GetId()==192: #192=numero de simulacoes
          Form1.Nsimulations3=int(event.GetString())
        if event.GetId()==193: #193=numero de simulacoes
          Form1.Nsimulations4=int(event.GetString())  
          
        if event.GetId()==194: #193=numero de simulacoes
          Form1.Nsimulations5=int(event.GetString())
        if event.GetId()==195: #194=numero de simulacoes
          Form1.Nsimulations6=int(event.GetString()) 
        if event.GetId()==196: #194=numero de simulacoes
          Form1.esc=int(event.GetString())        
          
          
          
          
        
            
             
                                
          
          
          
          
          
       
         
                    
       
        if event.GetId()==265: #265=cost
          Form1.OutArqCost=event.GetString()
          Form1.NEXPER_APOIO=Form1.OutArqCost
          Form1.NEXPER_FINAL=Form1.OutArqCost+"_"+Form1.NEXPER_AUX
          Form1.NEXPER_FINAL=Form1.NEXPER_FINAL.replace('@PERMANENT','')

        
        if event.GetId()==266: #266=Sts
          Form1.OutArqST=event.GetString()          
          
          #print Form1.OutArqCost
          
          
          
          
          
          
       
      
        if event.GetId()==30: #30=popsize
            Form1.output_prefix=event.GetString()
        if event.GetId()==40: #40=timesteps
            not_int=0
            try: 
                int(event.GetString())
            except ValueError:
                not_int=1
                
            if not_int==1:
                Form1.timesteps=0
            else:
                Form1.timesteps=int(event.GetString())
                
        if event.GetId()==50: #50=numberruns
            not_int=0
            try: 
                int(event.GetString())
            except ValueError:
                not_int=1
                
            if not_int==1:
                Form1.numberruns=0
            else:
                Form1.numberruns=int(event.GetString()) 



                
    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())
        if event.GetId()==91:
            if event.Checked()==1:
                Form1.include_habitatquality="HabitatQuality_YES"
            else:
                Form1.include_habitatquality="HabitatQuality_NO"
            self.logger.AppendText('   %s\n' % Form1.include_habitatquality)

        if event.GetId()==94: #Form1.plotmovements
            if int(event.Checked())==1:
                Form1.plotmovements=1
            else:
                Form1.plotmovements=0
            self.logger.AppendText('   Plot momevements: %s\n' % str(Form1.plotmovements))
            
            
    def OnExit(self, event):
        d= wx.MessageDialog( self, " Thanks for simulating \n"
                            " LSCorr V1.0 R.R","Good bye", wx.OK)
                            # Create a message dialog box
        d.ShowModal() # Shows it
        d.Destroy() # finally destroy it when finished.
        frame.Close(True)  # Close the frame. 

#----------------------------------------------------------------------
#......................................................................
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = wx.Frame(None, -1, "LSCorr V1.0 R.R", size=(540,510))
    Form1(frame,-1)
    frame.Show(1)
    
    app.MainLoop()

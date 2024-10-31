from ivisit.widgetdefcollection import *
from ivisit.defdb import *
from ivisit.defdialogs import *
from tkinter import *
from PIL import Image, ImageTk
import threading   # for locks
from supy.forms3 import *


# ******************************************
# class IVisitWidget:
# Abstract base class for IVisit Widgets
# ******************************************
class IVisitWidget:
    def __init__(self,parent_arg,widgetdef_arg,className_arg):   
        # set reference parameters
        self.parent = parent_arg        # reference to the parent widget (typically a IVisitRawDisplayFrame)
        self.widgetdef = widgetdef_arg  # reference to the widget definition (either a ParameterWidgetDef or DataWidgetDef)
        self.className=className_arg    # class name for identifying type of widget
        self.sizeX, self.sizeY = 0,0
        self.flagHide=0                 # if set then hide widget
        self.flagModifiedParVal=1       # will be set (1) if parameter value has been modified (only for parameter widgets)
        self.labelFrame=Frame(self)
        self.labelFrame.pack(side=TOP,fill=X)
        self.labeltext=StringVar()
        self.labeltext.set(self.widgetdef.name)
        #self.label=Label(self.labelFrame,text=self.widgetdef.name)
        self.label=Label(self.labelFrame,textvariable=self.labeltext)    # allow modification of text during simulation
        self.label.bind("<Button-1>",self.onLabelPressed)
        self.label.bind("<B1-Motion>",self.onLabelMoved)
        self.label.bind("<ButtonRelease-1>",self.onLabelReleased)
        self.label.bind("<Button-3>",self.onLabelPressedContext)
        self.labelFrame.bind("<Button-1>",self.onLabelPressed)
        self.labelFrame.bind("<B1-Motion>",self.onLabelMoved)
        self.labelFrame.bind("<ButtonRelease-1>",self.onLabelReleased)
        self.labelFrame.bind("<Button-3>",self.onLabelPressedContext)
        self.labelMoveFlag=0
        #self.labelMoveOldX,labelMoveOldY=self.posX,self.posY

    def updateData(self):   # return (width,height) tuple 
        assert 0, "updateData(self) must be implemented in subclasses of IVisitWidget!"

    def setLabelText(self,txt):
        self.labeltext.set(txt)
        
    def onLabelPressed(self,event):
        if(self.labelMoveFlag==0):
            #print "pressed at", event.x,event.y
            self.labelMoveInitX,self.labelMoveInitY = event.x, event.y
            self.labelMoveFlag=1
            self.lift()
        
    def onLabelMoved(self,event):
        if(self.labelMoveFlag>0):
            self.parent.isModified=True
            self.widgetdef.flagModified=True
            #print "moved to", event.x,event.y
            pos=self.widgetdef.pos    # reference to position list
            deltax, deltay = event.x-self.labelMoveInitX, event.y-self.labelMoveInitY    # relative movement of the mouse
            pos[0],pos[1] = pos[0]+deltax, pos[1]+deltay
            if(pos[0]<0): pos[0]=0
            if(pos[1]<0): pos[1]=0
            self.place(x=pos[0], y=pos[1]) 
            #self.update_idletasks()
        
    def onLabelReleased(self,event):
        if(self.labelMoveFlag>0):
            self.parent.adaptSize()
            #print "released at", event.x,event.y
            self.labelMoveFlag=0
            #deltax, deltay = event.x-self.labelMoveInitX, event.y-self.labelMoveInitY    # relative movement of the mouse
            #self.posX, self.posY = self.posX+deltax, self.posY+deltay
            #self.place(x=self.posX, y=self.posY) 
            
    def onLabelPressedContext(self,event):
        w=Toplevel(self.parent)
        if self.parent: w.transient(self.parent)     # make window transient, e.g., minmize with parent etc.
        w.title("Help")
        l=Label(w,text=self.widgetdef.comment)
        l.pack()
        b=Button(w,text="Close",command=w.destroy)
        b.pack()

    def bind(self,eventType,function2call,obj=None):  # bind function2call to object obj if eventType happens
        print("Warning: Call to abstract bind method of IVisitWidget ", self.widgetdef.name)
        return None
        
# *********************************************************
# class IVisitImageWidget:
# IVisit Image Widget to display 2D matrixese as images 
# *********************************************************

class IVisitImageWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitImageWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        assert isinstance(self.widgetdef,DataWidgetDef), "IVisitImageWidget needs to be initialized with a DataWidgetDef, but self.widgetdef="+str(self.widgetdef.name)+" is not!" 
        assert self.widgetdef.type=='image', "IVisitImageWidget needs to be initialized with a DataWidgetDef having type='image', but actually type="+str(self.widgetdef.type)+" is not valid!" 
        assert self.widgetdef.flagRefData>0, "IVisitImageWidget must be initialized with reference data, but self.widgetdef="+str(self.widgetdef.name)+" has no reference data!"
        self.label.pack(side=LEFT,fill=X)
        self.phim=None
        self.imgcanvas=Canvas(self)
        self.myscale=1.0
        self.mychannel="RGB"
        self.setState()
        self.imgcanvas.pack(side=BOTTOM)
        self.menuLabel=Label(self.labelFrame,text="...")
        self.menuLabel.pack(side=LEFT)
        self.menubar=Menu(self.labelFrame,tearoff=0)
        self.channel_menu = Menu(self.menubar,tearoff=0)
        self.channel_menu.add_command(label="RGB",command=lambda:self.setChannel("RGB"))
        self.channel_menu.add_command(label="Gray" ,command=lambda:self.setChannel("Gray"))
        self.channel_menu.add_command(label="Hue as RGB" ,command=lambda:self.setChannel("Hue"))
        self.channel_menu.add_separator()
        self.channel_menu.add_command(label="Red R" ,command=lambda:self.setChannel("R"))
        self.channel_menu.add_command(label="Green G" ,command=lambda:self.setChannel("G"))
        self.channel_menu.add_command(label="Blue B" ,command=lambda:self.setChannel("B"))
        self.channel_menu.add_separator()
        self.channel_menu.add_command(label="Hue H" ,command=lambda:self.setChannel("H"))
        self.channel_menu.add_command(label="Saturation S" ,command=lambda:self.setChannel("S"))
        self.channel_menu.add_command(label="Value V" ,command=lambda:self.setChannel("V"))
        self.menubar.add_cascade(label="Channels",menu=self.channel_menu)
        self.scale_menu = Menu(self.menubar,tearoff=0)
        self.scale_menu.add_command(label="1x",command=lambda:self.setScale(1.0))
        self.scale_menu.add_separator()
        self.scale_menu.add_command(label="2x",command=lambda:self.setScale(2.0))
        self.scale_menu.add_command(label="4x",command=lambda:self.setScale(4.0))
        self.scale_menu.add_command(label="8x",command=lambda:self.setScale(8.0))
        self.scale_menu.add_separator()
        self.scale_menu.add_command(label="1/2x",command=lambda:self.setScale(0.5))
        self.scale_menu.add_command(label="1/4x",command=lambda:self.setScale(0.25))
        self.scale_menu.add_command(label="1/8x",command=lambda:self.setScale(0.125))
        self.menubar.add_cascade(label="Scale",menu=self.scale_menu)
        self.menubar.add_command(label="Properties",command=self.onProperties)
        self.menubar.add_command(label="Save image",command=self.onSaveImage)
        self.menubar.add_command(label="Hide",command=self.onHide)
        #self.b.pack(side=RIGHT)
        self.menuLabel.bind("<Button-1>", self.popup)
        self.menuLabel.bind("<Button-3>", self.popup)
        if(className=="IVisitImageWidget"): self.updateData()      # derived classes may need further preprocessing before call

    def popup(self,event):
        self.menubar.post(event.x_root, event.y_root)

    def setChannel(self,str_channel):
        self.mychannel=str_channel
        self.updateData()
        
    def setScale(self,sc):
        self.myscale=sc
        self.setState()
        self.updateData()

    def onProperties(self):
        self.widgetdef.setDataFromSimulation()
        updated=editSQLTables(self,self.widgetdef.wdefcoll.db,"Editing of Table 'DataWidget'",tbed_datawidget_cfg,cond_on=[["datawidget.key",self.widgetdef.key]])
        if updated:
            self.widgetdef.wdefcoll.initFromDatabase(self.widgetdef.wdefcoll.simulation_key)
            self.parent.master.updateDisplay()
            
    def onSaveImage(self):
        if not self.phim is None:
            ftypes = [('PNG files' , '.png'),
                      ('JPEG files', '.jpg'),
                      ('TIF files' , '.tif'),
                      ('EPS files' , '.eps'),
                      ('All files' , '*'   )]
            fname = tkinter.filedialog.asksaveasfilename(filetypes=ftypes, defaultextension='.png')
            if not fname is None and fname!="":
                imgpil = ImageTk.getimage(self.phim)
                if imgpil.mode in ("RGBA", "P") and fname.split(".")[-1] in ['jpg','JPG','eps','EPS']:
                    imgpil=imgpil.convert("RGB")
                imgpil.save(fname) 
                imgpil.close()    

    def onHide(self):
        self.flagHide=1-self.flagHide

    def setState(self):        # set object fields that are derived from widget and data definitions
        self.shape=np.array(self.widgetdef.data).shape
        assert len(self.shape)>=2, "IVisitImageWidget '"+str(self.widgetdef.name)+"' is of type 'image', but is associatied to a dataarray '" + str(self.widgetdef.name_dataarray) + "' with less than 2 dimensions!" 
        self.RGBflag=0         # default a 2D gray scale array
        if len(self.shape)>=3: self.RGBflag=1    # 3D RGB array?
        self.NY, self.NX = self.shape[0],self.shape[1]
        myscale=self.widgetdef.scale*self.myscale
        self.CX, self.CY = int(myscale*self.NX), int(myscale*self.NY)
        self.SZ          = self.CX * self.CY
        if self.flagHide<=0: self.imgcanvas.configure(width=self.CX,height=self.CY)
        else: self.imgcanvas.configure(width=1,height=1)
        self.sizeX, self.sizeY = max(self.imgcanvas.winfo_reqwidth(),self.label.winfo_reqwidth()), self.imgcanvas.winfo_reqheight()+self.label.winfo_reqheight()


    def updateData(self):
        # (i) convert image?
        if self.RGBflag>0:
            if self.mychannel=="Gray":
                self.im=self.im.convert("L")
                self.label.configure(text=self.widgetdef.name+" (Gray)")
            elif self.mychannel=="R":
                self.im=Image.fromarray(np.array(self.widgetdef.data[:,:,0],dtype=np.uint8))
                self.label.configure(text=self.widgetdef.name+" (R)")
            elif self.mychannel=="G":
                self.im=Image.fromarray(np.array(self.widgetdef.data[:,:,1],dtype=np.uint8))
                self.label.configure(text=self.widgetdef.name+" (G)")
            elif self.mychannel=="B":
                self.im=Image.fromarray(np.array(self.widgetdef.data[:,:,2],dtype=np.uint8))
                self.label.configure(text=self.widgetdef.name+" (B)")
            elif self.mychannel=="H":
                self.im=Image.fromarray(np.array(self.widgetdef.data,dtype=np.uint8))
                self.im=self.im.convert("HSV")
                im=np.array(self.im.getdata(),dtype=np.uint8).reshape(self.widgetdef.data.shape)
                self.im=Image.fromarray(im[:,:,0])
                self.label.configure(text=self.widgetdef.name+" (H)")
            elif self.mychannel=="S":
                self.im=Image.fromarray(np.array(self.widgetdef.data,dtype=np.uint8))
                self.im=self.im.convert("HSV")
                im=np.array(self.im.getdata(),dtype=np.uint8).reshape(self.widgetdef.data.shape)
                self.im=Image.fromarray(im[:,:,1])
                self.label.configure(text=self.widgetdef.name+" (S)")
            elif self.mychannel=="V":
                self.im=Image.fromarray(np.array(self.widgetdef.data,dtype=np.uint8))
                self.im=self.im.convert("HSV")
                im=np.array(self.im.getdata(),dtype=np.uint8).reshape(self.widgetdef.data.shape)
                self.im=Image.fromarray(im[:,:,2])
                self.label.configure(text=self.widgetdef.name+" (V)")
            elif self.mychannel=="Hue":
                self.im=Image.fromarray(np.array(self.widgetdef.data,dtype=np.uint8))
                self.im=self.im.convert("HSV")
                im=np.array(self.im.getdata(),dtype=np.uint8)
                im=im.reshape(self.widgetdef.data.shape)
                print("im.shape=",im.shape)
                im[:,:,1]=255
                im[:,:,2]=255
                self.im=Image.fromarray(im,mode='HSV')
                self.label.configure(text=self.widgetdef.name+" (HSV-Hue)")
            else:
                self.im=Image.fromarray(np.array(self.widgetdef.data,dtype=np.uint8))  # default
                self.label.configure(text=self.widgetdef.name)
        else:
            self.im=Image.fromarray(np.array(self.widgetdef.data,dtype=np.uint8))      # default
            self.label.configure(text=self.widgetdef.name)
        # (ii) rescale image size?
        myscale=self.widgetdef.scale*self.myscale
        if(myscale!=1.0):
            if(myscale<1.0): self.im=self.im.resize((self.CX,self.CY),Image.ANTIALIAS)
            else: self.im=self.im.resize((self.CX,self.CY),Image.NEAREST)
        # (iii) display image
        self.phim = ImageTk.PhotoImage(self.im)
        self.imgcanvas.delete('all');
        if self.flagHide<=0: self.imgcanvas.create_image(0,0,image=self.phim,anchor=NW)
        self.setState()
        #self.imgcanvas.create_line(0,0,100,100)

    def getWidgetSize(self):   # return (width,height) tuple
        return (self.CX,self.CY)

    def bind(self,eventType,function2call,obj=None):  # use this method to bind a function call to the image canvas (e.g., if clicking on an image pixel)
        if obj==None:
            obj="imgcanvas"
        if obj=="imgcanvas":
            self.imgcanvas.bind(eventType,function2call)
            return self.imgcanvas
        else:
            print("Warning in IVisitImageWidget.bind(): Unknown widget object ", obj, " in IVisitImageWidget", self.widgetdef.name)
            return None
        
# *********************************************************
# class IVisitTextfieldWidget:
# IVisit Image Widget to display text data  
# *********************************************************

class IVisitTextfieldWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitTextfieldWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        assert isinstance(self.widgetdef,DataWidgetDef), "IVisitTextfieldWidget needs to be initialized with a DataWidgetDef, but self.widgetdef="+str(self.widgetdef.name)+" is not!" 
        assert self.widgetdef.type=='textfield', "IVisitTextfieldWidget needs to be initialized with a DataWidgetDef having type='textfield', but actually type="+str(self.widgetdef.type)+" is not valid!" 
        self.label.pack(side=LEFT)
        options=self.widgetdef.range
        str_just="center"
        if 'just_left'  in options: str_just="left"
        if 'just_right' in options: str_just="right"
        self.textlabel=Label(self,text="",justify=str_just)
        self.textlabel.pack(side=RIGHT)
        self.setState()
        if(className=="IVisitTextfieldWidget"): self.updateData()      # derived classes may need further preprocessing before call

    def setState(self):        # set object fields that are derived from widget and data definitions
        self.sizeX, self.sizeY = max(self.label.winfo_reqwidth()+self.textlabel.winfo_reqwidth()+10,self.winfo_reqwidth()), max(self.winfo_reqheight(),self.label.winfo_reqheight(),self.textlabel.winfo_reqheight())

    def updateData(self):
        if self.widgetdef.scale>0:
            self.label.configure(text=str(self.widgetdef.name)+': ')
        else:
            self.label.configure(text="")
        self.textlabel.configure(text=str(self.widgetdef.data))
        self.setState()

    def getWidgetSize(self):   # return (width,height) tuple
        return (self.sizeX,self.sizeY)
       
        
'''
# *******************************************************************
# class PyFeCombiImageWidget:
# PyFelix CombiImage Widget to display 2D population variables plus
# one binary 2D population variable,
# for example, spikes and dendritic potentials
# programmed on September 21, 2012 by Andreas Knoblauch
# *******************************************************************

# color palette for PyFeCombiImageWidget
PyFeCombiImageColorPalette = [item for sublist in ([[i,i,i] for i in range(255)] + [[255,0,0]]) for item in sublist]   

class PyFeCombiImageWidget(PyFeImageWidget):
    def __init__(self,parent,widgetdef_arg,database_arg):
        Frame.__init__(self,master=parent)
        PyFeImageWidget.__init__(self,parent,widgetdef_arg,database_arg,"PyFeCombiImageWidget")
        self.im.putpalette(PyFeCombiImageColorPalette)
        self.updateData()

    def updateData(self):
        #print "call to PyFeInter_getGradualCombiImage"
        self.database.libSim.PyFeInter_getGradualCombiImage(self.data_idx,self.scaleFactor,c_float(self.rangeMin),c_float(self.rangeMax),\
                                                            254,byref(self.imarray))
        self.im.fromstring(self.imarray)
        self.phim = ImageTk.PhotoImage(self.im)
        self.imgcanvas.delete('all');
        self.imgcanvas.create_image(0,0,image=self.phim,anchor=NW)
        #self.imgcanvas.create_line(0,0,100,100)
'''
       
        
# *********************************************************
# class IVisitSliderWidget:
# IVisit Slider Widget to control a simulation parameter
# *********************************************************

class IVisitSliderWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitSliderWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        assert isinstance(self.widgetdef,ParameterWidgetDef), "IVisitSliderWidget needs to be initialized with a ParameterWidgetDef, but self.widgetdef="+str(self.widgetdef.name)+" is not!" 
        assert self.widgetdef.type=='slider', "IVisitSliderWidget needs to be initialized with a ParameterWidgetDef having type='slider', but actually type="+str(self.widgetdef.type)+" is not valid!" 
        assert self.widgetdef.type_parameter=='int' or self.widgetdef.type_parameter=='float', "IVisitSliderWidget needs to be initialized with a numeric parameter type, but actually parameter_type="+str(self.widgetdef.type_parameter)+" is not valid!"
        assert isinstance(self.widgetdef.range,(tuple,list)) and len(self.widgetdef.range)>=4, "IVisitSliderWidget '"+str(self.widgetdef.name)+"' must have attribute range=[min,max,nTicks,scale], but actually range="+str(self.widgetdef.range)+"!"
        self.label.pack(side=LEFT)
        assert(self.widgetdef.range[0]<=self.widgetdef.range[1])and(self.widgetdef.range[3]>=0),"IVisitSliderWidget.__init__: wrong slider range parameters for slider widget " +\
            self.widgetdef.name + "! It must be min<=max and scale>0, whereas range=" + str(self.widgetdef.range) + "! Have a look at range specification in the corresponding " +\
            "parameter definition in the ParameterWidget table! Check format range=[min,max,nTicks,scale] after parameter name!"
        min_,max_,nTicks,scale=self.widgetdef.range[0],self.widgetdef.range[1],int(np.round(self.widgetdef.range[2])),self.widgetdef.range[3]
        if(self.widgetdef.type_parameter=='int'):
            min_,max_,scale = int(np.round(min_)),int(np.round(max_)),int(np.round(scale))
            #print("widget=",self.widgetdef.name,"min,max,scale=",min_,max_,scale)
        # ACHTUNG! BUG IN TKINTER: Man kann Slider nicht für ungerade integer-Werte konfigurieren (nur für gerade)!!!!!!!!!! Stand: Python 3.6 !!!! Vielleicht behoben mit höheren Versionen???
        self.slider=Scale(self,from_=min_,to=max_,command=self.onMove,orient='horizontal',\
                          tickinterval=(max_-min_)/nTicks,resolution=scale,length=int(self.widgetdef.size[0]))
        self.slider.set(self.widgetdef.value)
        self.slider.pack(side=LEFT)
        self.callback_on_sliderupdate=None
        self.onMove(self.widgetdef.value)
        self.setState()

    def setState(self):        # set object fields that are derived from widget and data definitions
        #min=c_double()    # ?????
        self.sizeX, self.sizeY = self.slider.winfo_reqwidth()+self.label.winfo_reqwidth(), self.slider.winfo_reqheight()+self.label.winfo_reqheight()
        #print "slider.sizeX=", self.sizeX, " sizeY=", self.sizeY

    def setValue(self,val):
        self.slider.set(val)

    def reconfigure(self,min=None,max=None,nTicks=None,scale=None):
        if min is None: min=self.widgetdef.range[0]
        if max is None: max=self.widgetdef.range[1]
        if nTicks is None: nTicks=int(np.round(self.widgetdef.range[2]))
        if scale is None: scale=self.widgetdef.range[3]
        if(self.widgetdef.type_parameter=='int'):
            min,max,scale = int(np.round(min)),int(np.round(max)),int(np.round(scale))
        self.slider.configure(from_=min,to=max,tickinterval=(max-min)/nTicks,resolution=scale)
        
    def onMove(self, val):
        #print("onMove...;flag=",flagIgnoreModFlag)
        #assert flagIgnoreModFlag==1
        #if(flagIgnoreModFlag<=0): 
        #    self.parent.isModified=True
        #    self.widgetdef.isModified=True
        newvalue = float(val)     #/self.data.scale
        if self.widgetdef.type_parameter=='int':
           newvalue = int(round(newvalue))
        if(newvalue!=self.widgetdef.value):
            self.parent.isModified=True
            self.flagModifiedParVal=1
        #print("value,newvalue=",self.widgetdef.value, newvalue)
        self.widgetdef.value=newvalue  #  or int(float(val)/self.data.scale+0.5)) ????
        if self.widgetdef.wdefcoll.sim.updateMode!='sync': self.widgetdef.setSimParValue()     # write new parameter value through to simulation (only for updateMode 'async')
        #print "new slider value is ", self.database.libSim.PyFeInter_getSliderValue(self.data_idx)*self.data.scale
        if not self.callback_on_sliderupdate is None: self.callback_on_sliderupdate()

    def getWidgetSize(self):   # return (width,height) tuple
        return (self.sizeX,self.sizeY)
       
    def bind(self,eventType,function2call,obj=None):  # use this method to bind a function call to the slider (e.g., if selecting a new value)
        if obj==None:
            obj="slider"
        if obj=="slider":
            self.callback_on_sliderupdate=function2call
        else:
            print("Warning in IVisitSliderWidget.bind(): Unknown widget object ", obj, " in IVisitSliderWidget", self.widgetdef.name)
        return None
            
# **************************************************************************************
# class IVisitDictSliderWidget:
# IVisit DictSlider Widget to control a dict of several different simulation parameters
# **************************************************************************************

class IVisitDictSliderWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitDictSliderWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        self.widgetdef.ref_to_dictsliderwidget=self   # DIRTY!!! ALLOW widgetdef object to efficiently access values !!!!!!!!! See widgetdefcollection.py; ParameterWidgetDef.setSimParValue(self)
        # (i) check consistency of widgetdef attributes and extract relevant information
        assert isinstance(self.widgetdef,ParameterWidgetDef), "IVisitDictSliderWidget needs to be initialized with a ParameterWidgetDef, but self.widgetdef="+str(self.widgetdef.name)+" is not!" 
        assert self.widgetdef.type=='dictslider', "IVisitDictSliderWidget needs to be initialized with a ParameterWidgetDef having type='dictslider', but actually type="+str(self.widgetdef.type)+" is not valid!"
        wdef=self.widgetdef
        msg_format="IVisitDictSliderWidget: widgetdef.items must have format: [nitems,idxselecteditem,  itemname1,type1,  itemname2,typ2, ...] (length 2+nitems*2)\n"
        msg_format+=" widgetdef.range must have format: [nitems, itemname1,min1,max1,nticks1,scale1, itemname2,min2,max2,nticks2,scale2, ...] (length 1+nitems*5\n"
        msg_format+=" widgetdef.range_parameter must have format: [nitems, key1,type1,min1,max1, key2,type2,min2,max2, ...] (length 1+nitems*4\n"
        assert isinstance(wdef.items,list) and len(wdef.items)>0,"IVisitDictSliderWidget "+str(self.widgetdef.name)+" must have wdef.items being a non-empty list, but wdef.items="+str(wdef.items)+"\n"+msg_format
        assert isinstance(wdef.range,list) and len(wdef.range)>0,"IVisitDictSliderWidget "+str(self.widgetdef.name)+" must have self.parameter being a non-empty list, but self.range="+str(self.range)+"\n"+msg_format
        assert isinstance(wdef.range_parameter,list) and len(wdef.range_parameter)>0,"IVisitDictSliderWidget "+str(self.widgetdef.name)\
            +" must have self.range_parameter being a non-empty list, but self.range_parameter="+str(self.range_parameter)+"\n"+msg_format
        self.nitems=wdef.items[0]         # for format see above
        assert isinstance(self.nitems,int),"wdef.items[0] must be int, but wdef.items="+wdef.items+"\n"+str(msg_format)
        assert len(wdef.items)==2+self.nitems*2,"wdef.items has wrong length!\n"+msg_format+"but wdef.items="+str(wdef.items)
        assert len(wdef.range)==1+self.nitems*5,"wdef.range has wrong length!\n"+msg_format+"but wdef.range="+str(wdef.range) 
        assert len(wdef.range_parameter)==1+self.nitems*4,"wdef.range_parameter has wrong length!\n"+msg_format+"but wdef.range_parameter="+str(wdef.range_parameter)
        self.itemtypes=[wdef.items[3+i*2] for i in range(self.nitems)]   # types of items
        for i in range(self.nitems):
            assert self.itemtypes[i] in ['int','float'],"All item types must be either 'int' or 'float', but self.itemtypes="+str(self.itemtypes)
            ibase=1+i*5
            assert isinstance(wdef.range[ibase],str) and isinstance(wdef.range[ibase+1],(int,float)) and isinstance(wdef.range[ibase+2],(int,float)) \
                and isinstance(wdef.range[ibase+3],int) and isinstance(wdef.range[ibase+4],(int,float)),"wdef.range has wrong types! But wdef.range="+str(wdef_range)+"\n"+msg_format
            assert wdef.range[ibase+1]<wdef.range[ibase+2] and wdef.range[ibase+4]!=0,"wdef.range has wrong mini,maxi,scalei! But wdef.range="+str(wdef_range)+"\n"+msg_format+"\n"+msg_format
            ibasep=1+i*4
            assert wdef.range[ibase+1]<wdef.range[ibase+2],"wdef.range.min < max required!\nBut wdef.range="+str(wdef.range)+"\n"+msg_format
            assert wdef.range_parameter[ibasep+2]<wdef.range_parameter[ibasep+3],"wdef.range_parameter.min < max required!\nBut wdef.range_parameter="+str(wdef.range_parameter)+"\n"+msg_format
        self.sliderranges=[[wdef.range[i*5+2],wdef.range[i*5+3],wdef.range[i*5+4],wdef.range[i*5+5]] for i in range(self.nitems)] # range information for each item for slider widget
        self.itemnames=[wdef.range[1+i*5] for i in range(self.nitems)]                                                            # item names for dict keys (to be displayed in item list of widget)
        self.dict_itemnames={self.itemnames[i]:i for i in range(self.nitems)}                                                     # dict for association itemname --> index
        self.itemkeys=[wdef.range_parameter[1+i*4] for i in range(self.nitems)]                                                   # item keys of dict
        self.values=parseStringAsList(wdef.value,'string',[])                                                                     # current values: first get list of string values
        for i in range(self.nitems):                                                                                              # ...then cast string values as numerical values
            if self.itemtypes[i]=='int': self.values[i]=asNumber(self.values[i],'int',0)                                          # ...either as int
            else: self.values[i]=asNumber(self.values[i],'float',0.0)                                                             # ...or float
        assert isinstance(self.values,list) and len(self.values)==self.nitems,"wdef.value must be string of list of length nitems="+str(self.nitems)+", but wdef.value="+str(wdef.value)
        self.selecteditem=wdef.items[1]                                                                                           # currently selected item
        self.selectedvalue=self.values[self.selecteditem]                                                                         # value of currently selected item
        sz=wdef.size
        self.size_sld,self.columns_text,self.rows_text,self.disp_mode,self.fontsz = 200,20,-1,0,10   # default values for slider size, number of columns in text widget, number of rows, display mode and fontsize
        if isinstance(sz,list):
            if len(sz)>0: self.size_sld=int(sz[0])            # slider size (=width)
            if len(sz)>1: self.columns_text=int(sz[1])        # number of text columns of text widget (for disp_mode=2) 
            if len(sz)>2: self.rows_text=int(sz[2])           # number of text rows of text widget (for disp_mode=2) 
            if len(sz)>3: self.disp_mode=int(sz[3])           # display mode (0=no extra; 1=display parameter values in optionlist entries; 2=extra textfield for parameter values)
            if len(sz)>4: self.fontsz=int(sz[4])              # fontsize for parameter values in textfield (only for disp_mode=2)
        else:
            self.size_sld=int(sz)
        self.itemnames4optionmenu=[s for s in self.itemnames] # default: use simply itemnames for optionmenu
        if self.disp_mode==1:
            self.itemnames4optionmenu=[self.itemnames[i]+": "+str(self.values[i]) for i in range(self.nitems)]   # for dips_mode1 display parameter values in option menu
        #print("IVisitDictSliderWidget",wdef.name)
        #print("   nitems=",self.nitems)
        #print("   itemnames=",self.itemnames)
        #print("   itemkeys=",self.itemkeys)
        #print("   itemtypes=",self.itemtypes)
        #print("   sliderranges=",self.sliderranges)
        #print("   selecteditem=",self.selecteditem)
        #print("   values=",self.values)
        #print("   selectedvalue=",self.selectedvalue)
        #exit(0)
        # (ii) create and initialize widgets
        # (ii.1) do some preparations
        self.label.pack(side=LEFT)
        self.parameterFrame=Frame(self)
        self.parameterFrame.pack(side=BOTTOM,expand=True,fill=BOTH)
        # (ii.2) option menu
        self.itemname_str_var = StringVar()
        self.itemname_str_var.set(str(self.itemnames4optionmenu[self.selecteditem]))
        self.optionmenu = OptionMenu(self.labelFrame,self.itemname_str_var,command=self.onSet,*self.itemnames4optionmenu)
        self.optionmenu.pack(side=LEFT)
        # (ii.3) slider
        rng=self.sliderranges[self.selecteditem]
        min,max,nTicks,scale=rng[0],rng[1],int(np.round(rng[2])),rng[3]
        if(self.itemtypes[self.selecteditem]=='int'):
            min,max,scale = int(np.round(min)),int(np.round(max)),int(np.round(scale))
        self.slider=Scale(self.parameterFrame,from_=min,to=max,command=self.onMove,orient='horizontal',\
                          tickinterval=(max-min)/nTicks,resolution=scale,length=int(self.size_sld))
        self.slider.set(self.values[self.selecteditem])
        self.slider.pack(side=TOP)
        # (ii.4) text widget
        if self.disp_mode==2:
            self.textFrame=Frame(self.parameterFrame)
            self.textFrame.pack(side=BOTTOM,expand=True,fill=BOTH)
            self.text_str_var = StringVar()
            self.text_str_var.set("".join([self.itemnames[i]+": "+str(self.values[i])+"\n" for i in range(self.nitems)])[:-1])
            if self.rows_text<=0: self.rows_text=self.nitems
            self.textinput = SupyTextFrame(self.textFrame, width=self.columns_text,height=self.rows_text, catch_focus=False, textvariable=self.text_str_var)
            self.textinput.text.configure(font=('Arial',self.fontsz))
            self.textinput.pack(side=LEFT)
            self.setbutton=Button(self.textFrame,text='Set',command=self.onSetTextButton)
            self.setbutton.pack(side=RIGHT)

        # (iii) finalize
        self.callback_on_sliderupdate=None
        self.callback_on_optionmenuupdate=None
        self.callback_on_textupdate=None
        self.onMove(self.values[self.selecteditem])
        self.setState()
        self.reconfigureOptionMenu()

    def setState(self):        # set object fields that are derived from widget and data definitions
        #min=c_double()    # ?????
        self.sizeX = max(self.slider.winfo_reqwidth(),self.label.winfo_reqwidth()+self.optionmenu.winfo_reqwidth())
        self.sizeY = max(self.label.winfo_reqheight(),self.optionmenu.winfo_reqheight())+self.slider.winfo_reqheight()
        #print "slider.sizeX=", self.sizeX, " sizeY=", self.sizeY

    def setValue(self,val):
        self.values=[val[i] for i in range(self.nitems)]
        self.selectedvalue=self.values[self.selecteditem]
        self.slider.set(self.selectedvalue)
        #sliderget=self.slider.get()
        #if self.selectedvalue!=sliderget:           # has slider modified value (due to range restrictions)? NO!!!!! THEN let the value be!!! Maybe useful to test parameter values outside the slider range/grid !!??
        #    if self.itemtypes[self.selecteditem]=='int': self.selectedvalue=int(sliderget)
        #    else                                       : self.selectedvalue=float(sliderget)
        #self.values[self.selecteditem]=self.selectedvalue
        #print("...final selectedalue=",self.selectedvalue)
        self.reconfigureOptionMenu()

    def reconfigureSlider(self,min=None,max=None,nTicks=None,scale=None):  
        rng=self.sliderranges[self.selecteditem]
        min,max,nTicks,scale=rng[0],rng[1],int(np.round(rng[2])),rng[3]
        if min is None: min=rng[0]
        if max is None: max=rng[1]
        if nTicks is None: nTicks=int(np.round(rng[2]))
        if scale is None: scale=rng[3]
        if(self.itemtypes[self.selecteditem]=='int'):
            min,max,scale = int(np.round(min)),int(np.round(max)),int(np.round(scale))
        self.slider.configure(from_=min,to=max,tickinterval=(max-min)/nTicks,resolution=scale)

    def reconfigureOptionMenu(self,item_idx=None):
        if item_idx is None:
            item_idx=list(range(self.nitems))
        elif isinstance(item_idx,int):
            item_idx=[item_idx]
        if self.disp_mode==1:
            for i in item_idx:
                self.itemnames4optionmenu[i]=self.itemnames[i]+": "+str(self.values[i])
        else:
            for i in item_idx:
                self.itemnames4optionmenu[i]=self.itemnames[i]
        for i in item_idx: self.optionmenu['menu'].entryconfigure(i, label=self.itemnames4optionmenu[i])
        if self.selecteditem in item_idx: self.itemname_str_var.set(self.itemnames4optionmenu[self.selecteditem])
        
    def onSet(self,e=None):                                      # called by optionmenu if new item is selected
        #print("onMove...;flag=",flagIgnoreModFlag)
        #assert flagIgnoreModFlag==1
        #if(flagIgnoreModFlag<=0): 
        #    self.parent.isModified=True
        #    self.widgetdef.isModified=True
        newitemname = self.itemname_str_var.get().split(':')[0]  # for disp_mode=1 take only part left of (last) ':'
        newitem = self.dict_itemnames[newitemname]               
        if newitem!=self.selecteditem:
            self.parent.isModified=True
            self.selecteditem=newitem
            self.selectedvalue=self.values[newitem]
            self.reconfigureSlider()
            self.slider.set(self.selectedvalue)
        if not self.callback_on_optionmenuupdate is None: self.callback_on_optionmenuupdate()

    def onMove(self, val):                                # called by slider if new value is selected
        #print("onMove...;flag=",flagIgnoreModFlag)
        #assert flagIgnoreModFlag==1
        #if(flagIgnoreModFlag<=0): 
        #    self.parent.isModified=True
        #    self.widgetdef.isModified=True
        newvalue = float(val)     # self.data.scale
        if self.itemtypes[self.selecteditem]=='int':
           newvalue = int(round(newvalue))
        #print("dictslider new value=",newvalue, "selectedvalue=",self.selectedvalue)
        if(newvalue!=self.selectedvalue):
            self.parent.isModified=True
            self.flagModifiedParVal=1
        #print("value,newvalue=",self.widgetdef.value, newvalue)
        self.values[self.selecteditem]=newvalue
        self.selectedvalue=newvalue
        self.widgetdef.value=str(self.values)    #  or int(float(val)/self.data.scale+0.5)) ????
        if self.widgetdef.wdefcoll.sim.updateMode!='sync': self.widgetdef.setSimParValue()     # write new parameter value through to simulation (only for updateMode 'async')
        #print "new slider value is ", self.database.libSim.PyFeInter_getDictSliderValue(self.data_idx)*self.data.scale
        if self.disp_mode==1: self.reconfigureOptionMenu(self.selecteditem)   # update parameter value in option menu (only for disp_mode=1)
        elif self.disp_mode==2: self.textinput.settext("".join([self.itemnames[i]+": "+str(self.values[i])+"\n" for i in range(self.nitems)])[:-1])
        if not self.callback_on_sliderupdate is None: self.callback_on_sliderupdate()

    def onSetTextButton(self):
        txt=self.textinput.gettext()
        txt=txt.split('\n')
        listvalstr=[s.split(':')[-1] for s in txt]
        newvalues=self.values
        for i in range(self.nitems):
            if i<len(listvalstr):
                v=asNumber(listvalstr[i],self.itemtypes[i],None)
                if not v is None: newvalues[i]=v
        self.setValue(newvalues)
        self.parent.isModified=True
        self.flagModifiedParVal=1
        self.widgetdef.value=str(self.values)    
        if self.widgetdef.wdefcoll.sim.updateMode!='sync': self.widgetdef.setSimParValue()     # write new parameter value through to simulation (only for updateMode 'async')
        if self.disp_mode==1: self.reconfigureOptionMenu(self.selecteditem)   # update parameter value in option menu (only for disp_mode=1)
        self.textinput.settext("".join([self.itemnames[i]+": "+str(self.values[i])+"\n" for i in range(self.nitems)])[:-1])   # normalize text in textbox
        if not self.callback_on_textupdate is None: self.callback_on_textupdate()
        
            
    def getWidgetSize(self):   # return (width,height) tuple
        return (self.sizeX,self.sizeY)
       
    def bind(self,eventType,function2call,obj=None):  # use this method to bind a function call to the slider (e.g., if selecting a new value)
        if obj==None:
            obj="slider"
        if obj=="slider":
            self.callback_on_sliderupdate=function2call
        if obj=='optionmenu':
            self.callback_on_optionmenuupdate=function2call
        if obj=='textbox':
            self.callback_on_textupdate=function2call
        else:
            print("Warning in IVisitDictSliderWidget.bind(): Unknown widget object ", obj, " in IVisitDictSliderWidget", self.widgetdef.name)
        return None
            
# ***********************************************************************
# class IVisitTextInputWidget:
# IVisit Text-Input Widget to control a string-type simulation parameter
# ***********************************************************************

class IVisitTextInputWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitTextInputWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        assert isinstance(self.widgetdef,ParameterWidgetDef), "IVisitTextInputWidget needs to be initialized with a ParameterWidgetDef, but self.widgetdef="+str(self.widgetdef.name)+" is not!" 
        assert self.widgetdef.type=='textfield', "IVisitTextInputWidget needs to be initialized with a ParameterWidgetDef having type='textfield', but actually type="+str(self.widgetdef.type)+" is not valid!" 
        assert self.widgetdef.type_parameter=='text' or self.widgetdef.type_parameter=='string', "IVisitTextInputWidget needs to be initialized with a parameter of type 'text' or 'string', but actually parameter_type="+str(self.widgetdef.type_parameter)+" is not valid!"
        #assert isinstance(self.widgetdef.range,(tuple,list)) and len(self.widgetdef.range)>=4, "IVisitTextInputWidget '"+str(self.widgetdef.name)+"' must have attribute range=[min,max,nTicks,scale], but actually range="+str(self.widgetdef.range)+"!"
        self.label.pack(side=LEFT)
        #assert(self.widgetdef.range[0]<=self.widgetdef.range[1])and(self.widgetdef.range[3]>=0),"IVisitTextInputWidget.__init__: wrong slider range parameters for slider widget " +\
        #    self.widgetdef.name + "! It must be min<=max and scale>0, whereas range=" + str(self.widgetdef.range) + "! Have a look at range specification in the corresponding " +\
        #    "parameter definition in the ParameterWidget table! Check format range=[min,max,nTicks,scale] after parameter name!"
        self.cols,self.rows = self.widgetdef.size[0], self.widgetdef.size[1]
        self.str_var = StringVar()
        self.str_var.set(str(self.widgetdef.value))
        self.textframe = SupyTextFrame(self, width=self.cols, height=self.rows, catch_focus=False, textvariable=self.str_var)
        self.textframe.pack(side=LEFT)
        self.setbutton=Button(self,text='Set',command=self.onSet)
        self.setbutton.pack(side=LEFT)
        self.callback_on_textUpdate = None
        self.onSet() 
        self.setState()

    def set(self,text):     # set text
        self.textframe.settext(str(text))
        print("str_var=",str(text))
        self.onSet()
    
    def setState(self):        # set object fields that are derived from widget and data definitions
        #min=c_double()    # ?????
        self.sizeX, self.sizeY = self.label.winfo_reqwidth()+self.textframe.winfo_reqwidth()+self.setbutton.winfo_reqwidth(),self.label.winfo_reqheight()+self.textframe.winfo_reqheight()+self.setbutton.winfo_reqheight()
        #print "slider.sizeX=", self.sizeX, " sizeY=", self.sizeY

    def onSet(self):
        #print("onMove...;flag=",flagIgnoreModFlag)
        #assert flagIgnoreModFlag==1
        #if(flagIgnoreModFlag<=0): 
        #    self.parent.isModified=True
        #    self.widgetdef.isModified=True
        newvalue = self.textframe.gettext()
        if(newvalue!=self.widgetdef.value):
            self.parent.isModified=True
            self.flagModifiedParVal=1
        self.widgetdef.value=newvalue  
        if self.widgetdef.wdefcoll.sim.updateMode!='sync': self.widgetdef.setSimParValue()     # write new parameter value to simulation (only for updateMode 'async')
        if not self.callback_on_textUpdate is None: self.callback_on_textUpdate()

    def getWidgetSize(self):   # return (width,height) tuple
        return (self.sizeX,self.sizeY)

    def bind(self,eventType,function2call,obj=None):  # use this method to bind a function call to the slider (e.g., if selecting a new value)
        if obj==None:
            obj="textfield"
        if obj=="textfield":
            self.callback_on_textUpdate=function2call
        else:
            print("Warning in IVisitTextInputWidget.bind(): Unknown widget object ", obj, " in IVisitTextInputWidget", self.widgetdef.name)
        return None
        
# ***********************************************************************
# class IVisitListSelectionWidget:
# IVisit Option-List to control a string-type simulation parameter
# ***********************************************************************

class IVisitListSelectionWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitListSelectionWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        assert isinstance(self.widgetdef,ParameterWidgetDef), "IVisitTextInputWidget needs to be initialized with a ParameterWidgetDef, but self.widgetdef="+str(self.widgetdef.name)+" is not!" 
        assert self.widgetdef.type=='listselection', "IVisitTextInputWidget needs to be initialized with a ParameterWidgetDef having type='listsel', but actual type="+str(self.widgetdef.type)+" is not valid!" 
        assert self.widgetdef.type_parameter in ['text','string','int','float'], "IVisitListSelectionWidget needs to be initialized with a parameter of type 'text' or 'string' or 'int' or 'float', but actual parameter_type="+str(self.widgetdef.type_parameter)+" is not valid!"
        #assert isinstance(self.widgetdef.range,(tuple,list)) and len(self.widgetdef.range)>=4, "IVisitTextInputWidget '"+str(self.widgetdef.name)+"' must have attribute range=[min,max,nTicks,scale], but actually range="+str(self.widgetdef.range)+"!"
        self.label.pack(side=LEFT)
        #assert(self.widgetdef.range[0]<=self.widgetdef.range[1])and(self.widgetdef.range[3]>=0),"IVisitTextInputWidget.__init__: wrong slider range parameters for slider widget " +\
        #    self.widgetdef.name + "! It must be min<=max and scale>0, whereas range=" + str(self.widgetdef.range) + "! Have a look at range specification in the corresponding " +\
        #    "parameter definition in the ParameterWidget table! Check format range=[min,max,nTicks,scale] after parameter name!"
        self.listvalues = self.widgetdef.range    # list of strings to be diplayed in the OptionMenu
        self.listvalues = [str(s) for s in self.listvalues]
        self.str_var = StringVar()
        self.str_var.set(str(self.widgetdef.value))
        #print("ListSel: widgetdef.value=",self.widgetdef.value)
        self.optionmenu = OptionMenu(self,self.str_var,command=self.onSet,*self.listvalues)
        self.optionmenu.pack(side=LEFT)
        self.callback_on_optionmenuupdate=None
        self.setState()
        self.onSet()

    def setState(self):        # set object fields that are derived from widget and data definitions
        #min=c_double()    # ?????
        self.sizeX, self.sizeY = self.label.winfo_reqwidth()+self.optionmenu.winfo_reqwidth(), self.label.winfo_reqheight()+self.optionmenu.winfo_reqheight()
        #print "slider.sizeX=", self.sizeX, " sizeY=", self.sizeY

    def onSet(self,e=None):
        #print("onMove...;flag=",flagIgnoreModFlag)
        #assert flagIgnoreModFlag==1
        #if(flagIgnoreModFlag<=0): 
        #    self.parent.isModified=True
        #    self.widgetdef.isModified=True
        newvalue = self.str_var.get() 
        if(newvalue!=self.widgetdef.value):
            self.parent.isModified=True
            self.flagModifiedParVal=1
        self.widgetdef.value=newvalue  
        if self.widgetdef.wdefcoll.sim.updateMode!='sync': self.widgetdef.setSimParValue()     # write new parameter value to simulation (only for updateMode 'async')
        if not self.callback_on_optionmenuupdate is None: self.callback_on_optionmenuupdate()

    def getWidgetSize(self):   # return (width,height) tuple
        return (self.sizeX,self.sizeY)
       
    def bind(self,eventType,function2call,obj=None):  # use this method to bind a function call to the OptionMenu (e.g., if selecting a new value)
        if obj==None:
            obj="optionmenu"
        if obj=="optionmenu":
            self.callback_on_optionmenuupdate=function2call
        else:
            print("Warning in IVisitListSelectionWidget.bind(): Unknown widget object ", obj, " in IVisitListSelectionWidget", self.widgetdef.name)
        return None
            
# **************************************************************************
# class IVisitCheckboxWidget:
# IVisit Checkbox to control a string of boolean-type simulation parameters
# **************************************************************************

class IVisitCheckboxWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitCheckboxWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        assert isinstance(self.widgetdef,ParameterWidgetDef), "IVisitCheckboxWidget needs to be initialized with a ParameterWidgetDef, but self.widgetdef="+str(self.widgetdef.name)+" is not!" 
        assert self.widgetdef.type=='checkbox', "IVisitCheckboxWidget "+str(self.widgetdef.name)+" needs to be initialized with a ParameterWidgetDef having type='checkbox', but actual type="+str(self.widgetdef.type)+" is not valid!" 
        assert self.widgetdef.type_parameter in ['string','str','text'], "IVisitCheckboxWidget "+str(self.widgetdef.name)+" needs to be initialized with parameters of type 'text', but actual parameter_type="+str(self.widgetdef.type_parameter)+" is not valid!"
        assert isinstance(self.widgetdef.range,(tuple,list)), "IVisitCheckboxWidget "+str(self.widgetdef.name)+": IVisitCheckboxWidget.widgetdef.range="+str(self.widgetdef.range)+" must be a string list!"
        assert isinstance(self.widgetdef.value,str), "IVisitCheckboxWidget "+str(self.widgetdef.name)+": IVisitCheckboxWidget.widgetdef.value="+str(self.widgetdef.value)+" must be a string!"
        assert len(self.widgetdef.range)==len(self.widgetdef.value), "IVisitCheckboxWidget "+str(self.widgetdef.name)+": IVisitCheckboxWidget.widgetdef.value and range must have same length!"
        self.label.pack(side=LEFT)
        self.checkboxFrame=Frame(self)
        self.checkboxFrame.pack(side=BOTTOM,expand=True,fill=BOTH)
        self.listkeys = self.widgetdef.range    # list of strings to be diplayed in the Checkbox Frame
        self.listvalues = [str(s) for s in self.listkeys]
        self.int_vars = [IntVar() for s in self.listvalues]
        self.checkbuttons=[Checkbutton(self.checkboxFrame, text=self.listkeys[i], variable=self.int_vars[i], command=self.onSet, justify=LEFT, anchor="w") for i in range(len(self.int_vars))]
        for i in range(len(self.int_vars)):
            assert self.widgetdef.value[i] in ['0','1'], "IVisitCheckboxWidget "+str(self.widgetdef.name)+": IVisitCheckboxWidget.widgetdef.value="+str(self.widgetdef.value)+" must be a string of '0' and '1'!"
            self.int_vars[i].set(int(self.widgetdef.value[i]))
            self.checkbuttons[i].grid(row=i,sticky=W)
        self.callback_on_checkboxupdate=None
        self.setState()
        self.onSet()

    def setState(self):        # set object fields that are derived from widget and data definitions
        self.sizeX = max([self.winfo_reqwidth()]+[self.label.winfo_reqwidth()]+[cb.winfo_reqwidth() for cb in self.checkbuttons])
        self.sizeY = self.label.winfo_reqheight()+np.sum([cb.winfo_reqheight() for cb in self.checkbuttons])

    def setValue(self,val):
        assert isinstance(val,str), "IVisitCheckboxWidget "+str(self.widgetdef.name)+": parameter val="+str(val)+" must be string of '0' and '1'"
        assert len(val)==len(self.int_vars), "IVisitCheckboxWidget "+str(self.widgetdef.name)+": length len(val)="+str(len(val))+" must be the same as number of checkboxes "+str(len(self.int_vars))
        for i in range(len(val)):
            assert val[i] in ['0','1'], "parameter val="+str(val)+" must be string of '0' and '1'"
            self.int_vars[i].set(int(val[i]))

    def onSet(self,e=None):
        newvalue = "".join([str(iv.get()) for iv in self.int_vars])
        if newvalue!=self.widgetdef.value:
            self.parent.isModified=True  # newvalue differs from previous value?
            self.flagModifiedParVal=1
        self.widgetdef.value=newvalue                                   # copy newvalue 
        if self.widgetdef.wdefcoll.sim.updateMode!='sync': self.widgetdef.setSimParValue()           # write new parameter value to simulation (only for updateMode 'async')
        if not self.callback_on_checkboxupdate is None: self.callback_on_checkboxupdate()

    def getWidgetSize(self):   # return (width,height) tuple
        return (self.sizeX,self.sizeY)
       
    def bind(self,eventType,function2call,obj=None):  # use this method to bind a function call to the OptionMenu (e.g., if selecting a new value)
        if obj==None:
            obj="checkbox"
        if obj=="checkbox":
            self.callback_on_checkboxupdate=function2call
        else:
            print("Warning in IVisitCheckboxWidget.bind(): Unknown widget object ", obj, " in IVisitCheckboxWidget", self.widgetdef.name)
        return None
            
# ***********************************************************************
# class IVisitRadiobuttonWidget:
# IVisit Radiobutton to control a string of boolean-type simulation parameters
# ***********************************************************************

class IVisitRadiobuttonWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitRadioButtonWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        assert isinstance(self.widgetdef,ParameterWidgetDef), "IVisitRadiobuttonWidget needs to be initialized with a ParameterWidgetDef, but self.widgetdef="+str(self.widgetdef.name)+" is not!" 
        assert self.widgetdef.type=='radiobutton', "IVisitRadiobuttonWidget needs to be initialized with a ParameterWidgetDef having type='radiobutton', but actual type="+str(self.widgetdef.type)+" is not valid!" 
        assert self.widgetdef.type_parameter in ['string','str','text'], "IVisitRadiobuttonWidget needs to be initialized with parameters of type 'text', but actual parameter_type="+str(self.widgetdef.type_parameter)+" is not valid!"
        assert isinstance(self.widgetdef.range,(tuple,list)), "IVisitRadiobuttonWidget.widgetdef.range="+str(self.widgetdef.range)+" must be a string list!"
        assert isinstance(self.widgetdef.value,str), "IVisitRadiobuttonWidget.widgetdef.value="+str(self.widgetdef.value)+" must be a string!"
        self.label.pack(side=LEFT)
        self.radiobuttonFrame=Frame(self)
        self.radiobuttonFrame.pack(side=BOTTOM,expand=True,fill=BOTH)
        self.listkeys = [str(s) for s in self.widgetdef.range]  # list of strings to be diplayed in the Radiobutton Frame
        self.str_var = StringVar()
        self.radiobuttons=[Radiobutton(self.radiobuttonFrame, text=self.listkeys[i], variable=self.str_var, command=self.onSet, justify=LEFT, anchor="w", value=self.listkeys[i]) for i in range(len(self.listkeys))]
        self.dict_radiobuttons={self.listkeys[i]:self.radiobuttons[i] for i in range(len(self.listkeys))}
        assert str(self.widgetdef.value) in self.listkeys, \
            "IVisitRadiobuttonWidget needs to be initialized a value in listkeys="+str(self.listkeys)+" but widgetdef.value="+str(self.widgetdef.value)+" is not contained in this list!"
        self.str_var.set(str(self.widgetdef.value))
        for i in range(len(self.radiobuttons)):
            self.radiobuttons[i].grid(row=i,sticky=W)
        self.callback_on_radiobuttonupdate=None
        self.setState()
        self.onSet()

    def setState(self):        # set object fields that are derived from widget and data definitions
        self.sizeX = max([self.winfo_reqwidth()]+[self.label.winfo_reqwidth()]+[rb.winfo_reqwidth() for rb in self.radiobuttons])
        self.sizeY = self.label.winfo_reqheight()+np.sum([rb.winfo_reqheight() for rb in self.radiobuttons])

    def setValue(self,val,flagInvoke=0):
        assert isinstance(val,str), "parameter val="+str(val)+" must be a string!"
        assert val in self.listkeys, "string parameter val="+str(val)+" must be from key list "+str(self.listkeys)
        self.str_var.set(val)
        if flagInvoke>0:
            self.dict_radiobuttons[val].invoke()   # is as the user has pressed radio button (call to onSet etc.)

    def onSet(self,e=None):
        #print("onMove...;flag=",flagIgnoreModFlag)
        #assert flagIgnoreModFlag==1
        #if(flagIgnoreModFlag<=0): 
        #    self.parent.isModified=True
        #    self.widgetdef.isModified=True
        newvalue = str(self.str_var.get())
        if newvalue!=self.widgetdef.value:
            self.parent.isModified=True  # newvalue differs from previous value?
            self.flagModifiedParVal=1
        self.widgetdef.value=newvalue                                   # copy newvalue 
        if self.widgetdef.wdefcoll.sim.updateMode!='sync': self.widgetdef.setSimParValue()           # write new parameter value to simulation (only for updateMode 'async')
        if not self.callback_on_radiobuttonupdate is None: self.callback_on_radiobuttonupdate()

    def getWidgetSize(self):   # return (width,height) tuple
        return (self.sizeX,self.sizeY)
       
    def bind(self,eventType,function2call,obj=None):  # use this method to bind a function call to the OptionMenu (e.g., if selecting a new value)
        if obj==None:
            obj="radiobutton"
        if obj=="radiobutton":
            self.callback_on_radiobuttonupdate=function2call
        else:
            print("Warning in IVisitRadiobuttonWidget.bind(): Unknown widget object ", obj, " in IVisitRadiobuttonWidget", self.widgetdef.name)
        return None
            
# *********************************************************************************
# class IVisitButtonWidget:
# IVisit Button to control a boolean-type simulation parameter to initiate actions
# *********************************************************************************

class IVisitButtonWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitButtonWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        assert isinstance(self.widgetdef,ParameterWidgetDef), "IVisitButtonWidget needs to be initialized with a ParameterWidgetDef, but self.widgetdef="+str(self.widgetdef.name)+" is not!" 
        assert self.widgetdef.type=='button', "IVisitButtonWidget needs to be initialized with a ParameterWidgetDef having type='button', but actual type="+str(self.widgetdef.type)+" is not valid!" 
        assert self.widgetdef.type_parameter in ['string','str','text'], "IVisitButtonWidget needs to be initialized with parameters of type 'string', but actual parameter_type="+str(self.widgetdef.type_parameter)+" is not valid!"
        assert isinstance(self.widgetdef.range,(tuple,list)) and len(self.widgetdef.range)==2,\
            "IVisitButtonWidget.widgetdef.range="+str(self.widgetdef.range)+" must be a list [LabelText,ButtonText] of two strings!"
        assert isinstance(self.widgetdef.value,str), "IVisitButtonWidget.widgetdef.value="+str(self.widgetdef.value)+" must have type string!"
        self.lock = threading.Lock()
        #self.label.configure(text=str(self.widgetdef.range[0]))
        self.labeltext.set(self.widgetdef.range[0])
        self.label.pack(side=LEFT)
        self.button = Button(self.labelFrame,text=str(self.widgetdef.range[1]),command=self.onPressedButton)
        self.button.pack(side=RIGHT)
        self.callback_on_buttonupdate=None
        self.setState()
        self.setValue(0)

    def setState(self):        # set object fields that are derived from widget and data definitions
        self.sizeX = self.label.winfo_reqwidth()+self.button.winfo_reqwidth()
        self.sizeY = max([self.label.winfo_reqheight(),self.button.winfo_reqheight()]) 

    def setValue(self,val):
        val=str(val)
        self.lock.acquire()                       # mutual exclusion for accessing value
        if val!=self.widgetdef.value:
            self.parent.isModified=True  # newvalue differs from previous value?
            self.flagModifiedParVal=1
        self.widgetdef.value=val                  # set new value 
        if self.widgetdef.wdefcoll.sim.updateMode!='sync': self.widgetdef.setSimParValue()           # write new parameter value to simulation (only for updateMode 'async')
        self.lock.release()

    def onPressedButton(self,e=None):
        #print("onMove...;flag=",flagIgnoreModFlag)
        #assert flagIgnoreModFlag==1
        #if(flagIgnoreModFlag<=0): 
        #    self.parent.isModified=True
        #    self.widgetdef.isModified=True
        self.setValue(1)                          # set value to 1
        if not self.callback_on_buttonupdate is None: self.callback_on_buttonupdate()

    def getWidgetSize(self):   # return (width,height) tuple
        return (self.sizeX,self.sizeY)
       
    def bind(self,eventType,function2call,obj=None):  # use this method to bind a function call to the button (e.g., if selecting a new value)
        if obj==None:
            obj="button"
        if obj=="button":
            self.callback_on_buttonupdate=function2call
        else:
            print("Warning in IVisitButtonWidget.bind(): Unknown widget object ", obj, " in IVisitButtonWidget", self.widgetdef.name)
        return None
            
# *********************************************************
# class IVisitTextCommentWidget:
# IVisit Comment Widget to display a comment as a textfield  
# *********************************************************

class IVisitTextCommentWidget(Frame,IVisitWidget):
    def __init__(self,parent,widgetdef_arg,className="IVisitTextCommentWidget"):
        Frame.__init__(self,master=parent)
        IVisitWidget.__init__(self,parent,widgetdef_arg,className)
        assert self.widgetdef.type=='textfield', "IVisitTextCommentWidget needs to be initialized with a CommentWidgetDef having type='textfield', but actually type="+str(self.widgetdef.type)+" is not valid!"
        if (self.widgetdef.flagDisplayName<1):
            self.labeltext.set(self.widgetdef.comment)
        else:
            n=self.widgetdef.name
            self.labeltext.set(n+'\n'+len(n)*'-'+self.widgetdef.comment)
        self.label.configure(fg=self.widgetdef.fontcolor,font=(self.widgetdef.fontname,self.widgetdef.fontsize,self.widgetdef.fontstyle))
        self.label.pack(side=TOP)
        self.setState()
        if(className=="IVisitTextCommentWidget"): self.updateData()      # derived classes may need further preprocessing before call

    def setState(self):        # set object fields that are derived from widget and data definitions
        self.sizeX, self.sizeY = self.label.winfo_reqwidth(), self.label.winfo_reqheight()
        #self.shape=np.array(self.widgetdef.data).shape
        #assert len(self.shape)>=2, "IVisitImageWidget '"+str(self.widgetdef.name)+"' is of type 'image', but is associatied to a dataarray '" + str(self.widgetdef.name_dataarray) + "' with less than 2 dimensions!" 
        #self.RGBflag=0         # default a 2D gray scale array
        #if len(self.shape)>=3: self.RGBflag=1    # 3D RGB array?
        #self.NY, self.NX = self.shape[0],self.shape[1]
        #self.CX, self.CY = int(self.widgetdef.scale*self.NX), int(self.widgetdef.scale*self.NY)
        #self.SZ          = self.CX * self.CY

    def updateData(self):
        pass

    def getWidgetSize(self):   # return (width,height) tuple
        return (self.sizeX,self.sizeY)
       
        
# *********************************************************
# class IVisitWidgetFactory:
# Factory class to create different types of IVisitWidgest
# *********************************************************
class IVisitWidgetFactory:
    def create_IVisitWidget(self,parent,widgetdef):
        assert isinstance(widgetdef,(ParameterWidgetDef,DataWidgetDef,CommentWidgetDef)), "widgetdef must be either a ParameterWidgetDef or DataWidgetDef or CommentWidgetDef!" 
        if isinstance(widgetdef,ParameterWidgetDef):
            assert widgetdef.type in ['slider','dictslider','listselection','checkbox','radiobutton','button','textfield'], \
                "ParameterWidgetDef with name="+str(widgetdef.name)+" has type="+str(widgetdef.type)+" which is not yet implemented!"
            if  (widgetdef.type=='slider'         ):
                #print("widgetdef of slider:")
                #widgetdef.printState()
                return IVisitSliderWidget(parent,widgetdef)
            elif(widgetdef.type=='dictslider'     ):
                #print("widgetdef of dictslider:")
                #widgetdef.printState()
                #exit(0)
                return IVisitDictSliderWidget(parent,widgetdef)
            elif(widgetdef.type=='listselection'  ): return IVisitListSelectionWidget(parent,widgetdef)
            elif(widgetdef.type=='checkbox'       ): return IVisitCheckboxWidget(parent,widgetdef)
            elif(widgetdef.type=='radiobutton'    ): return IVisitRadiobuttonWidget(parent,widgetdef)
            elif(widgetdef.type=='button'         ): return IVisitButtonWidget(parent,widgetdef)
            elif(widgetdef.type=='textfield'      ): return IVisitTextInputWidget(parent,widgetdef)
        if isinstance(widgetdef,DataWidgetDef):
            assert widgetdef.type in ['image','textfield'], "DataWidgetDef with name="+str(widgetdef.name)+" has type="+str(widgetdef.type)+" which is not yet implemented!"
            if   (widgetdef.type=='image'    ): return IVisitImageWidget(parent,widgetdef)
            elif (widgetdef.type=='textfield'): return IVisitTextfieldWidget(parent,widgetdef)
        if isinstance(widgetdef,CommentWidgetDef):
            assert widgetdef.type in ['textfield'], "CommentWidgetDef with name="+str(widgetdef.name)+" has type="+str(widgetdef.type)+" which is not yet implemented!"
            if(widgetdef.type=='textfield'): return IVisitTextCommentWidget(parent,widgetdef)
        return None

# ******************************************
# class IVisitRawDisplayFrame:
# Database of Widgets 
# ******************************************
class IVisitRawDisplayFrame(Frame):
    def __init__(self,parent,wdefcoll=None):
        Frame.__init__(self,master=parent,width=200,height=500)
        self.isModified=False
        self.widgets=[]
        self.dict_widgets={}
        self.data_widgets=[]
        self.par_widgets=[]
        self.com_widgets=[]
        self.wdefcoll=None
        self.createWidgets(wdefcoll)

    def createWidgets(self,wdefcoll):
        if(wdefcoll): 
            self.wdefcoll=wdefcoll
            # first remove old widgets...
            self.deleteWidgets()
            # create new widgets...
            widget_factory = IVisitWidgetFactory()
            for wdef in wdefcoll.wdefs_data+wdefcoll.wdefs_parameters+wdefcoll.wdefs_comments:
                #w=widget_factory.create_PyFeWidget(self,database,wdef)
                w=widget_factory.create_IVisitWidget(self,wdef)
                assert w, "Unable to create widget "+ wdef.name + " of type " + wdef.type 
                #sz=w.getWidgetSize()
                #self.geometry("%dx%d+%d+%d" % (sz[0],sz[1],w.posX,w.posY))
                w.place(x=wdef.pos[0],y=wdef.pos[1])
                #w.place(x=0, y=0)
                #w.pack()       
                self.widgets.append(w)
                self.dict_widgets[w.widgetdef.name]=w
                if isinstance(wdef,ParameterWidgetDef): self.par_widgets.append(w)
                if isinstance(wdef,DataWidgetDef): self.data_widgets.append(w)
                if isinstance(wdef,CommentWidgetDef): self.com_widgets.append(w)
            self.updateData()

            #database.libSim.PyFeInter_checkUpdatedParameters(0); # update parameters according to loaded slider values

    def deleteWidgets(self):
        for w in self.widgets:
            w.place_forget()
        self.widgets=[]
        self.data_widgets=[]
        self.par_widgets=[]

    def resetButtonsAndFlags(self,flagModifiedParVal=0):  # reset Button variables after each call to step() (where the values may be checked!!)
        for w in self.widgets:
            w.flagModifiedParVal=flagModifiedParVal                  # reset modified flag for ParameterWidgets
            if isinstance(w,IVisitButtonWidget): w.setValue(0)       # reset button
        
    def updateData(self):
        for w in self.data_widgets: 
            w.updateData()
        self.adaptSize()
            #w.update_idletasks()             

    def adaptSize(self):
        maxX,maxY = 100,100
        for w in self.widgets:
            xx,yy = w.widgetdef.pos[0]+w.sizeX, w.widgetdef.pos[1]+w.sizeY
            if(xx>maxX): maxX=xx
            if(yy>maxY): maxY=yy
        self.configure(width=maxX+50,height=maxY+50)
        try:
            self.master.adaptSize()
            #self.master.master.adaptSize()
            #self.master.master.master.adaptSize()
            #self.master.master.adaptSize()     # ok, this is not so elegent, making some special assumptions, but it works....
        except:
            #print "exception: no master.master.adaptSize()!!!!"
            pass
        else:
            #print "no exception: there is master.master.adaptSize()!!!!"
            pass
    
    def saveGUIDataToDatabase(self, flagForce=0):
        if (self.isModified or (flagForce>0)) and len(self.widgets)>0: self.wdefcoll.saveToDatabase()
        self.isModified=False

    def bind2Widget(self,widgetname,eventType,function2call,widgetobj=None):  # bind function2call to object obj of widget widgetname if eventType happens
        found=False
        for w in self.widgets:
            if w.widgetdef.name==widgetname:
                found=True
                break
        if found:
            res_wobj=w.bind(eventType,function2call,widgetobj)
        else:
            print("Warning in IVisitRawDisplayFrame.bind2Widget: Unknown widget ",widgetname)
            res_wobj=None
        return res_wobj

    def getWidget(self,widgetname):
        try:
            w=self.dict_widgets[widgetname]
        except KeyError:
            w=None
        finally:
            return w
        #found=False
        #for w in self.widgets:
        #    if w.widgetdef.name==widgetname:
        #        found=True
        #        break
        #if found: return w
        #else: return None

    def getFlagModified(self,widgetname=None):
        if widgetname is None: return self.isModified
        else:
            w=self.getWidget(widgetname)
            if w is None: return 0
            else: return w.flagModifiedParVal
        
    def setWidgetValue(self,widgetname,val):
        w=self.getWidget(widgetname)
        if not w is None:
            w.setValue(val)
        else:
            print("Warning in IVisitRawDisplayFrame.setWidgetValue: Unknown widget ",widgetname)
            
            
if __name__ == '__main__':
    print("\nModule test of ivisit.widgetcollection.py")
    print("-------------------------------------------\n") 
    # (i) read widgetsdefs from database
    db = sqldatabase(db_ivisit_cfg)
    sim=IVisit_Simulation()
    wdefcoll = IVisitWidgetDefCollection(db,sim)
    wdefcoll.initFromDatabase(0)
    #wdefcoll.printState()
    # (ii) create widgets and display
    root=Tk()
    f=IVisitRawDisplayFrame(root,wdefcoll)
    f.adaptSize()
    f.pack()
    wdefcoll.sim.main_init()
    wdefcoll.sim.init()
    for i in range(200): 
        wdefcoll.sim.step()
    f.updateData()
    f.update()
    root.mainloop()
 

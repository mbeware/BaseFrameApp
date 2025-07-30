#!/usr/bin/python3
from os import name
import tkinter as tk
import tkinter.ttk as ttk
import Template_OutilsUIui as baseui
from tkinter import Widget

from os import path

SCRIPT_PATH = path.abspath(__file__)
SCRIPT_DIRECTORY = path.dirname(path.abspath(__file__))
ASSETS_DIRECTORY = path.join(SCRIPT_DIRECTORY, "Assets")
#
# Begin image loader - Setup image_loader in derived class file
#
def better_image_loader(image_name):
    img = None
    image_full_path = path.join(ASSETS_DIRECTORY, image_name)

    try:
        img = tk.PhotoImage(file=image_full_path)
    except tk.TclError:
        pass
    return img


baseui.image_loader = better_image_loader
# End image loader




class OutilUI(baseui.OutilUIUI):
    def __init__(self, master=None):
        super().__init__(master)
        self.bo = super()
        # self.img_icon_placehorder_logo_64x64 = image_loader("/home/mbeware/Documents/dev/BaseFrameApp/Assets/icon_placehorder_logo.64x64.png")
        # self.img_icon_placehorder_toggleLogin_32x32 = image_loader("/home/mbeware/Documents/dev/BaseFrameApp/Assets/icon_placehorder_toggleLogin.32x32.png")
        # self.img_icon_placehorder_nav1_32x32 = image_loader("/home/mbeware/Documents/dev/BaseFrameApp/Assets/icon_placehorder_nav1.32x32.png")
        # self.img_icon_placehorder_nav2_32x32 = image_loader("/home/mbeware/Documents/dev/BaseFrameApp/Assets/icon_placehorder_nav2.32x32.png")
        # self.img_icon_placehorder_nav3_32x32 = image_loader("/home/mbeware/Documents/dev/BaseFrameApp/Assets/icon_placehorder_nav3.32x32.png")
        # self.img_icon_placehorder_config_32x32 = image_loader("/home/mbeware/Documents/dev/BaseFrameApp/Assets/icon_placehorder_config.32x32.png")
        # self.img_icon_placehorder_aide_32x32 = image_loader("/home/mbeware/Documents/dev/BaseFrameApp/Assets/icon_placehorder_aide.32x32.png")
        

        # self.UI_ToggleLoginOption.set('False')
        # self.UI_NomApplication.set('Test de l\'application')
        # self.DYN_UI_Field_datauser.set('Des données utilisateur')
        # self.DYN_UI_data_datauser.set('Le nom de l\'utilisateur')
        # self.DYN_UI_lb_datauser.set('libellé')
        # self.UI_App_Messages.set('Tout va bien !')
        # self.UI_NavOption1.set('Utilisateur')
        # self.UI_NavOption2.set('Developpeur')
        # self.UI_NavOption3.set('Admin')
        # self.UI_NavConfig.set('---')

        # self.ID_Logo.configure(image=self.img_icon_placehorder_logo_64x64)
        # self.ID_ToggleLoginOption.configure(image=self.img_icon_placehorder_toggleLogin_32x32)
        # self.ID_NavOption1.configure(image=self.img_icon_placehorder_nav1_32x32)
        # self.DYN_NavOption2.configure(image=self.img_icon_placehorder_nav2_32x32)
        # self.DYN_NavOption3.configure(image=self.img_icon_placehorder_nav3_32x32)
        # self.ID_NavConfig.configure(image=self.img_icon_placehorder_config_32x32)
        # self.ID_Aide.configure(image=self.img_icon_placehorder_aide_32x32)

        # read the configuration of a widget
        

        self.ID_AIDE_command =self.ID_Aide.cget("command")
        self.ID_NavOption1_command = self.ID_NavOption1.cget("command")

        self.LastNavigationSelected = "ID_NavOption1"


    def showOnlyform(self, navwidget_id):   
        allNavButton  = {}
        for  aaa in self.ID_SectionNavApp.children.values():   
            
                        
            print(f"aaa: {aaa.winfo_name()}")
            for  navbutton_widget in aaa.children.values():
                print(f"navbutton_widget: {navbutton_widget.winfo_name()}")
                allNavButton[navbutton_widget.winfo_name()] =navbutton_widget

        navselected = allNavButton[navwidget_id]
        lastnavselected = allNavButton[self.LastNavigationSelected] 
        navform = self.ID_Section_Forms.children[navselected.winfo_class()]    
                                                 # cget("class")]
        lastform = self.ID_Section_Forms.children[lastnavselected.cget("class")]
        lastform.pack_forget()
        navform.pack()
        lastnavselected.master.configure(relief="raised")
        navselected.master.configure(relief="groove")
        
        self.LastNavigationSelected = navwidget_id
        




    def ChangeSelectedNavOption(self, widget_id):
        # multiple widgets can have the same command
            self.showOnlyform(widget_id)
            print(f"ChangeSelectedNavOption called with widget_id: {widget_id}")
        

    def OutilsUIValidate(self, d_action, i_index, p_entry_value,
                         s_prev_value, s_new_value, v_validate, v_condition, w_entry_name):
        pass

    def OutilsUIValidationError(self, d_action, i_index, p_entry_value,
                                s_prev_value, s_new_value, v_validate, v_condition, w_entry_name):
        pass

    def ClickButton(self, event=None):
        print(f"ClickButton called with     event: {event}")
        
if __name__ == "__main__":
    app = OutilUI()
    app.run()

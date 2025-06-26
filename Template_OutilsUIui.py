#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from customtkinter import CTkTabview
from pygubu.forms.ttkwidget import (Entry, Label)
from ttkwidgets.linklabel import LinkLabel


#
# Begin image loader - Setup image_loader in derived class file
#
def default_image_loader(image_name):
    img = None
    try:
        img = tk.PhotoImage(file=image_name)
    except tk.TclError:
        pass
    return img


image_loader = default_image_loader
# End image loader


class OutilUIUI:
    def __init__(self, master=None, data_pool=None):
        # build ui
        self.ID_OutilsUI = tk.Tk(master, baseName="baseName")
        self.ID_Section_app = ttk.Frame(
            self.ID_OutilsUI, name="id_section_app")
        self.ID_Section_app.configure(height=200, padding=2, width=500)
        self.ID_Section_Forms = ttk.Frame(
            self.ID_Section_app, class_="A", name="id_section_forms")
        self.ID_Section_Forms.configure(
            borderwidth=2, height=200, relief="groove", width=200)
        self.ID_NavOption1_form = CTkTabview(self.ID_Section_Forms)
        ID_Tab1 = self.ID_NavOption1_form.add("REQ tab 1")
        self.ID_TabContainer_1 = ttk.Frame(ID_Tab1, name="id_tabcontainer_1")
        self.ID_TabContainer_1.configure(height=200, width=200)
        self.DYN_label_datauser = Label(
            self.ID_TabContainer_1,
            field_name="DYN_FN_label_datauser",
            name="dyn_label_datauser")
        self.DYN_UI_lb_datauser = tk.StringVar(value='DYN label datauser')
        self.DYN_label_datauser.configure(
            anchor="w",
            text='DYN label datauser',
            textvariable=self.DYN_UI_lb_datauser)
        self.DYN_label_datauser.pack(anchor="n", side="left")
        self.DYN_entry_datauser = Entry(
            self.ID_TabContainer_1,
            field_name="DYN_FN_data_datauser",
            name="dyn_entry_datauser")
        self.DYN_UI_data_datauser = tk.StringVar(value='Lf1 Datasss')
        self.DYN_entry_datauser.configure(
            exportselection=True,
            textvariable=self.DYN_UI_data_datauser,
            validate="focusout")
        _text_ = 'Lf1 Datasss'
        self.DYN_entry_datauser.delete("0", "end")
        self.DYN_entry_datauser.insert("0", _text_)
        self.DYN_entry_datauser.pack(anchor="n", side="left")
        _validatecmd = (
            self.DYN_entry_datauser.register(
                self.OutilsUIValidate),
            "%d",
            "%i",
            "%P",
            "%s",
            "%S",
            "%v",
            "%V",
            "%W")
        self.DYN_entry_datauser.configure(validatecommand=_validatecmd)
        _validatecmd = (
            self.DYN_entry_datauser.register(
                self.OutilsUIValidationError),
            "%d",
            "%i",
            "%P",
            "%s",
            "%S",
            "%v",
            "%V",
            "%W")
        self.DYN_entry_datauser.configure(invalidcommand=_validatecmd)
        self.ID_TabContainer_1.pack(expand=True, fill="both", side="top")
        DYN_Tab2 = self.ID_NavOption1_form.add("DYN tab 2")
        self.DYN_TabContainer_2 = ttk.Frame(
            DYN_Tab2, name="dyn_tabcontainer_2")
        self.DYN_TabContainer_2.configure(height=200, width=200)
        self.linklabel1 = LinkLabel(self.DYN_TabContainer_2)
        self.linklabel1.configure(text='linklabel1')
        self.linklabel1.pack(side="top")
        self.DYN_TabContainer_2.pack(expand=True, fill="both", side="top")
        DYN_Tab3 = self.ID_NavOption1_form.add("DYN tab 3")
        self.DYN_TabContainer_3 = ttk.Frame(
            DYN_Tab3, name="dyn_tabcontainer_3")
        self.DYN_TabContainer_3.configure(height=200, width=200)
        self.DYN_TabContainer_3.pack(expand=True, fill="both", side="top")
        self.ID_NavOption1_form.pack(
            anchor="center",
            expand=True,
            fill="both",
            padx=4,
            side="top")
        self.DYN_NavOption2_form = CTkTabview(self.ID_Section_Forms)
        tab1 = self.DYN_NavOption2_form.add("Info--")
        self.frame21 = ttk.Frame(tab1, name="frame21")
        self.frame21.configure(height=200, width=200)
        self.label5 = Label(
            self.frame21,
            field_name="DYN_FN_label_datauser",
            name="label5")
        self.label5.configure(
            anchor="w",
            text='lab',
            textvariable=self.DYN_UI_lb_datauser)
        self.label5.pack(anchor="n", side="left")
        self.entry4 = Entry(
            self.frame21,
            field_name="DYN_FN_data_datauser",
            name="entry4")
        self.DYN_UI_data_datauser3 = tk.StringVar(value='g')
        self.entry4.configure(
            exportselection=True,
            textvariable=self.DYN_UI_data_datauser3,
            validate="focusout")
        _text_ = 'g'
        self.entry4.delete("0", "end")
        self.entry4.insert("0", _text_)
        self.entry4.pack(anchor="n", side="left")
        _validatecmd = (
            self.entry4.register(
                self.OutilsUIValidate),
            "%d",
            "%i",
            "%P",
            "%s",
            "%S",
            "%v",
            "%V",
            "%W")
        self.entry4.configure(validatecommand=_validatecmd)
        _validatecmd = (
            self.entry4.register(
                self.OutilsUIValidationError),
            "%d",
            "%i",
            "%P",
            "%s",
            "%S",
            "%v",
            "%V",
            "%W")
        self.entry4.configure(invalidcommand=_validatecmd)
        self.frame21.pack(expand=True, fill="both", side="top")
        self.DYN_NavOption2_form.pack(
            anchor="center",
            expand=True,
            fill="both",
            padx=4,
            side="top")
        self.ID_AppMessages = tk.Message(
            self.ID_Section_Forms, name="id_appmessages")
        self.UI_App_Messages = tk.StringVar(value='DEF message')
        self.ID_AppMessages.configure(
            anchor="nw",
            takefocus=False,
            text='DEF message',
            textvariable=self.UI_App_Messages,
            width=600)
        self.ID_AppMessages.pack(expand=False, fill="x", side="top")
        self.ID_Section_Forms.pack(
            anchor="sw",
            expand=True,
            fill="both",
            side="right")
        self.ID_Section_Navigation = ttk.Frame(
            self.ID_Section_app, name="id_section_navigation")
        self.ID_Section_Navigation.configure(
            borderwidth=2, height=200, relief="groove", width=200)
        self.ID_SectionNavApp = ttk.Frame(
            self.ID_Section_Navigation,
            name="id_sectionnavapp")
        self.ID_SectionNavApp.configure(borderwidth=5, height=200)
        self.ID_FrameNavOption1 = ttk.Frame(
            self.ID_SectionNavApp, name="id_framenavoption1")
        self.ID_FrameNavOption1.configure(
            borderwidth=2,
            height=200,
            padding=0,
            relief="raised",
            width=200)
        self.ID_NavOption1 = ttk.Button(
            self.ID_FrameNavOption1, name="id_navoption1")
        self.img_icon_placehorder_nav1_32x32 = image_loader(
            "icon_placehorder_nav1.32x32.png")
        self.UI_NavOption1 = tk.StringVar(value='DEF NavOption1')
        self.ID_NavOption1.configure(
            compound="left",
            image=self.img_icon_placehorder_nav1_32x32,
            padding=4,
            style="Toolbutton",
            takefocus=True,
            text='DEF NavOption1',
            textvariable=self.UI_NavOption1)
        self.ID_NavOption1.pack(anchor="n", expand=False, fill="x", side="top")
        def ID_NavOption1_cmd_(): self.ChangeSelectedNavOption("ID_NavOption1")

        self.ID_NavOption1.configure(command=ID_NavOption1_cmd_)
        self.ID_FrameNavOption1.pack(anchor="n", fill="x", side="top")
        self.DYN_FrameNavOption2 = ttk.Frame(
            self.ID_SectionNavApp, name="dyn_framenavoption2")
        self.DYN_FrameNavOption2.configure(
            borderwidth=2,
            height=200,
            padding=0,
            relief="groove",
            width=200)
        self.DYN_NavOption2 = ttk.Button(
            self.DYN_FrameNavOption2, name="dyn_navoption2")
        self.img_icon_placehorder_nav2_32x32 = image_loader(
            "icon_placehorder_nav2.32x32.png")
        self.UI_NavOption2 = tk.StringVar(value='DYN NavOption2')
        self.DYN_NavOption2.configure(
            compound="left",
            image=self.img_icon_placehorder_nav2_32x32,
            padding=4,
            style="Toolbutton",
            takefocus=True,
            text='DYN NavOption2',
            textvariable=self.UI_NavOption2)
        self.DYN_NavOption2.pack(
            anchor="n",
            expand=False,
            fill="x",
            side="top")

        def DYN_NavOption2_cmd_(): self.ChangeSelectedNavOption("DYN_NavOption2")

        self.DYN_NavOption2.configure(command=DYN_NavOption2_cmd_)
        self.DYN_FrameNavOption2.pack(
            anchor="n", expand=False, fill="x", side="top")
        self.DYN_FrameNavOption3 = ttk.Frame(
            self.ID_SectionNavApp, name="dyn_framenavoption3")
        self.DYN_FrameNavOption3.configure(
            borderwidth=2,
            height=200,
            padding=0,
            relief="raised",
            width=200)
        self.DYN_NavOption3 = ttk.Button(
            self.DYN_FrameNavOption3, name="dyn_navoption3")
        self.img_icon_placehorder_nav3_32x32 = image_loader(
            "icon_placehorder_nav3.32x32.png")
        self.UI_NavOption3 = tk.StringVar(value='DYN NavOption3')
        self.DYN_NavOption3.configure(
            compound="left",
            image=self.img_icon_placehorder_nav3_32x32,
            padding=4,
            style="Toolbutton",
            takefocus=True,
            text='DYN NavOption3',
            textvariable=self.UI_NavOption3)
        self.DYN_NavOption3.pack(
            anchor="n",
            expand=False,
            fill="x",
            side="top")

        def DYN_NavOption3_cmd_(): self.ChangeSelectedNavOption("DYN_NavOption3")

        self.DYN_NavOption3.configure(command=DYN_NavOption3_cmd_)
        self.DYN_FrameNavOption3.pack(
            anchor="n", expand=False, fill="x", side="top")
        self.ID_SectionNavApp.pack(anchor="n", fill="x", side="top")
        self.ID_Section_Config = ttk.Frame(
            self.ID_Section_Navigation,
            name="id_section_config")
        self.ID_Section_Config.configure(height=200, width=200)
        self.ID_NavConfig = ttk.Button(
            self.ID_Section_Config, name="id_navconfig")
        self.img_icon_placehorder_config_32x32 = image_loader(
            "icon_placehorder_config.32x32.png")
        self.UI_NavConfig = tk.StringVar(value='button1')
        self.ID_NavConfig.configure(
            image=self.img_icon_placehorder_config_32x32,
            text='button1',
            textvariable=self.UI_NavConfig)
        self.ID_NavConfig.pack(anchor="s", expand=False, side="left")
        def ID_NavConfig_cmd_(): self.ChangeSelectedNavOption("ID_NavConfig")

        self.ID_NavConfig.configure(command=ID_NavConfig_cmd_)
        self.ID_Aide = ttk.Button(self.ID_Section_Config, name="id_aide")
        self.img_icon_placehorder_aide_32x32 = image_loader(
            "icon_placehorder_aide.32x32.png")
        self.UI_Aide = tk.StringVar(value='button2')
        self.ID_Aide.configure(
            image=self.img_icon_placehorder_aide_32x32,
            text='button2',
            textvariable=self.UI_Aide)
        self.ID_Aide.pack(anchor="s", expand=False, side="right")
        def ID_Aide_cmd_(): self.ChangeSelectedNavOption("ID_Aide")

        self.ID_Aide.configure(command=ID_Aide_cmd_)
        self.ID_ToggleLoginOption = ttk.Button(
            self.ID_Section_Config, name="id_toggleloginoption")
        self.img_icon_placehorder_toggleLogin_32x32 = image_loader(
            "icon_placehorder_toggleLogin.32x32.png")
        self.UI_ToggleLoginOption = tk.StringVar(value='button4')
        self.ID_ToggleLoginOption.configure(
            image=self.img_icon_placehorder_toggleLogin_32x32,
            text='button4',
            textvariable=self.UI_ToggleLoginOption)
        self.ID_ToggleLoginOption.pack(anchor="s", expand=False, side="bottom")
        def ID_ToggleLoginOption_cmd_(): self.ChangeSelectedNavOption("ID_ToggleLoginOption")

        self.ID_ToggleLoginOption.configure(command=ID_ToggleLoginOption_cmd_)
        self.ID_Section_Config.pack(
            anchor="s", expand=False, fill="x", side="bottom")
        self.ID_Section_Navigation.pack(
            anchor="nw", expand=True, fill="y", side="top")
        self.ID_Section_app.pack(
            anchor="n",
            expand=True,
            fill="both",
            side="left")

        # Main widget
        self.mainwindow = self.ID_OutilsUI

    def center_window(self):
        if self.mainwindow.winfo_ismapped():
            min_w, min_h = self.mainwindow.wm_minsize()
            max_w, max_h = self.mainwindow.wm_maxsize()
            screen_w = self.mainwindow.winfo_screenwidth()
            screen_h = self.mainwindow.winfo_screenheight()
            final_w = min(
                screen_w,
                max_w,
                max(
                    min_w,
                    self.mainwindow.winfo_width(),
                    self.mainwindow.winfo_reqwidth(),
                ),
            )
            final_h = min(
                screen_h,
                max_h,
                max(
                    min_h,
                    self.mainwindow.winfo_height(),
                    self.mainwindow.winfo_reqheight(),
                ),
            )
            x = (screen_w // 2) - (final_w // 2)
            y = (screen_h // 2) - (final_h // 2)
            geometry = f"{final_w}x{final_h}+{x}+{y}"

            def set_geometry():
                self.mainwindow.geometry(geometry)

            self.mainwindow.after_idle(set_geometry)
        else:
            # Window is not mapped, wait and try again later.
            self.mainwindow.after(5, self.center_window)

    def run(self, center=False):
        if center:
            self.center_window()
        self.mainwindow.mainloop()

    def OutilsUIValidate(self, d_action, i_index, p_entry_value,
                         s_prev_value, s_new_value, v_validate, v_condition, w_entry_name):
        pass

    def OutilsUIValidationError(self, d_action, i_index, p_entry_value,
                                s_prev_value, s_new_value, v_validate, v_condition, w_entry_name):
        pass

    def ChangeSelectedNavOption(self, widget_id):
        pass


if __name__ == "__main__":
    app = OutilUIUI()
    app.run()

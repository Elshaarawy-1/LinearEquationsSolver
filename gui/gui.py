
import dearpygui.dearpygui as dpg
from gui.logger import CustomLogger

class SolverGUI:
    def __init__(self) -> None:
        self.set_theme()
        self.__create_menubar()
    
    def set_theme(self, theme=None):
        if theme is None:
            with dpg.theme() as theme:

                with dpg.theme_component(dpg.mvAll):
                    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 5, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing, 5, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_IndentSpacing, 20, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 20, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 0, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, 0, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 5, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_WindowMinSize, 100, 100, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 5, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, 0.5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_style(dpg.mvStyleVar_SelectableTextAlign, 0.5, 0.5, category=dpg.mvThemeCat_Core)
        
        dpg.bind_theme(theme)
        
    def __create_menubar(self):
        with dpg.viewport_menu_bar(tag="menu_window"):
        
            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Reset GUI", callback=self.reset_gui)
                dpg.add_menu_item(label="Fullscreen",check=True, callback=lambda:dpg.toggle_viewport_fullscreen())
            with dpg.menu(label="About"):
                dpg.add_text("Linear Equations Solver - v1.0")
                dpg.add_text("CSE213 Numerical Analysis Project")
                dpg.add_text("By CSED 2026 Students :\nAhmed Ayman\nAhmed Youssef\nEbrahim Alaa\nAli Hassan\nAhmed Mustafa\nMostafa Esam")
    
    def create_windows(self):
        with dpg.window(tag="equations_window", label="System of Equations",pos=(0,30),autosize=True):
            dpg.add_input_text(tag="equations",default_value="2x+4y=5\nx-8y=15.5",multiline=True,no_spaces=True,width=580)

            with dpg.group(horizontal=True):
                dpg.add_spacer(width=423)
                dpg.add_button(label="SOLVE",width=150)
                
        with dpg.window(tag="solution_window", label="Solution",pos=(0,280),width=390,height=350):
                dpg.add_text("x1 = 1\nx2 = 5\nx3 = 8")
        
        with dpg.window(tag="steps_window",label="Steps",pos=(395,280),width=750,height=350,):
            steps = CustomLogger(title="Steps",pos=(595,300),width=550,height=350,parent="steps_window")
            mat = [[1,0],[5,1]]
            
            steps.log("L matrix = "+str(mat))
            steps.log("U matrix = "+str(mat))
        
        with dpg.window(tag="properties_window",label="Properties",pos=(595,30),autosize=True):
            dpg.add_spacer(width=545)
            dpg.add_checkbox(label="Scaling", tag="scaling")
            dpg.add_slider_int(tag="precision",label="Precision",default_value=16,min_value=1,max_value=50)
            dpg.add_combo(label = "Method",
                        tag="method",
                        items=["Gauss Elimination", "Gauss-Jordan", "LU Decomposition", "Gauss-Seidel", "Jacobi-Iteration"],
                        default_value="Gauss Elimination",
                        callback=self.on_method_changed)
            
            with dpg.group(label="LU Decomposition Settings",tag="lu_settings",show=False):
                dpg.add_combo(label = "LU Format",
                        tag="lu_format",
                        items=["Doolittle", "Crout", "Cholesky"],
                        default_value="Doolittle")
                
            with dpg.group(label="Iterative Methods Settings",tag="iter_settings",show=False):
                dpg.add_input_text(label = "Initial Guess",
                        tag="initial_guess",
                        default_value="1,1")
                
                with dpg.tooltip("initial_guess"):
                    dpg.add_text("Comma sperated decimal numbers.\nNumber of elements should match the number of equations.")
                    
                dpg.add_combo(label = "Stopping Condition",
                        tag="stop_condition",
                        items=["Number of Iterations", "Absolute Relative Error"],
                        default_value="Number of Iterations",
                        callback=self.on_stop_condition_changed)
                
                #based on the stopping condition combo, show either a number_of_iterations input or absolute_relative_error input
                dpg.add_input_int(label="Number of Iterations", tag="number_of_iterations",default_value=50,max_value=500,min_value=1,min_clamped=True,max_clamped=True)
                dpg.add_input_float(label="Absolute Relative Error", tag="absolute_relative_error",default_value=0.0001,format="%.6f",min_value=0.000001,min_clamped=True)

                # Initially hide the absolute_relative_error input
                dpg.configure_item("absolute_relative_error", show=False)

    def reset_gui(self,sender, app_data):
        # Destroy all existing windows
        dpg.delete_item("equations_window")
        dpg.delete_item("properties_window")
        # Recreate the windows
        self.create_windows()
    
    def on_stop_condition_changed(self,sender, app_data):
        selected_item = dpg.get_value(sender)
        if selected_item == "Number of Iterations":
            dpg.configure_item("number_of_iterations", show=True)
            dpg.configure_item("absolute_relative_error", show=False)
        elif selected_item == "Absolute Relative Error":
            dpg.configure_item("number_of_iterations", show=False)
            dpg.configure_item("absolute_relative_error", show=True)

    def on_method_changed(self, sender, app_data):
        selected_method = dpg.get_value(sender)
        if selected_method in ["Gauss Elimination", "Gauss-Jordan", "LU Decomposition"]:
            dpg.configure_item("scaling", show=True)
        else:
            dpg.configure_item("scaling", show=False)
            
        if selected_method == "LU Decomposition":
            dpg.configure_item("lu_settings", show=True)
            dpg.configure_item("iter_settings", show=False)
        elif selected_method in ["Gauss-Seidel", "Jacobi-Iteration"]:
            dpg.configure_item("lu_settings", show=False)
            dpg.configure_item("iter_settings", show=True)
        else:
            dpg.configure_item("lu_settings", show=False)
            dpg.configure_item("iter_settings", show=False)
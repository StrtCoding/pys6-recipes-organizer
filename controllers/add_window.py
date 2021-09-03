from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.add_edit_window import AddEditWindow
from views.general_custom_ui import GeneralCustomUi

from database import recipes

import shutil

class AddWindowForm(QWidget, AddEditWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.ui.fill_category_cb()
        self.setWindowFlag(Qt.Window)

        self.add_edit_button.setText("Agregar")
        self.add_edit_button.clicked.connect(self.add_recipe)
        self.select_img_button.clicked.connect(self.select_img)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def add_recipe(self):
        title = self.title_line_edit.text()
        category = self.category_combo_box.currentText()
        url = self.url_line_edit.text()
        budget = self.budget_line_edit.text()
        img_path = self.img_path_to
        ingredients = self.ingredients_text_edit.toPlainText()
        directions = self.directions_text_edit.toPlainText()

        data = (title, category, url, budget, img_path, ingredients, directions)

        if recipes.insert(data):
            self.save_img()
            print("Recipe Added")
            self.clear_inputs()
            self.parent.set_table_data()

    def select_img(self):
        self.img_path_from = QFileDialog.getOpenFileName()[0]
        img_name = self.img_path_from.split("/")[-1]
        self.img_path_to = f"recipe_images\{img_name}"
        self.image_path_line_edit.setText(img_name)

    def save_img(self):
        shutil.copy(self.img_path_from, "recipe_images")
    
    def clear_inputs(self):
        self.title_line_edit.clear()
        self.category_combo_box.clear()
        self.ui.fill_category_cb()
        self.url_line_edit.clear()
        self.budget_line_edit.clear()
        self.image_path_line_edit.clear()
        self.ingredients_text_edit.clear()
        self.directions_text_edit.clear()
   
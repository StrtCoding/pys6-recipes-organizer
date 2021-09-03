from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from views.recipe_details_window import DetailWindow
from views.general_custom_ui import GeneralCustomUi

from database import recipes

class DetailWindowForm(QWidget, DetailWindow):

    def __init__(self, parent=None, recipe_id=None):
        super().__init__(parent)

        self.recipe_id = recipe_id

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fill_widgets()
    
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def fill_widgets(self):
        data = recipes.select_by_id(self.recipe_id)

        title = data[1]
        category = data[2]
        url = data[3]
        budget = data[4]
        img_path = data[5]
        ingredients = data[6]
        directions = data[7]

        self.recipe_title_label.setText(title)
        self.recipe_category_label.setText(category)
        self.ingredients_text_edit.setPlainText(ingredients)
        self.directions_text_edit.setPlainText(directions)
        self.set_recipe_budget(budget)
        self.set_recipe_url(url)
        self.set_recipe_image(img_path)

    def set_recipe_budget(self, budget):
        budget = f"${str(budget)}"
        self.recipe_budget_label.setText(budget)
    
    def set_recipe_url(self, url):
        url = f"<a href={url}>{url}</a>"
        self.recipe_url_label.setOpenExternalLinks(True)
        self.recipe_url_label.setText(url)
    
    def set_recipe_image(self, img_path):
        pix_map = QPixmap(img_path)

        self.recipe_pic_label.setPixmap(pix_map)
        self.recipe_pic_label.setScaledContents(True)

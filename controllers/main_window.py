from views.recipe_details_window import DetailWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

from views.main_window import MainWindow
from controllers.add_window import AddWindowForm
from controllers.edit_window import EditWindowForm
from controllers.recipe_details_window import DetailWindowForm
from views.general_custom_ui import GeneralCustomUi
from views import components

from database import recipes

import os

class MainWindowForm(QWidget, MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        
        self.config_table()
        self.set_table_data()

        self.new_recipe_button.clicked.connect(self.open_add_window)
        self.search_line_edit.returnPressed.connect(self.search)
        self.search_line_edit.textChanged.connect(self.restore_table_data)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def open_add_window(self):
        window = AddWindowForm(self)
        window.show()
    
    def open_edit_window(self, recipe_id):
        window = EditWindowForm(self, recipe_id)
        window.show()
    
    def config_table(self):
        column_labels = ("ID", "IMG", "TITULO", "CATEGORIA", "")
        self.recipes_table.setColumnCount(len(column_labels))
        self.recipes_table.setHorizontalHeaderLabels(column_labels)
        self.recipes_table.setColumnWidth(1, 200)
        self.recipes_table.setColumnWidth(4, 120)
        self.recipes_table.verticalHeader().setDefaultSectionSize(150)
        self.recipes_table.setColumnHidden(0, True)
        self.recipes_table.setSelectionBehavior(QAbstractItemView.SelectRows)
    
    def populate_table(self, data):

        self.recipes_table.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                if index_cell == 1:
                    self.recipes_table.setCellWidget(
                        index_row, index_cell, components.RecipeImg(cell)
                    )
                else:
                    self.recipes_table.setItem(
                        index_row, index_cell, QTableWidgetItem(str(cell))
                    )
            self.recipes_table.setCellWidget(
                index_row, 4, self.build_action_buttons()
            )
    
    def set_table_data(self):
        data = recipes.select_all()
        self.populate_table(data)
    
    def restore_table_data(self):
        param = self.search_line_edit.text()
        if param == "":
            self.set_table_data()
    
    def search(self):
        param = self.search_line_edit.text()
        if param != "":
            data = recipes.select_by_parameter(param)
            self.populate_table(data)
    
    def build_action_buttons(self):
        view_button = components.Button("view", "#17A2B8")
        edit_button = components.Button("edit", "#007BFF")
        delete_button = components.Button("delete", "#DC3545")

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(view_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)

        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)

        view_button.clicked.connect(self.view_recipe)
        edit_button.clicked.connect(self.edit_recipe)
        delete_button.clicked.connect(self.delete_recipe)

        return buttons_frame
    
    def open_detail_window(self, recipe_id):
        window = DetailWindowForm(self, recipe_id)
        window.show()
    
    def view_recipe(self):
        button = self.sender()
        table = self.recipes_table

        if button:
            recipe_id = self.get_recipe_id_from_table(table, button)
            self.open_detail_window(recipe_id)
    
    def edit_recipe(self):
        button = self.sender()
        table = self.recipes_table

        if button:
            recipe_id = self.get_recipe_id_from_table(table, button)
            self.open_edit_window(recipe_id)
    
    def delete_recipe(self):
        button = self.sender()
        table = self.recipes_table

        if button:
            recipe_id = self.get_recipe_id_from_table(table, button)
            data = recipes.select_by_id(recipe_id)

            if recipes.delete(recipe_id):
                self.remove_img(data[5])
                self.set_table_data()
    
    def remove_img(self, img_path):
        os.remove(img_path)
            
    def get_recipe_id_from_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index, 0)
        recipe_id = table.model().data(cell_id_index)
        return recipe_id
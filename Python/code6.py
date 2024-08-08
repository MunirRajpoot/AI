import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Simple Calculator')
        
        # Create the main layout
        self.layout = QVBoxLayout()
        
        # Create the display
        self.result = QLineEdit()
        self.layout.addWidget(self.result)
        
        # Create the buttons
        self.create_buttons()
        
        # Set the layout
        self.setLayout(self.layout)
    
    def create_buttons(self):
        buttons = [
            ('7', self.add_to_expression), ('8', self.add_to_expression), ('9', self.add_to_expression), ('/', self.add_to_expression),
            ('4', self.add_to_expression), ('5', self.add_to_expression), ('6', self.add_to_expression), ('*', self.add_to_expression),
            ('1', self.add_to_expression), ('2', self.add_to_expression), ('3', self.add_to_expression), ('-', self.add_to_expression),
            ('0', self.add_to_expression), ('.', self.add_to_expression), ('+', self.add_to_expression), ('=', self.calculate_result),
            ('C', self.clear_expression)
        ]
        
        for i in range(0, len(buttons), 4):
            row = QHBoxLayout()
            for j in range(4):
                if i + j < len(buttons):
                    button_text, button_action = buttons[i + j]
                    button = QPushButton(button_text)
                    button.clicked.connect(button_action)
                    row.addWidget(button)
            self.layout.addLayout(row)
    
    def add_to_expression(self):
        button = self.sender()
        current_text = self.result.text()
        new_text = current_text + button.text()
        self.result.setText(new_text)
    
    def calculate_result(self):
        try:
            result = eval(self.result.text())
            self.result.setText(str(result))
        except Exception as e:
            self.result.setText('Error')
    
    def clear_expression(self):
        self.result.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = SimpleCalculator()
    calculator.show()
    sys.exit(app.exec_())

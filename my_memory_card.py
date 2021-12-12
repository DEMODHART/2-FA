#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton,QPushButton, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QButtonGroup
from random import *
win = False
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("2-FA")
main_win.resize(400, 200)

class Question():
    def __init__(self, what_question, right_ans, wrong_ans1, wrong_ans2, wrong_ans3):
        self.what_question = what_question
        self.right_ans = right_ans
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
question_list = []
def set_2FA():
    for i in range(4):
        theme_of_que = input("Введите вопрос(осталось - "+ str(4 - i) + "):")
        answers = input("Введите ответы через пробел:").split(" ")
        question_list.append(Question(theme_of_que, answers[0],answers[1],answers[2],answers[3]))

question = QLabel("")
question.setText("Самый сложный вопрос в мире!")
button = QPushButton("Ответить")
radio_group = QGroupBox("Варианты ответов")
result_ans = QLabel("")
win_or_not = QLabel("Правильно/Неправильно")
result_box = QGroupBox("Результат теста")
ans1 = QRadioButton("")
ans2 = QRadioButton("")
ans3 = QRadioButton("")
ans4 = QRadioButton("")
answer_buttons = [ans1, ans2, ans3, ans4]
radio_box = QButtonGroup()
radio_box.addButton(ans1)
radio_box.addButton(ans2)
radio_box.addButton(ans3)
radio_box.addButton(ans4)
right_ans = "ответ1"
wrong_ans1 = "ответ2"
wrong_ans2 = "ответ3"
wrong_ans3 = "ответ4"
what_question = "вопрос"
def next_question():
    randomNum = randint(0, len(question_list) - 1)
    q = question_list[randomNum]
    question_list.remove(q)
    ask(q)
def show_question():
    radio_group.show()
    result_box.hide()
    button.setText("Ответить")
    radio_box.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    radio_box.setExclusive(True)
def ask(q: Question):
    shuffle(answer_buttons)
    answer_buttons[0].setText(q.right_ans)
    answer_buttons[1].setText(q.wrong_ans1)
    answer_buttons[2].setText(q.wrong_ans2)
    answer_buttons[3].setText(q.wrong_ans3)
    question.setText(q.what_question)    
    show_question()  
def show_correct(res):
    result_ans.setText(res)
    radio_group.hide()
    result_box.show()
    button.setText("Следующий вопрос")
    main_win.total += 1
def check_ans():
    if answer_buttons[0].isChecked():
        main_win.score += 1
        show_correct("Правильный ответ")
    elif answer_buttons[1].isChecked() or answer_buttons[2].isChecked() or answer_buttons[3].isChecked(): 
        show_correct("Неправильный ответ")
def test_while():
    if "Ответить" == button.text():
        check_ans()
    else:
        if main_win.total < 4:
            next_question()
        else:
            if (main_win.score / main_win.total) * 100 > 75:
                print("Вход выполнен")
            else:
                print("Вход воспрещён")
v_boxlay1 = QVBoxLayout()
v_boxlay2 = QVBoxLayout()
h_boxlay = QHBoxLayout()
v_boxlay1.addWidget(answer_buttons[0])
v_boxlay1.addWidget(answer_buttons[1])
v_boxlay2.addWidget(answer_buttons[2])
v_boxlay2.addWidget(answer_buttons[3])
h_boxlay.addLayout(v_boxlay1)
h_boxlay.addLayout(v_boxlay2)
h_boxlay.setSpacing(15)
radio_group.setLayout(h_boxlay)

v_rboxlay = QVBoxLayout()
h_rboxlay = QHBoxLayout()
v_rboxlay.addWidget(win_or_not, alignment = (Qt.AlignLeft | Qt.AlignTop))
v_rboxlay.addWidget(result_ans, alignment = Qt.AlignHCenter)
h_rboxlay.addLayout(v_rboxlay)
result_box.setLayout(h_rboxlay)

mainv_lay = QVBoxLayout()
h_lay1 = QHBoxLayout()
h_lay2 = QHBoxLayout()
h_lay3 = QHBoxLayout()

h_lay1.addWidget(question, alignment=Qt.AlignHCenter)
h_lay2.addStretch(1)
h_lay2.addWidget(radio_group, stretch= 5)
h_lay2.addWidget(result_box, stretch= 5)
result_box.hide()
h_lay2.addStretch(1)
h_lay3.addStretch(1)
h_lay3.addWidget(button, stretch= 2)
h_lay3.addStretch(1)


mainv_lay.addLayout(h_lay1)
mainv_lay.addLayout(h_lay2)
mainv_lay.addLayout(h_lay3)
mainv_lay.setSpacing(20)

main_win.score = 0
main_win.total = 0

set_2FA()
next_question()
button.clicked.connect(test_while)
main_win.setLayout(mainv_lay)
main_win.show()
app.exec_()

#https://docs.google.com/presentation/d/1eV5RrlSukMcAPSzNVK92rirtithjFmTAJjD-bKXzmeg/edit?usp=sharing
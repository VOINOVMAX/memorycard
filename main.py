from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import randint

app = QApplication([])
class Question():
    def __init__(
    self, question, right_answer, wrong1, wrong2, wrong3):
        self.question  = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Год крещения руси?', '988', '986', '980', '970'))
question_list.append(Question('Столица США', 'Вашингтон', 'Чикаго', 'Нью-Йорк', 'Лос-Анджелес'))
question_list.append(Question('Гос. язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Question('какого цвета нет нв флаге России?', 'Зеленый', 'Красный', 'Синий', 'Белый'))
question_list.append(Question('Год начала второй меровй?', '1939', '1941', '1938', '1945'))
window = QWidget()
window.setWindowTitle('Memory Card')
btn_ok = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox('Вырианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следущий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Ответить' == btn_ok.text():
        show_result()
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')

def next_question():
    window.total += 1    
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    if window.total != 0:
        print(window.score/window.total * 100)
    ask(q)
    
    
def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.score = 0
window.total = -1
btn_ok.clicked.connect(click_OK)
next_question()
window.setLayout(layout_card)
window.show()
app.exec()


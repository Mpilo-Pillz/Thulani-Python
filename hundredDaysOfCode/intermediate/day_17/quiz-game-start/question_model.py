class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

new_q = Question("Test Modal", "False")
print(new_q.text)

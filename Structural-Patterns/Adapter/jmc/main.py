class QuestionAnswering:

    def answer(self):
        return "정답은 A입니다."
    

class EnglishChatbot:

    def english_answer(self):
        return "the answer is A"
    

class Adapter(QuestionAnswering, EnglishChatbot):

    def answer(self):
        return f"Adapter: (translated) {self.english_answer()}"
    

def client_code(target: QuestionAnswering):

    print(target.answer())


qa = QuestionAnswering()
adapter = Adapter()

client_code(adapter)
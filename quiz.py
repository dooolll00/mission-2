"""퀴즈 한 개를 표현하는 Quiz 클래스."""


class Quiz:
    """문제, 선택지 4개, 정답 번호(1~4)를 가지는 퀴즈 한 개."""

    def __init__(self, question, choices, answer, quiz_id=None):
        self.quiz_id = quiz_id
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 사이의 정답 번호

    def display(self, number):
        """문제와 선택지를 화면에 출력한다."""
        print(f"[문제 {number}] {self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"    {i}. {choice}")

    def check(self, user_answer):
        """사용자가 입력한 번호가 정답인지 확인한다."""
        return user_answer == self.answer


def default_quizzes():
    """저장 파일이 없을 때 사용하는 기본 파이썬 퀴즈 5개."""
    return [
        Quiz(
            "파이썬에서 리스트의 맨 끝에 값을 추가할 때 사용하는 메서드는?",
            ["append()", "push()", "add()", "insert_last()"],
            1,
        ),
        Quiz(
            "파이썬에서 한 줄 주석을 작성할 때 사용하는 기호는?",
            ["//", "<!-- -->", "#", "/* */"],
            3,
        ),
        Quiz(
            "딕셔너리에서 키와 값을 함께 반복할 때 사용하는 메서드는?",
            ["keys()", "values()", "items()", "pairs()"],
            3,
        ),
        Quiz(
            "파이썬에서 예외 처리를 시작할 때 사용하는 키워드는?",
            ["catch", "try", "except", "error"],
            2,
        ),
        Quiz(
            "함수에서 값을 돌려줄 때 사용하는 키워드는 무엇일까요?",
            ["return", "yield", "print", "break"],
            1,
        ),
    ]
    

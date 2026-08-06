"""퀴즈 한 개를 표현하는 Quiz 클래스."""


class Quiz:
    """문제, 선택지 4개, 정답 번호(1~4)를 가지는 퀴즈 한 개."""

    def __init__(self, question, choices, answer, quiz_id=None):
        self.quiz_id = quiz_id
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, number):
        """문제와 선택지를 화면에 출력한다."""
        print(f"[문제 {number}] {self.question}")

        for i, choice in enumerate(self.choices, start=1):
            print(f"    {i}. {choice}")

    def check(self, user_answer):
        """사용자가 입력한 번호가 정답인지 확인한다."""
        return user_answer == self.answer

    @property
    def options(self):
        """기존 options 이름을 쓰는 코드와 호환하기 위한 별칭."""
        return self.choices

    @property
    def correct_answer(self):
        """기존 correct_answer 이름을 쓰는 코드와 호환하기 위한 별칭."""
        return self.answer

    def check_answer(self, user_answer):
        """기존 check_answer 이름을 쓰는 코드와 호환하기 위한 별칭."""
        return self.check(user_answer)

    def to_dict(self):
        """JSON 저장을 위해 Quiz 객체를 딕셔너리로 변환한다."""
        return {
            "id": self.quiz_id,
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """JSON에서 읽은 딕셔너리로 Quiz 객체를 생성한다."""
        return cls(
            question=str(data["question"]),
            choices=[str(choice) for choice in data["choices"]],
            answer=int(data["answer"]),
            quiz_id=data.get("id"),
        )


def default_quizzes():
    """저장 파일이 없을 때 사용하는 기본 파이썬 퀴즈 5개."""
    return [
        Quiz(
            "파이썬에서 리스트의 맨 끝에 값을 추가할 때 사용하는 메서드는?",
            ["append()", "push()", "add()", "insert_last()"],
            1,
            quiz_id=1,
        ),
        Quiz(
            "파이썬에서 한 줄 주석을 작성할 때 사용하는 기호는?",
            ["//", "<!-- -->", "#", "/* */"],
            3,
            quiz_id=2,
        ),
        Quiz(
            "딕셔너리에서 키와 값을 함께 반복할 때 사용하는 메서드는?",
            ["keys()", "values()", "items()", "pairs()"],
            3,
            quiz_id=3,
        ),
        Quiz(
            "파이썬에서 예외 처리를 시작할 때 사용하는 키워드는?",
            ["catch", "try", "except", "error"],
            2,
            quiz_id=4,
        ),
        Quiz(
            "함수에서 값을 돌려줄 때 사용하는 키워드는 무엇일까요?",
            ["return", "yield", "print", "break"],
            1,
            quiz_id=5,
        ),
    ]
    

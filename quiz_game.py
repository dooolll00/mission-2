"""게임 전체를 관리하는 QuizGame 클래스."""

import os
import random

from quiz import Quiz, default_quizzes

STATE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "state.json",
)


class QuizGame:
    """메뉴를 보여주고 사용자가 선택한 기능을 실행하는 게임 관리 클래스."""

    def __init__(self, state_file: str = STATE_FILE):
        self.state_file = state_file
        self.quizzes = default_quizzes()
        self.best_score = None

    def show_menu(self) -> None:
        """사용자가 선택할 수 있는 메인 메뉴를 출력한다."""
        print()
        print("=" * 40)
        print("          🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("        1. 퀴즈 풀기")
        print("        2. 퀴즈 추가")
        print("        3. 퀴즈 목록")
        print("        4. 점수 확인")
        print("        5. 종료")
        print("=" * 40)

    def read_int(
        self,
        prompt: str,
        min_value: int,
        max_value: int,
    ) -> int | None:
        """숫자 입력을 검사하고 올바른 정수를 반환한다."""
        while True:
            try:
                raw = input(prompt).strip()
            except (KeyboardInterrupt, EOFError):
                print(
                    "\n\n⚠️ 입력이 중단되었습니다. "
                    "현재 데이터를 저장하고 안전하게 종료합니다."
                )
                self.save_state()
                return None

            if raw == "":
                print(
                    f"⚠️ 아무것도 입력되지 않았습니다. "
                    f"{min_value}-{max_value} 사이의 숫자를 입력하세요."
                )
                continue

            try:
                value = int(raw)
            except ValueError:
                print(
                    f"⚠️ 잘못된 입력입니다. "
                    f"{min_value}-{max_value} 사이의 숫자를 입력하세요."
                )
                continue

            if not min_value <= value <= max_value:
                print(
                    f"⚠️ 잘못된 입력입니다. "
                    f"{min_value}-{max_value} 사이의 숫자를 입력하세요."
                )
                continue

            return value

    def read_text(self, prompt: str) -> str | None:
        """문자 입력을 검사하고 올바른 문자열을 반환한다."""
        while True:
            try:
                raw = input(prompt).strip()
            except (KeyboardInterrupt, EOFError):
                print(
                    "\n\n⚠️ 입력이 중단되었습니다. "
                    "현재 데이터를 저장하고 안전하게 종료합니다."
                )
                self.save_state()
                return None

            if not raw:
                print("⚠️ 빈 입력은 사용할 수 없습니다. 다시 입력하세요.")
                continue

            try:
                raw.encode("utf-8")
            except UnicodeEncodeError:
                print(
                    "⚠️ 인식할 수 없는 문자가 포함되어 있습니다. "
                    "다시 입력하세요."
                )
                continue

            return raw

    def play_quiz(self) -> None:
        """퀴즈를 랜덤 순서로 출제하고 채점한다."""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        total = len(self.quizzes)
        correct = 0
        shuffled = random.sample(self.quizzes, total)

        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")
        print("-" * 40)

        for number, quiz in enumerate(shuffled, start=1):
            quiz.display(number)

            user_answer = self.read_int("    정답 입력: ", 1, 4)
            if user_answer is None:
                return

            if quiz.check(user_answer):
                correct += 1
                print("✅ 정답입니다!")
            else:
                correct_choice = quiz.choices[quiz.answer - 1]
                print(
                    f"❌ 오답입니다! "
                    f"(정답: {quiz.answer}. {correct_choice})"
                )

            print("-" * 40)

        score = round(correct / total * 100)

        print("=" * 40)
        print(
            f"🏆 결과: {total}문제 중 "
            f"{correct}문제 정답! ({score}점)"
        )

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")

        self.save_state()
        print("=" * 40)

    def add_quiz(self) -> None:
        """문제, 선택지 4개, 정답 번호를 입력받아 퀴즈를 추가한다."""
        print("\n📌 새로운 퀴즈를 추가합니다.")

        question = self.read_text("문제를 입력하세요: ")
        if question is None:
            return

        choices = []

        for i in range(1, 5):
            choice = self.read_text(f"선택지 {i}: ")
            if choice is None:
                return
            choices.append(choice)

        answer = self.read_int("정답 번호 (1-4): ", 1, 4)
        if answer is None:
            return

        quiz_id = max(
            (
                quiz.quiz_id
                for quiz in self.quizzes
                if quiz.quiz_id is not None
            ),
            default=0,
        ) + 1

        new_quiz = Quiz(
            question,
            choices,
            answer,
            quiz_id=quiz_id,
        )

        self.quizzes.append(new_quiz)
        self.save_state()

        print("\n✅ 퀴즈가 추가되었습니다!")

    def list_quizzes(self) -> None:
        """등록된 퀴즈 목록을 번호와 함께 출력한다."""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

        print("-" * 40)

    def show_score(self) -> None:
        """최고 점수를 출력한다. 아직 퀴즈를 풀지 않았으면 안내한다."""
        if self.best_score is None:
            print(
                "⚠️ 아직 퀴즈를 푼 기록이 없습니다. "
                "먼저 퀴즈를 풀어보세요!"
            )
            return

        print(f"\n🏆 최고 점수: {self.best_score}점")

    def save_state(self) -> None:
        """파일 저장 기능은 이후 단계에서 구현한다."""
        pass

    def run(self) -> None:
        """메인 메뉴를 반복해서 실행한다."""
        while True:
            self.show_menu()
            choice = self.read_int("    선택: ", 1, 5)

            if choice is None:
                break

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            else:
                print("👋 게임을 종료합니다.")
                break


if __name__ == "__main__":
    QuizGame().run()
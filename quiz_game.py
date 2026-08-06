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
                print("🚧 퀴즈 추가 기능은 준비 중입니다.")
            elif choice == 3:
                print("🚧 퀴즈 목록 기능은 준비 중입니다.")
            elif choice == 4:
                print("🚧 점수 확인 기능은 준비 중입니다.")
            else:
                print("👋 게임을 종료합니다.")
                break


if __name__ == "__main__":
    QuizGame().run()
"""게임 전체를 관리하는 QuizGame 클래스."""

import os

from quiz import Quiz, default_quizzes

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")


class QuizGame:
    """메뉴를 보여주고 사용자가 선택한 기능을 실행하는 게임 관리 클래스."""

    def __init__(self, state_file: str = STATE_FILE):
        self.state_file = state_file
        self.quizzes = default_quizzes()
        self.best_score = None  # 아직 퀴즈를 풀지 않았으면 None

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

    def read_int(self, prompt: str, min_value: int, max_value: int) -> int | None:
        """숫자 입력 공통 처리: 공백 제거, 빈 입력/숫자 아님/범위 밖이면 재입력."""
        while True:
            try:
                raw = input(prompt).strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\n⚠️ 입력이 중단되었습니다. 현재 데이터를 저장하고 안전하게 종료합니다.")
                self.save_state()
                return None

            if raw == "":
                print(f"⚠️ 아무것도 입력되지 않았습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue
            try:
                value = int(raw)
            except ValueError:
                print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue
            if not min_value <= value <= max_value:
                print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue
            return value

    def save_state(self) -> None:
        """파일 저장 기능은 이후 단계에서 구현한다."""
        pass

    def run(self) -> None:
        """메인 루프: 메뉴 출력 → 번호 선택 → 기능 실행."""
        while True:
            self.show_menu()
            choice = self.read_int("    선택: ", 1, 5)
            if choice is None:
                break
            if choice == 1:
                print("🚧 퀴즈 풀기 기능은 준비 중입니다.")
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
 
"""퀴즈 게임 진입점. 실행: python main.py"""

from quiz_game import QuizGame


def main() -> None:
    """QuizGame을 실행하고 입력 중단 시 데이터를 저장한 뒤 종료한다."""
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n⚠️ 입력이 중단되었습니다. 데이터를 저장하고 종료합니다.")
        game.save_state()


if __name__ == "__main__":
    main()
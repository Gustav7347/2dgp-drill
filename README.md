# 2DGP 실습

캐릭터가 원, 사각형, 삼각형을 차례로 한 바퀴씩 이동하고 반복합니다.

- `character_draws.py`: 단계별로 구현한 버전
- `character_draws_ai.py`: AI로 작성한 버전
- `character.png`: 수업 저장소에서 제공한 이미지

## 실행

Python 3.8 이상에서 다음 명령으로 실행합니다.

```text
python -m pip install -r requirements.txt
python character_draws.py
python character_draws_ai.py
```

두 프로그램은 각각 실행합니다. 이미지는 코드와 같은 위치에 둡니다.
터미널에서 `Ctrl+C`, VS Code 디버그 실행에서는 `Shift+F5`로 중지합니다.
입력 이벤트 처리를 넣지 않아 창의 닫기 버튼은 종료용으로 사용하지 않습니다.

한 순환만 확인하려면 다음처럼 실행합니다.

```text
python character_draws.py --cycles 1
python character_draws_ai.py --cycles 1
```

원의 중심은 `(400, 300)`, 반지름은 `200`입니다.
사각형은 `(50, 550)`에서 시작해 오른쪽, 아래, 왼쪽, 위 순서로 이동합니다.
삼각형은 `(100, 100)`, `(700, 100)`, `(400, 500)`을 지납니다.

참고: [수업 저장소](https://github.com/unreal-class/2026-2DGP)의 LEC06 점진적 개발 실습.

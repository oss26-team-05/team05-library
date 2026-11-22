# ClearVision (`team05`)

저조도(야간), 고감도 센서 노이즈, 안개 등 악천후 환경에서 촬영된 이미지의 밝기와 명암 대비를 보정하고 시인성을 복원하는 Python 이미지 전처리 라이브러리입니다.

## 1. What it does

야간 도로 주행 데이터를 수집하는 연구원이나 저조도·안개 환경의 CCTV·블랙박스 이미지를 분석하는 개발자는 조도 부족, 센서 노이즈, 대기 산란으로 인해 객체 식별률이 떨어지는 문제를 겪습니다. ClearVision(`team05`)은 비선형 감마 보정(`adjust_gamma`), CLAHE 국소 대비 개선(`apply_clahe`), 양방향 필터 노이즈 제거(`denoise_bilateral`), 다크 채널 기반 안개 제거(`dehaze_dark_channel`) 파이프라인을 제공하여 원본 해상도를 유지한 채 가볍고 일관된 기준으로 이미지 시인성을 복원합니다.

## 2. Installation

TestPyPI를 통해 테스트 배포 버전을 설치할 수 있습니다:

```bash
pip install -i [https://test.pypi.org/simple/](https://test.pypi.org/simple/) --extra-index-url [https://pypi.org/simple/](https://pypi.org/simple/) team05==0.1.0
```

*(정식 PyPI 릴리즈 이후에는 `pip install team05`로 설치할 수 있습니다.)*

## 3. Quick start

```python
from team05 import adjust_gamma

# 어두운 야간 이미지의 감마 값을 보정하여 암부 디테일 복원
restored_img = adjust_gamma("samples/night.jpg", gamma=0.5)
restored_img.save("samples/night_restored.jpg")
```

## 4. Dependencies

- Pillow>=10 (MIT-CMU License) – 이미지 파일 입출력 및 포맷 변환
- numpy>=1.26 (BSD 3-Clause License) – 픽셀 배열 연산 및 수치 처리

## 5. Tests

TODO

## 6. Documentation
- Documentation Site: [https://oss26-team-05.github.io/team05-library/](https://oss26-team-05.github.io/team05-library/)

- API Reference: [https://oss26-team-05.github.io/team05-library/api/](https://oss26-team-05.github.io/team05-library/api/)

## 7. Release

TODO

## 8. Team

- **이승준** (`@seungjun0307`) — 팀장, 아키텍처 설계 및 패키징/배포 총괄
- **정성태**('@asnm0926-wq')-전처리 모듈 개발 및 품질 검즘
AI 사용 고지: 모든 pull request의 ##ai use 섹션에 사용 도구, 대상 파일, 활용 방식 및 직접 검증 내역을 명시합니다
- 정준오 (@Dahlia-ui) - 전처리 모듈 개발 및 테스트
  협업 규칙: [docs/team-rules.md](docs/team-rules.md)
## 9. License

이 프로젝트는 **MIT License**를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.

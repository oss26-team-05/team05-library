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

<!-- 김원 작성 구역: Pillow, numpy 라이브러리와 라이선스, 역할 작성 -->

## 5. Tests

TODO

## 6. Documentation

<!-- 배건영 작성 구역: GitHub Pages 문서 사이트 주소와 API 페이지 링크 작성 -->

## 7. Release

TODO

## 8. Team

- **이승준** (`@seungjun0307`) — 팀장, 아키텍처 설계 및 패키징/배포 총괄
<!-- 정준오 작성 구역: 본인 이름/GitHub ID 및 docs/team-rules.md 링크 작성 -->
<!-- 정성태 작성 구역: 본인 이름/GitHub ID 및 AI 사용 고지 규칙 한 줄 작성 -->

## 9. License

이 프로젝트는 **MIT License**를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.
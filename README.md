# coala

## 개요

Coala 연구소에 오신 것을 환영합니다! 당신은 이제 연구소의 일원으로서 동료 연구원들과 협력하여 새로운 원소를 합성하고 기록하는 임무를 맡게 되었습니다.

- **기본 원소:** 공기(AIR), 흙(EARTH), 불(FIRE), 물(WATER)의 4가지 원소가 기초 자산으로 제공됩니다.
- **원소 합성:** 기본 원소들을 정교하게 조합하여 세상에 없던 복합 원소들을 만들어낼 수 있습니다.

## 준비 과정

> [uv](https://docs.astral.sh/uv/) 설치 및 환경 구성

`uv`를 사용하여 프로젝트의 의존성을 빠르고 안전하게 관리합니다.

```bash
# uv 설치
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# 프로젝트 의존성 동기화 및 가상환경 생성
$ uv sync

# 코드 품질 관리를 위한 pre-commit 설정
$ uv run pre-commit install

# 기본 테스트 환경 작동 여부 확인
$ uv run pytest
```

> [GH](https://cli.github.com/) (선택 사항)

명령줄에서 GitHub 작업을 효율적으로 처리하려면 `gh`를 활용하세요.

```bash
# 설치 (macOS 기준)
$ brew install gh

# GitHub 계정 인증
$ gh auth login
```

**저장소 포크 및 로컬 복제**
```bash
# 연구용 개인 저장소 생성 및 복제
$ gh repo fork https://github.com/[REPO_OWNER]/coala.git --clone

$ cd coala
```

## 원소 합성 실험

새로운 원소는 테스트 코드를 작성하고 실행하는 과정을 통해 합성할 수 있습니다.

```python
@pytest.mark.asyncio
async def test_fusing_fire_earth(tutorial_lab: Lab):
    # 불과 흙을 합성했을 때의 예상 결과를 기술합니다.
    assert await tutorial_lab.fuse("fire", "earth") == "???"
```

작성한 실험(테스트)은 다음과 같이 실행하여 결과를 확인할 수 있습니다.

```bash
# -k: 특정 키워드가 포함된 실험만 선택 실행
# -s: 실험 과정 중의 출력 내용을 실시간으로 확인
# -v: 실험 결과에 대한 상세 보고서 출력
$ uv run pytest -k "tutorial and fire and water" -s -v
```

## 커밋 메시지 규약

합성에 성공한 원소를 저장소에 기록할 때는 아래의 형식을 준수해 주세요.

```
discover([lab 이름]): [발견한 원소 이름]

- 합성 과정 및 특이사항 기술
```

## 레시피 공유

합성법(Recipe)은 `src/coala/(lab_이름)/*.yaml` 파일 형태로 작성하여 Pull Request를 통해 공유합니다.

```yaml
# steam.yaml
ingredients:
  - "fire"
  - "water"
```

## 연구실 검증

해당 연구실(Lab)의 모든 레시피가 올바르게 구성되었는지 확인하려면 다음 명령을 실행합니다.

```bash
$ uv run pytest -k "tutorial_lab" -s -v
```

## 연구 목표

- **최종 목표:** 주어진 연구실에서 지정된 목표 원소를 합성할 때까지 끊임없이 실험을 반복하세요!
- **목표 원소:** 각 연구실(Lab)마다 상이하며, 참여 인원과 난이도에 따라 조정됩니다.

### 단계별 가이드

1. **팀 빌딩:** 동료들과 협의하여 사용할 연구실(Lab) 이름을 확정합니다.
2. **사전 학습:** 연구실 PR이 생성되기 전까지 튜토리얼을 통해 합성 시스템을 숙지합니다.
3. **연구 개시:** 생성된 연구실의 목표를 확인하고 합성을 시작합니다.
4. **성과 보고:** 목표 원소 합성에 성공하면 패치를 제출하여 성과를 공유합니다.

## 운영 규칙

- **단일 원소 원칙:** 하나의 변경 리스트(CL)에는 단 하나의 원소만 담아야 합니다. (새로운 원소의 가치를 존중합니다.)
- **상호 리뷰:** 최소 1명 이상의 동료 검토가 필수이며, 스스로 승인(Self-merge)하지 않습니다.
- **긴급 승인:** 단일 원소가 포함된 CL에 한해 연구 관리자에게 즉시 승인을 요청할 수 있습니다 (최대 3회).
- **검증 기반:** 모든 합성은 스크립트가 아닌 테스트 코드를 통해 증명되어야 하며, 통과된 테스트만 제출 가능합니다.

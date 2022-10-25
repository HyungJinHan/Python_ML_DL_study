# 1. Keggle 진행 방법

## 파일 관리

### 버전 관리

- 분류형과 회귀형을 나눠서 관리

- 점수 별로의 모델을 관리하여 최적의 값을 하나씩 찾는 방식으로 진행
  - ex) `model01_CLA_80`
    - 모델 01번이며 분류형 모델, 점수는 80점
  - ex) `model01_REG_91`
    - 모델 01번이며 회귀형 모델, 점수는 91점
<br><br>
---
<br><br>
# 2. Description of fnlwgt (final weight)

## 개인 수익 예측 모델 (분류 모델)

he weights on the CPS files are controlled to independent estimates of the
civilian noninstitutional population of the US. These are prepared monthly
for us by Population Division here at the Census Bureau. We use 3 sets of
controls.<br><br>
These are:

1.  A single cell estimate of the population 16+ for each state.
    - 각 주에 대한 16세 이상의 인구에 대한 단일 셀 추정치<br><br>
2.  Controls for Hispanic Origin by age and sex.
    - 연령 및 성별에 따른 히스패닉계 통제<br><br>
3.  Controls by Race, age and sex.
    - 인종, 연령 및 성별에 따른 통제<br><br>

# File descriptions

- `train.csv` - 트레이닝 셋<br><br>
- `test.csv` - 테스트 셋<br><br>
- `sampleSubmission.csv` - 케글 점수 체크용 정답 데이터 셋<br><br>

# Goal

사람별로 income을 예측하는것이 여러분의 목표입니다.<br>
50k달러 초과면 1, 50k 달러 이하는 0입니다.<br><br>

# Attribute information

- `age` : 나이<br><br>

- `workclass` - 직업군
  - Private : 비공개
  - Self-emp-not-inc : 법인이 없는 개인사업가
  - Self-emp-inc : 자영업
  - Federal-gov : 연방 정부
  - Local-gov : 지방 정부
  - State-gov : 주정부
  - Without-pay : 무급
  - Never-worked : 백수<br><br>
  
- `fnlwgt` : 데이터의 각 행이 나타내는 (추정) 사람 수.<br><br>

- `education` - 학력
  - Bachelors : 학사
  - Some-college : 대학 졸업
  - 11th : 11년 공부
  - HS-grad : 고졸
  - Prof-school : 전문학교
  - Assoc-acdm : 연합학원
  - Assoc-voc
  - 9th : 9년 공부
  - 7th-8th : 7 ~ 8년 공부
  - 12th : 12년 공부
  - Masters1st-4th : 1 ~ 4년 공부한 석사
  - 10th : 10년 공부
  - Doctorate : 박사
  - 5th-6th : 5 ~ 6년 공부
  - Preschool : 유졸<br><br>
  
- `education-num` : 학력에 따른 번호 (점수 개념)<br><br>

- `marital-status` - 혼인 상태
  - Married-civ-spouse : 기혼
  - Divorced : 이혼
  - Never-married : 비혼
  - Separated : 분가
  - Widowed : 과부
  - Married-spouse-absent : 직업상의 이유로 별거
  - Married-AF-spouse : 배우자가 군인<br><br>
  
  
- `occupation` - 직업
  - Tech-support : 기술 지원
  - Craft-repair : 기술 수리
  - Other-service : 기타 서비스
  - Sales : 판매원
  - Exec-managerial : 부장급
  - Prof-specialty : 전문직
  - Handlers-cleaners : 청소부
  - Machine-op-inspct : 기계 작동 점검원
  - Adm-clerical : MD 보조 사무직
  - Farming-fishing : 농 / 어부
  - Transport-moving : 운송업
  - Priv-house-serv : 개인 주택 서비스업
  - Protective-serv : 보안 서비스업
  - Armed-Forces : 군인<br><br>
  
- `relationship` - 관계
  - Wife : 아내
  - Own-child : 자녀
  - Husband : 남편
  - Not-in-family : 가족 없음
  - Other-relative : 기타 관계
  - Unmarried : 비혼<br><br>
  
- `race` - 인종
  - White : 백인
  - Asian-Pac-Islander : 아시안-태평양-아일랜드계
  - Amer-Indian-Eskimo : 아메리카-인디안-에스키모계
  - Other : 기타
  - Black : 흑인<br><br>
  
- `sex` - 성별
  - Female
  - Male<br><br>
  
- `capital-gain` - 자본 이익
  - 수치로 표시<br><br>
  
- `capital-loss` - 자본 손실
  - 수치로 표시<br><br>
  
- `hours-per-week` - 주당 시간
  - 수치로 표시<br><br>

- `native-country` - 국가 (내용은 국가명)
  - United-States
  - Cambodia
  - England
  - Puerto-Rico
  - Canada, Germany
  - Outlying-US(Guam-USVI-etc)
  - India, Japan
  - Greece
  - South
  - China
  - Cuba
  - Iran
  - Honduras
  - Philippines
  - Italy
  - Poland
  - Jamaica
  - Vietnam
  - Mexico
  - Portugal
  - Ireland
  - France
  - Dominican-Republic
  - Laos
  - Ecuador
  - Taiwan
  - Haiti
  - Columbia
  - Hungary
  - Guatemala
  - Nicaragua
  - Scotland
  - Thailand
  - Yugoslavia
  - El-Salvador
  - Trinadad&Tobago
  - Peru
  - Hong
  - Holand-Netherlands<br><br>

---
<br><br>
# 3. Acknowledgements

이 데이터는 인터넷 사이트를 통해 직접 수집된 데이터입니다.<br>
ML을 이용해 집 가격을 예측하는 모델을 완성해보세요.<br><br>

## 주택 가격 예측 모델 (회귀 모델)<br><br>

# File descriptions

- `train.csv` - 트레이닝 셋<br><br>
- `test.csv` - 테스트 셋<br><br>
- `sampleSubmission.csv` - 케글 점수 체크용 정답 데이터 셋<br><br>

# Data fields

- `ID` - 각 집의 고유한 번호<br><br>
- `ADDRESS` - 집의 주소<br><br>
- `SUBURB` - 동네 이름<br><br>
- `PRICE` - 가격<br><br>
- `BEDROOMS` - 침실의 갯수<br><br>
- `BATHROOMS` - 욕실의 갯수<br><br>
- `GARAGE` - 차고의 수<br><br>
- `LAND_AREA` - 토지 면적<br><br>
- `FLOOR_AREA` - 건물 면적<br><br>
- `BUILD_YEAR` - 건축년도<br><br>
- `CBD_DIST` - Central business district까지의 거리<br><br>
- `NEAREST_STN` - 근처 역 정보<br><br>
- `NEAREST_STN_DIST` - 근처 역까지 거리<br><br>
- `DATE_SOLD` - 판매된 날짜<br><br>
- `POSTCODE` - 우편번호<br><br>
- `LATITUDE` - 위도<br><br>
- `LONGITUDE` - 경도<br><br>
- `NEAREST_SCH` - 근교의 학교<br><br>
- `NEAREST_SCH_DIST` - 근교의 학교까지의 거리<br><br>
- `NEAREST_SCH_RANK` - 근교의 학교까지의 랭킹<br><br>

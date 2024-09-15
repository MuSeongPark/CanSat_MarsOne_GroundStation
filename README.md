# Ground Station for CanSat Competition Korea 2022
## 1. 캔 위성 경연대회 소개
<p align="center"><a href="https://cansat.kaist.ac.kr/"><img src="images\CanSatKorea.jpg"></a></p>
&nbsp; 해당 깃헙 프로젝트는 인공위성 연구소, 과학기술정보통신부, 한국항공우주연구원등이 공동으로 주최하는 <br> 캔 위성 경연대회를 위한 지상관제 시스템 프로젝트입니다.<br>
2022년도 경연대회에 참가한 ACT팀의 지상관제 시스템입니다.

## 2. 사용 패키지
- numpy==1.22.4
- PyQt5==5.15.6
- PyQt5-Qt5==5.15.2
- PyQt5-sip==12.10.1
- pyqtgraph==0.12.4
- pyserial==3.5
- pandas==1.2.3
- Jinja2==3.1.2
- folium==0.12.1.post1
- selenium==4.3.0

## 3. 패키지 설치

``` bash
pip install -r requirements.txt
```

## 4. 관제 시스템 기능 소개
<p align="center"><img src="images\UI.png"></p>

### (a) 데이터 저장 및 관리
데이터 수신을 시작한 이후, Start 버튼을 누른 시점부터 Stop 버튼을 누른 시점까지의 데이터를 excel 파일로 저장하는 기능이다.<br>
KST(Korea Standard Time)를 포함하여 저장하도록 개발되어 수집한 데이터를 분석하기 용이하도록 하였다.

### (b) 포트 탐색 및 연결
지상국 컴퓨터와 통신 모듈 사이는 UART 통신을 하게 되므로, 이를 위한 포트 탐색 및 연결 기능을 제공한다.<br>
Search 버튼을 통해 콤보박스에 탐색된 시리얼 포트를 출력하고, 사용자가 콤보박스에 나타난 시리얼 포트를 선택하여 Connect 버튼을 누르면, 해당 시리얼 포트와 연결된다. 정상적으로 연결된 경우, 아래의 지도 영역과 센서값 영역에 수신한 데이터를 나타낸다.

### (c) 이미지 출력
ESP32 카메라 모듈을 통해 촬영된 사진을 나타내는 기능으로, 사진은 기본적으로 용량이 크므로, 원활한 통신을 위해 ESP32와 지상국은 와이파이 통신을 이용한다.<br>
**와이파이 통신의 통신거리가 생각보다 짧고, 예상보다 사진 송신에 시간이 걸리는 문제점이 존재함**

### (d) 캔 위성 위치 추적
folium, jinja2 패키지를 활용하여 개발되었고, 캔 위성에서 수신한 GPS 신호를 바탕으로 지도상에 위성의 위치를 실시간으로 표시한다. 사용자가 마커를 클릭할 경우, 해당 마커가 표시된 위치에서의 위성 고도와 시각 정보를 나타낸다.

### (e) 씨앗 사출 확인
캔 위성 대회에서 설정한 임무 목표에 따라, 캔 위성은 특정 고도와 가속도 조건에서 씨앗을 사출해야한다. 캔 위성의 씨앗이 사출 되었을 경우, 해당 영역에 'Ejected' 이라고 표시된다. 대기 상태일 경우 'Ejection Ready'라고 표시된다.

### (f) 센서값 그래프
캔 위성에서 수신한 이산화탄소 값, 고도 값, z축 가속도 값을 그래프로 나타내는 기능이다.<br>
0.5초마다 지그비로 수신한 센서 데이터를 그래프로 시각화하여 사용자가 실시간으로 캔 위성의 상태를 파악하도록 한다.

## 5. 역할
| 이름 | 소속 | 역할 | 이메일 |
| :---: | :---: | :---: | :---: |
| 박무성 | 경상국립대학교 항공우주및소프트웨어 공학부| 관제시스템 전반의 UI / 위성 위치추적 기능 / 실시간 센서값 그래프 / 버튼 리스너 / 시리얼 통신 개발 | pms3620@gmail.com |
| 이태상 | 경상국립대학교 항공우주및소프트웨어 공학부| ESP32 캠 연동 및 Selenium 활용 이미지 수신 개발 | dandy0113@naver.com |

## 6. 주최 및 후원 기관
| 인공위성 연구소 | 과학기술정보통신부 | 한국항공우주연구원 | 카이스트 | 전라남도 고흥군 |
| :---: | :---: | :---: | :---: | :---: |
|<a href="https://satrec.kaist.ac.kr/"><img src="images\1-1.jpg" height="100px"></a>|<a href="https://www.msit.go.kr/"><img src="images\1-2.jpg" height="100px"></a>|<a href="https://www.kari.re.kr/kor.do"><img src="images\1-3.jpg" height="100px"></a>|<a href="https://www.kaist.ac.kr/kr/"><img src="images\1-4.jpg" height="100px"></a>|<a href="https://www.goheung.go.kr/"><img src="images\1-5.jpg" height="100px"></a>|

## 7. 발표 논문

- [박무성, 이태상, 김다은, 이성진, "테라포밍을 위한 캔 위성의 임무와 관제시스템 개발", 한국항공우주학회 2022 추계학술대회](https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11180784&googleIPSandBox=false&mark=0&minRead=5&ipRange=false&b2cLoginYN=false&icstClss=010000&isPDFSizeAllowed=true&accessgl=Y&language=ko_KR&hasTopBanner=true)

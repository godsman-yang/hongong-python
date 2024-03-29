# 추가 정보
최근 언어를 가르치는 방식을 배우면서 알게되는 것들

#### 언어의 종류에 따른 개발 환경 구성
C/C++, JAVA, Python 언어를 개발하려면 개발환경이 필요하다. 어떤 언어의 개발환경을 쉽게 구성할 수 있고, 어떤 언어의 개발환경을 구성하는 것이 어려울까?
언어의 특성을 보면, 
* 컴파일언어와 인터프리터 언어의 차이 - IDE vs Editor
* Native OS와 Virtual 환경 이용의 유무 - SDK 설치
* 실행파일 배포와 코드 배포와 같은 배포 방식에 따라 다르다.

컴파일 언어는 독자적인 IDE를 이용하는 것이 편하다. 혼공C에서도 Microsoft Visual Studio를 사용한다.
인터프리터 언어는 기능이 많고, 편리하고, 지속해서 개발 중인 에디터를 이용한다. Visual Studio Code를 사용한다.
가상 환경을 이용하는 언어는 OS에 가상환경을 설치해야 한다. JAVA의 경우 자바 개발환경인 JDK를 설치한다. 버전을 맞추거나 systemp의 PATH를 설정하는 부분에서 어려움을 느낄 수 있다.
코드로 배포하는 언어는 개발환경 구성이 단순하다. 필요한 라이브러리는 배포한 시스템에서 (자동으로) 구성된다.

#### C언어로 시작할 때 어려운 점
C언어는 컴파일언어로 코드를 작성하고 컴파일한 후에 실행파일을 실행시켜서 결과를 확인한다.
기본적인 Hello, World 프로그램 안에 알아야 할 개념이 들어가 있다.
* include - 라이브러리, 나중에 설명
* int main() - 함수, 나중에 설명
* {} - 코드 블록, 나중에 설명
* printf() - 함수
* ; - 세미콜론, 문장의 끝
* "\n" - 이스케이프 문자
반대로 Hello, World 프로그램 하나를 이해하면 C언어 프로그램의 대략적인 개념을 알 수 있다.

다른 언어에서는 잘 설명하지 않는 개념을 기초 책에서 설명한다. 포인터 이전에 벌써 어렵다.
* ASCII 코드
* 정수형 - 2바이트, 4바이트, 8바이트에 따라 표현할 수 있는 범위가 다르다. 음수의 표현방법
* 부동소수 - 정확하지 않다. double의 경우에도 유효숫자 15자리까지 사용 가능하다.
* 진수 - 2진수, 8진수, 16진수


#### GitHub
코드 버전관리를 해야한다. 버전관리를 도와주는 도구가 있다. 도구를 이용하지 않으면 소스를 변경할 때마다 소스폴더를 다른이름으로 저장해 두거나 복사해 두었다. 버전관리 도구는 이전 버전을 기록해 두어서 코드가 잘못된 경우 과거의 코드로 돌아갈 수 있다.
* 코드의 이력관리가 가능하다
* 코드의 공유가 쉽다. - 다른 사람에게 코드를 공유하기 쉽다
* 코드에서 필요없는 주석을 제거할 수 있다 - 이전 코드 참조를 위한 주석이 필요없다

최근에 버전관리 도구로 git을 사용한다. 

git의 버전관리 개념으로 서비스를 만든 것이 gitHub 이다
* git 서비스
* issue 서비스
* gitHub flow - 소스 수정 절차

GitHub 참고
* 깃헙 소개 동영상[한글자막] - https://youtu.be/w3jLJU7DT5E
* [깃허브 사용법] - https://blog.naver.com/whdtjd419/221424826718


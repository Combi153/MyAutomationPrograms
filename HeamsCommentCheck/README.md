# HeamCommentCheck Program
경제학회에서 힘즈(Heams) 댓글 시간을 체크하고, 지각자를 색출하기 위해 만든 프로그램이다.

## Heams
* Heams란, 경제학회에서 제공하는 경제신문기사 메일링 서비스이다.
* 학회원들은 매일 Heams를 읽고 그에 관한 생각 혹은 분석을 댓글로 남겨야 한다.
* Heams의 신문기사가 게재되는 플랫폼은 네이버 카페이며, 네이버 카페 게시글에 댓글이 달리는 형식이다.

사진 예시 1

사진 예시 2

## 작동방식
1. 네이버 카페의 화면을 복사/붙여넣기한 파일, 학회원들의 이름을 저장한 파일 입력한다.
   * 화면 복사/붙여넣기 시 로그인, 로그아웃 상태에 따라 화면 구성이 달라진다. 따라서 로그인, 로그아웃에 따라 두 파일을 만들었다. 
2. 입력된 파일에서 학회원들의 이름을 비교하여 게시글 작성자, 작성 시간, 댓글 작성자, 작성 시간을 체크한다.
3. 정상 작성, 지각, 미작성 여부를 Dictionary ({학회원 이름 : 댓글 여부}) 구조로 저장한다.
4. Dictionary를 DataFrame으로 변환하여 엑셀 파일을 저장한다.

## 결과
* 모든 댓글과 작성자를 일일히 비교해 수행하던 일을 1분 내에 수행할 수 있었다.
* 정확한 벌금 계산을 할 수 있었다.
  

결과 사진 예시

## 역경과 아쉬움

### 1. 크롤링
* 네이버 카페의 화면을 복사/붙여넣는 것이 아니라 웹 크롤링을 하고 싶었다. 그러나 네이버 카페는 robot.txt에서 크롤링을 허용하지 않았다. 실제로 HTML을 받아오면 카페 내부의 코드는 받아올 수 없았다. 여러가지 방법을 찾아보았지만 내 수준에서 풀 수 없는 문제였다. 따라서 화면을 복사/붙여넣기하는 방법으로 돌아가는 선택을 했다.

### 2. 여러가지 반례들
* 코드를 작성한 후 테스트할 때 반례를 많이 발견했다.
  * 한 회원이 두 개의 댓글을 작성한 경우
  * 공휴일, 시험 기간 등의 이유로 게시글 및 댓글 작성 여부의 규칙이 이전과 달라지는 경우
  * 회원이 댓글을 수정한 경우
* 모든 반례를 해결하는 코드를 짜기에는 역량이 부족했다. 현재의 코드 작성 방식이 아닌 새로운 방식을 도입해야 한다고 생각했다. 가령 정규식을 공부해 새롭게 코드를 짜면 좋겠다고 생각했다.

### 3. 코드 방식
* 이 프로그램을 신규 운영진에게 인수인계했다.
* 파이썬에 대한 이해가 없는 사람은 코드를 기반으로 작동하는 프로그램을 사용하기 어려워했다. 예를 들어 local에서 이 프로그램을 사용하기 위해서는 python을 비롯한 pandas 등의 라이브러리를 직접 설치해서 사용해야 했다. 이러한 것을 안내해드리기 어려웠다. 
* 구글드라이브에서 사용할 수 있게 안내해드렸지만, 충분하지 않았다. 화면과 버튼으로 구성된 보다 작동하기 편한 프로그램을 만들었다면 더 좋았을 것이다.
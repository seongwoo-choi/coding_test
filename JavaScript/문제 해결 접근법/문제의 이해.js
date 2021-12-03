// 1. 문제를 나만의 방식으로 다시 적을 수 있는지
// 2. 문제에 입력하는 값이 무엇인지?(타입, 유효한 범위의 값, 다른 제한 조건이 있는지)
// 3. 문제의 해결 방법이 도출해야 하는 값은 무엇인지?
// 4. 출력값이 입력값에 의해 도출되는지?
// 5. 문제의 일부인 데이터의 중요한 부분이 무엇인지 알고 이름을 붙일 수 있는지?

// 두 숫자를 더해서 합을 출력하는 함수를 작성
// 1. 이 경우엔 두 숫자를 더해서 덧셈을 하는 것이다.
// 2. 그냥 두 숫자를 더하는 것(정수, 숫자가 얼마나 클 것인가? -> 상한선이 존재한다., 다른 )
// 3. 정수와 소수를 더했을 때 혹은 문자열일 경우
// 4. 맞다.
// 5. add 함수, num1, num2 가 있고 sum 을 받는다.
function add(num1, num2) {
  let sum = num1 + num2;
  return sum;
}

function charCount(arr) {
  // 문자열 q 를 split 으로 값을 쪼개서 배열로 만든다.
  // 배열 내부의 값들을 sort
  // 정렬된 값들을 다시 join 을 이용해서 문자열로 만들고 trim 을 이용해 맨 앞과 맨 뒤의 공백제거 후 다시 배열로 변환
  let sample = arr.split("").sort().join("").trim().split("");

  const count = sample.reduce((acc, cur, index, arr) => {
    // acc[x] 가 존재하면 현재 result[x] 의 밸류 값에 + 1
    if (acc[cur]) {
      acc[cur] += 1;
    }
    // acc[x] 가 undefined 일 경우 객체 생성을 해주고 밸류값으로는 1을 집어넣어준다.
    else {
      acc[cur] = 1;
    }
    // 누적합 생성
    return acc;
  }, {});
  console.log(count);
}

console.log(charCountForEach("aababbbacaccswcwajidjihod"));

// 먼저 알 수 있는 것은 출력값이 배열이나 다른 데이터 구조가 아니라 객체여야 한다.
charCount("aaaa"); // 출력 => { a:4 }
// 출력값에는 입력값에 있는 글자만 보여주면 되는 건가? 만약 입력값에 없는 글자는?
// { b:0, c:0 } 이런식으로 추가해야 하나?
charCount("hello"); // 출력 => { h:1, e:1, l:2, o:1 }

// 이것이 입력값이라면 출력값은 어떻게 되어야 하나?
// => 띄어쓰기도 고려해야 하나?
// 달러 표시나 밑줄이나 숫자같은 다른 문자들은 어떻게 처리??
charCount("내 전화번호는 1111002");

// 대문자 H 와 소문자 h 가 있으면 대소문자 구분을 해야 하는가?
charCount("Hello hi");

// 이런식으로 복잡한 입력값을 떠올릴 수록 문제를 이해하는데 도움이 되고 이런 질문들을 하면서 문제를 단순화 해서 더 깊이 이해할 수 있다.
// 문제에 달려들기 전에 문제를 이해하는 다른 방식이다.

// 이런식으로 charCount 에 아무것도 넣지 않거나 비어있는 문자열을 입력하면 어떻게 되나?
// charCount(); // null false undefined error 중에 무엇을 출력해야 할까?

// 문자열이 아니라 숫자나 객체나 null 을 입력하면 어떻게 될까??
// 물음표 살인마가 되야 한다.

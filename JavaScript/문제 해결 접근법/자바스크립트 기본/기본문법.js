var _ = require("lodash");

const num = [1, 2, 3, 3, 3, 4, 4, 5, 5, 6];
const obj1 = {name: "js", text: "11"};
const obj2 = {as: "js", name: "asd"};
const obj3 = {
    name: "Kim",
    tel: ["010-1111-1111", "010-2222-2222"],
};
const obj4 = {
    name: "Kim",
    address: "Seoul",
};

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

function charCountForEach(arr) {
    let sample = arr.split("").sort().join("").trim().split("");

    let result = {};
    sample.forEach((x) => {
        // result[x] 가 존재하면 현재 result[x] 의 밸류 값에 + 1
        if (result[x]) {
            result[x] += 1;
        }
        // result[x] 가 undefined 일 경우 객체 생성을 해주고 밸류값으로는 1을 집어넣어준다.
        else {
            result[x] = 1;
        }
    });
    return result;
}

console.log(charCountForEach("aababbbacaccswcwajidjihod"));

function avgNum(numArray) {
    const avg = numArray.reduce((acc, current, index, array) => {
        // index 의 갯수가 배열 갯수와 같아졌을 경우엔 스탑
        if (index === array.length - 1) {
            return (acc + current) / array.length;
        }
        // if 문 통과하기 전까지 모든 숫자를 더한다.
        return acc + current;
    }, 0);
    console.log(avg);
}

function isEmptyObj(obj) {
    if (obj.constructor !== Object) {
        return false;
    }

    for (let props in obj) {
        console.log(props);
        console.log(obj);
        if (!obj.hasOwnProperty(props)) {
            return false;
        }
    }

    return true;
}

console.log(isEmptyObj(obj1));

function mergeObj(obj1, obj2) {
    if (obj1.constructor !== Object && obj2.constructor !== Object) {
        return false;
    }

    //   for (let props in obj1) {
    //     if (!obj1.hasOwnProperty(props)) {
    //       return false;
    //     }
    //   }

    //   for (let props in obj2) {
    //     if (!obj2.hasOwnProperty(props)) {
    //       return false;
    //     }
    //   }

    let newObj = {};

    for (let props in obj1) {
        newObj[props] = obj1[props];
        console.log(newObj);
    }
    for (let props in obj2) {
        newObj[props] = obj2[props];
    }

    return newObj;
}

console.log(mergeObj(obj1, obj2));

function mergeObj2(obj1, obj2) {
    const newObj = Object.assign(obj1, obj2);
    const newObj2 = {...obj1, ...obj2};

    console.log("변경전", newObj2);

    obj1.test = "test";

    console.log(obj1);

    console.log("변경후", newObj2);
}

console.log(mergeObj2(obj1, obj2));

function lodashObjMerge(obj3, obj4) {
    const newObj = _.merge(obj3, obj4);
    console.log(newObj);

    obj3.tel.push("010-3333-3333");
    console.log(obj3.tel[0], obj3.tel[obj3.tel.length - 1]);
    console.log(newObj);
}

lodashObjMerge(obj3, obj4);

let arr = ["a", "b", "b", "c"];

function deleteArrIndex(arr) {
    // 원소 'b' 삭제
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "b") {
            arr.splice(i, 1);
            i--;
        }
    }
}

function deleteArrIndex2(arr) {
    // 원소 'b' 삭제
    let newArr = arr.filter((el) => el !== "b");
    console.log(newArr);
}

deleteArrIndex2(arr);

function filter() {
    const arr = [
        {name: "apple", price: 1000},
        {name: "banana", price: 2000},
        {name: "apple", price: 3000},
    ];

    const data = arr.filter((fruit) => fruit.name == "apple");

    // 접근법 data[배열 idx][객체 속성 이름]
    console.log(data);
}

filter();

const arraySort = [4, 1, 3, 6];
arraySort.sort((a, b) => (a > b ? 1 : -1));
console.log(arraySort);


// 프로그래머스 49993 솔루션 1
function solution1(skill, skill_trees) {
    let answer = 0;

    loop: for (let tree of skill_trees) {
        let lastIndex = -1;
        let noMoreFlag = false;

        for (let a of skill) {
            let currIndex = tree.indexOf(a);

            if (currIndex === -1) {
                noMoreFlag = true;
                continue;
            }

            if (noMoreFlag === true) {
                continue loop;
            }

            if (currIndex < lastIndex) {
                continue loop;
            }
            lastIndex = currIndex;
        }

        answer++;
    }

    return answer;
}


// 프로그래머스 49993 솔루션 2
function solution2(skill, skill_trees) {
    function isCorrect(n) {
        let skills = skill.split("");
        for (let i = 0; i < n.length; i++) {
            if (!skill.includes(n[i])) {
                continue;
            }
            if (n[i] === skills.shift()) {
                continue;
            }
            return false;
        }
        return true;
    }

    return skill_trees.filter(isCorrect).length;
}


// 프로그래머스 49993 솔루션 3
function solution3(skill, skill_trees) {
    const skills = skill.split("");
    return skill_trees.filter((tree) =>
        skill.indexOf(
            tree.split("")
                .filter(s => skills.includes(s))
                .join("")
        ) === 0
    ).length;
}

skill = "CBD";
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"];
console.log(solution1(skill, skill_trees));
console.log(solution2(skill, skill_trees));
console.log(solution3(skill, skill_trees));

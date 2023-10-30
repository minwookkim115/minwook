/*
손님이 분식점에서 라면을 시켰다 == 우리가 만든 서비스의 화면을 사용자가 요청 했다
라면 == 화면
라면 재료 준비 == 화면을 보여주는데 필요한 데이터
완성되면 서빙 == 주니되면 화면보여주기

Promise 객체 사용법
new Promise((resolve, reject) => {

    if(비동기작업 완료 조건){
        return resolve(value) // 비동기 작업이 성공했을 때 리턴하고 싶은 값이 있으면 value
    } else if (비동기작업 실패 조건){
        return reject(value) // 비동기 작업이 실패했을 때 리턴하고 싶은 값이 있으면 value
    }
})

.then()과 .catch()는 Promise 객체에 사용하는 메소드
*/

console.log('라면을 끓인다. (각 과정이 준비되는데 1~3초가 걸린다.)')

// 물은 끓는데 3초가 걸린다
const water = function (ramen) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('1. 물을 끓인다.')
            ramen.push('물')
            return resolve(ramen)
            // return reject('물을 너무 많이 넣었다.') 이걸 쓰면 .catch()에서 에러로 잡힘
        }, 3000)
    })
}


const soupAndNoodle = function (ramen) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('2. 스프와 면을 넣는다.')
            ramen.push('스프')
            ramen.push('면')
            return resolve(ramen)
        }, 2000)
    })
}

const egg = function (ramen) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('3. 계란을 넣는다.')
            ramen.push('계란')
            return resolve(ramen)
        }, 1000)
    })
}


const ramen = []

water(ramen)
    .then((ramen) => {
        return soupAndNoodle(ramen)
    })
    .then((ramen) => {
        return egg(ramen)
    })
    .then((ramen) => {
        console.log('라면 완성!!: ', ramen)
    })
    .catch((err) => {
        console.log('라면을 끓이는 도중에 문제 발생: ', err)
    })
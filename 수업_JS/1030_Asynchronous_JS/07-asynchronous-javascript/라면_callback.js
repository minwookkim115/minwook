// 너무 쌓이게 됨
setTimeout(() => {
    console.log('1. 물을 끓인다')
    setTimeout(() => {
        console.log('2. 면과 스프를 넣는다.')
        setTimeout(() => {
            console.log('3. 계란을 넣는다.')
        }, 1000);
    }, 2000)
}, 3000)
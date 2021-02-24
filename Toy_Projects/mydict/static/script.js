// let words = {{words|tojson}};
// let word_list = [];
// for (let i = 0; i < words.length; i++) {
//     word_list.push(words[i]['word'])
// }
// console.log(word_list)
//


function find_word() {
    let word = $('#input-word').val()
    $.ajax({
        type: "GET",
        url: `/`,
        data: {},
        success: function (response) {
            let words = response['words']
            console.log(words)
        }
    })
}

//     if (word_list.includes(word)) {
//         // 리스트에 있으면 하이라이트
//         $(`#word-${word}`).addClass('highlight')
//         $(`#word-${word}`)[0].scrollIntoView()
//     } else {
//         // 리스트에 없으면 새 단어를 위한 상세페이지로
//         window.location.href = `/detail/${word}?status_give=new`
//     }
// }
// Test Start 버튼을 클릭했을 때, article class='start'를 숨기고, article class='question'을 나타냄
function start(){
    $('.start-area').hide();
    $('.question').show();
    next();
};

var q_num = 1;
function next() {
    if (q_num == 16) {
        // PAI type 결과를 결정하는 로직을 작성한다.
        var PAI_type = '';
        var type_other1 = '';
        var type_other2 = '';
        if ($('#R').val()<=2 && $('#O').val()>=3 && $('#E').val()<=2) {
            PAI_type = 'I'
            type_other1 = 'M'
            type_other2 = 'A'
        } else if ($('#R').val()>=3 && $('#O').val()<=2 && $('#E').val()>=3) {
            PAI_type = 'A'
            type_other1 = 'M'
            type_other2 = 'I'
        } else {
            PAI_type = 'M'
            type_other2 = 'I'
            type_other1 = 'A'
        }

        $('.question').hide();
        $('.result').show();
        $('#type_img').attr('src', result[PAI_type]['img'])

        $('#type_other1').attr('src', result[type_other1]['img'])
        $('#type_other2').attr('src', result[type_other2]['img'])


    } else {
        $('#contents').html(questions[q_num]['contents']);
        $('#type').val(questions[q_num]['type']);
        $('#Yes').html(questions[q_num]['Yes']);
        $('#No').html(questions[q_num]['No']);
        $('.progress-bar').attr('style','width: calc(100/15*'+(q_num)+'%)');
        $('#counts').html(q_num+' / 15');
        q_num++;
    }
}

// id="Yes"를 클릭 했을 때, 함수를 실행
// 해당 함수는 id="type"의 value를 가져오고, 그 value를 type이라는 변수에 저장
// 변수 type에 해당하는 태그의 value를 가져와서, preValue라는 변수에 저장
// 변수 type에 해당하는 태그의 value를 prevValue에 1을 더한 값으로 변환
$("#Yes").click(function(){
    var type = $('#type').val();
    var preValue = $('#'+type).val();
    $('#'+type).val(parseInt(preValue)+1);
    next();
});
    
$("#No").click(function(){
    next();
});

// 문제 리스트
var questions = {
    1: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 규칙, 규정을 잘 따르는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "R", "Yes": "그런 편이다", "No": "아닌 편이다"},
    2: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 정해진 방식보다 유연성을 잘 발휘하는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "O", "Yes": "그런 편이다", "No": "아닌 편이다"},
    3: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 구체적으로 촘촘하게 계획된 일을 좋아하는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "E", "Yes": "그런 편이다", "No": "아닌 편이다"},
    4: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 사소한 규정이나, 규칙일지라도 무조건 지키는 사람이라 <br> (ex 휴게 시간을 정확하게 기록한다) </span> <br> 말한다 / 피드백한다", "type": "R", "Yes": "그런 편이다", "No": "아닌 편이다"},
    5: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 규칙에 크게 구애 받지 않고, 유연하게 일하는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "O", "Yes": "그런 편이다", "No": "아닌 편이다"},
    6: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 사소한 일이라도 기록하고, 미리 계획하는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "E", "Yes": "그런 편이다", "No": "아닌 편이다"},
    7: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 체계적이고, 조직적으로 일하는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "R", "Yes": "그런 편이다", "No": "아닌 편이다"},
    8: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 합의된 계획대로 일이 진행되지 않더라도, <br> 불안해하지 않는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "O", "Yes": "그런 편이다", "No": "아닌 편이다"},
    9: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 업무 스케쥴 관리가 체계적인 사람이라 </span> <br> 말한다 / 피드백한다", "type": "E", "Yes": "그런 편이다", "No": "아닌 편이다"},
    10: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 관리하는 것(일, 업무 등)에 질서를 부여하기 좋아하는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "R", "Yes": "그런 편이다", "No": "아닌 편이다"},
    11: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 계획없이 떠나는 여행을 선호하는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "O", "Yes": "그런 편이다", "No": "아닌 편이다"},
    12: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 휴일이나 주말에 쉬는 것도 사전에 계획하는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "E", "Yes": "그런 편이다", "No": "아닌 편이다"},
    13: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 약속된 시간에 늦을 것 같지 않은 사람이라 </span> <br> 말한다 / 피드백한다", "type": "R", "Yes": "그런 편이다", "No": "아닌 편이다"},
    14: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 꼼꼼하게 일정을 관리하기 보다는, <br> 대략적인 마감일자를 정해놓고 일하는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "O", "Yes": "그런 편이다", "No": "아닌 편이다"},
    15: {"contents": "나에 대해서 동료들은 <br> <span class='question-text'> 정해진 일정 안에서 효율을 높이는 방법을 찾는 사람이라 </span> <br> 말한다 / 피드백한다", "type": "E", "Yes": "그런 편이다", "No": "아닌 편이다"},
}

// 결과 리스트
var result = {
    "I": {"title": "해시계를 기깔나게 표현하는 문구", "explain": "나는야 해시계", "img": "https://wetimeresult1.netlify.app/result1.jpg"},
    "M": {"title": "명품시계를 기깔나게 표현하는 문구 ", "explain": "나는야 배꼽시계", "img": "https://wetimeresult2.netlify.app/result2.jpg"},
    "A": {"title": "올림픽시계를 기깔나게 표현하는 문구", "explain": "나는야 올림픽시계", "img": "https://wetimeresult3.netlify.app/result3.jpg"},
} 

function others() {
    let status = $('.type_others').css('display');
    if (status == 'block') {
        $('.type_others').hide();
        $('.btn-type-other').text('다른 유형 구경하기')
    } else {
        $('.type_others').show();
        $('.btn-type-other').text('다른 유형 구경닫기')
    }
}

Kakao.init('9d747fb632219a3cd369499cf00cb58a'); // 초기화
// function sendLink() { // 카카오톡 공유하기
//     Kakao.Link.sendDefault({
//         objectType: 'text',
//         text: '시간 관점 테스트',
//         link: {
//             mobileWebUrl: 'https://kakao-pai-test.netlify.app',
//             webUrl: 'https://kakao-pai-test.netlify.app',
//         },
//     })
// }

function sendLink() {
    Kakao.Link.sendDefault({
        objectType: 'feed',
        content: {
            title: '시간 관점 테스트',
            description: '나를 시계로 표현한다면!?',
            imageUrl:
                'https://t1.kakaocdn.net/friends/prod/product/20200714160917279_8809721502280_BW_00.jpg',
            link: {
                mobileWebUrl: 'https://kakao-pai-test.netlify.app',
                webUrl: 'https://kakao-pai-test.netlify.app',
            },
        },
    });
}
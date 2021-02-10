// $(document).ready(function(){
// //    페이지가 로딩되면 실행하고 싶은 함수 작성
// });

function openClose() {
    let status = $('#main-posting-box').css('display');
    if (status == 'block') {
        $('#main-posting-box').hide();
        $('#main-btn').text('기록하기');
    } else {
        $('#main-posting-box').show();
        $('#main-btn').text('기록닫기');
    }
}



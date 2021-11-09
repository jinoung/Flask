$(document).ready(function() {

    // Bootstrap-selcct - http://silviomoreto.github.io/bootstrap-select
    $('.selectpicker').selectpicker();

    // http://getbootstrap.com/javascript/#popovers
    $('[data-profile="popover"]').popover({
        placement : 'auto',
        html: 'true',
        container: '.rb-bbs',
        content: '<div class="media"><a class="pull-left" href="#" data-toggle="modal" data-target="#modal-profile"><img class="media-object" src="../../assets/img/noavatar-blue.png"></a><div class="media-body"><h4 class="media-heading"><a href="#" data-toggle="modal" data-target="#modal-profile">홍길동 (대한이)</a> <i class="fa fa-circle rb-presence active" data-toggle="tooltip" title="온라인"></i></h4><p class="text-muted"><small>가입일 : 2009.06.12 (2312일전)<br>마지막접속 : 2015.10.12 (0일전)<br>포인트 : 11,966 , 등급 : 비기너++ 10</small></p><p class="rb-relation">함께아는 친구 <strong>16명</strong></p></div></div>',
        template: '<div class="popover rb-profile" role="tooltip"><div class="arrow"></div><div class="popover-content"></div><div class="popover-footer text-right"><div class="btn-group" role="group" aria-label="..."><div class="btn-group btn-group-sm" role="group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-check"></i> 친구 <span class="caret"></span></button><ul class="dropdown-menu"><li><a href="#">친구 끊기</a></li></ul></div><div class="btn-group btn-group-sm" role="group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-check"></i> 팔로잉 <span class="caret"></span></button><ul class="dropdown-menu dropdown-menu-right"><li><a href="#">팔로잉 취소</a></li></ul></div><button type="button" class="btn btn-default btn-sm">메시지</button></div></div></div>'
    });

    // http://mattlockyer.com/2013/04/08/close-a-twitter-bootstrap-popover-when-clicking-outside/
    $('body').on('click', function (e) {
        $('[data-profile="popover"]').each(function () {
            //the 'is' for buttons that trigger popups
            //the 'has' for icons within a button that triggers a popup
            if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.popover').has(e.target).length === 0) {
                $(this).popover('hide');
            }
        });
    });

    //$("body").on("click", function(e) {
        //$('[data-profile="popover"]').each(function() {
            //$(this).is(a.target) || 0 !== $(this).has(a.target).length || 0 !== $(".popover").has(a.target).length || $(this).popover("hide")
        //})
    //})


});
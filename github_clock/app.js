var Format = 1,
    TimeHolder = 0,
    stopChecker = 0;

function SetDay(DD) {
    if (DD === 5) {
        $(".WeekDays span:nth-child(" + (DD + 2) + ")").addClass('active')
    }
    $(".WeekDays span:nth-child(" + ((DD + 2) % 7) + ")").addClass('active')
}

function resetTimer() {
    $('.S1').removeClass().addClass('S1 show0')
    $('.S2').removeClass().addClass('S2 show0')

    $('.M1').removeClass().addClass('M1 show0')
    $('.M2').removeClass().addClass('M2 show0')

    $('.H1').removeClass().addClass('H1 show0')
    $('.H2').removeClass().addClass('H2 show0')
}

function Run24hr(S1, S2, M1, M2, H1, H2) {
    $('.S1').removeClass().addClass('S1 show' + S1)
    $('.S2').removeClass().addClass('S2 show' + S2)

    $('.M1').removeClass().addClass('M1 show' + M1)
    $('.M2').removeClass().addClass('M2 show' + M2)

    $('.H1').removeClass().addClass('H1 show' + H1)
    $('.H2').removeClass().addClass('H2 show' + H2)
}

function Run12hr(S1, S2, M1, M2, HH) {
    if (HH > 12) {
        HH = HH - 12
        $(".Formats span:nth-child(2)").addClass('active');
    } else {
        $(".Formats span:nth-child(1)").addClass('active');
    }

    var H1 = Math.floor(HH / 10),
        H2 = HH % 10;

    $('.S1').removeClass().addClass('S1 show' + S1)
    $('.S2').removeClass().addClass('S2 show' + S2)

    $('.M1').removeClass().addClass('M1 show' + M1)
    $('.M2').removeClass().addClass('M2 show' + M2)

    if (H1 === 0) {
        $('.H1').fadeOut(0)
    } else {
        $('.H1').fadeIn().removeClass().addClass('H1 show' + H1)
    }
    $('.H2').removeClass().addClass('H2 show' + H2)
}

function StopWatch(TimeHolder) {
    var HH = Math.floor(TimeHolder / 3600),
        MM = Math.floor((TimeHolder - (HH * 3600)) / 60),
        SS = Math.floor(TimeHolder - HH * 3600 - MM * 60)
    var S1 = Math.floor(SS / 10),
        S2 = SS % 10,
        M1 = Math.floor(MM / 10),
        M2 = MM % 10,
        H1 = Math.floor(HH / 10),
        H2 = HH % 10;
    Run24hr(S1, S2, M1, M2, H1, H2)
}

function update_time() {
    var dt = new Date(),
        HH = dt.getHours(),
        MM = dt.getMinutes(),
        SS = dt.getSeconds(),
        DD = dt.getDay();

    SetDay(DD)

    var S1 = Math.floor(SS / 10),
        S2 = SS % 10,
        M1 = Math.floor(MM / 10),
        M2 = MM % 10,
        H1 = Math.floor(HH / 10),
        H2 = HH % 10;

    if (Format === 1) {
        Run24hr(S1, S2, M1, M2, H1, H2);
    }
    else if (Format === 2) {
        Run12hr(S1, S2, M1, M2, HH);
    } else if (Format === 3 && stopChecker === 0) {
        TimeHolder++
        StopWatch(TimeHolder)
    } else if (Format === 4 && stopChecker === 0) {
        TimeHolder--
        if (TimeHolder === 0) {
            AlarmOut();
        }
        else {
            StopWatch(TimeHolder)
        }
    }
    setTimeout(update_time, 1000)
}


$('.Type span').on('click', function () {
    $('.Type .active').removeClass('active');
    $(this).addClass('active');

    var T = $(this).html()
    if (T === '24hr') {
        Format = 1;
        $('.H1').fadeIn();
        $('.Formats span').removeClass('active')
    } else {
        Format = 2;
    }
})


$('.fa-stopwatch').on('click', function () {
    $('body').removeClass('BgAnimation')
    $('.H1').fadeIn()
    if (!($('.timeHolder').hasClass('StopWatch'))) {
        Format = 3;
        resetTimer()
        stopChecker = 1
        $('.timeHolder').removeClass().addClass('timeHolder StopWatch')
        $('.numbers').fadeIn(0)
        $('.pause').removeClass('active')
        $('.start').addClass('active')
        TimeHolder = 0
        console.log(Format);
    }
})

$('.start').on('click', function () {
    $('body').removeClass('BgAnimation')
    if (Format === 3) {
        stopChecker = 0;
        $(this).removeClass('active')
        $('.pause').addClass('active')
    }
    else if (Format === 4) {
        TimeHolder = $('.countDown input').val()
        if (TimeHolder > 0) {
            stopChecker = 0;
            resetTimer()
            $(this).removeClass('active')
            $('.pause').addClass('active')
            $('.countDown').addClass('DisNone')
            $('.numbers').fadeIn(0)

        }
    }
})

$('.pause').on('click', function () {
    stopChecker = 1
    $(this).removeClass('active')
    $('.start').addClass('active')
})

$('.stop').on('click', function () {
    $('body').removeClass('BgAnimation')
    if (Format === 3) {
        stopChecker = 1
        TimeHolder = 0
        resetTimer()
        $('.pause').removeClass('active')
        $('.start').addClass('active')
    }
    else if (Format === 4) {
        resetTimer()
        stopChecker = 1
        $('.countDown').removeClass('.DisNone')
        $('.numbers').fadeIn(0)
        $('.countDown input').val("")
        $('.pause').removeClass('active')
        $('.start').addClass('active')
    }
})

$('.fa-solid.fa-clock').on('click', function () {
    $('body').removeClass('BgAnimation')

    if (($('.Type .active').html()) === '12hr') {
        Format = 2;
    } else {
        Format = 1;
    }

    stopChecker = 0

    $('.timeHolder').removeClass().addClass('timeHolder')
    $('.numbers').fadeIn(0)
})

$('.fa-regular.fa-clock').on('click', function () {
    $('body').removeClass('BgAnimation')
    $('.H1').fadeIn()
    if (!($('.timeHolder').hasClass('countDwn'))) {
        $('.timeHolder').removeClass().addClass('timeHolder countDwn')
        Format = 4
        resetTimer();
        stopChecker = 1
        $('.countDown').removeClass('DisNone')
        $('.timeHolder').addClass('countDwn')
        $('.numbers').fadeOut(0)
        $('.pause').removeClass('active')
        $('.start').addClass('active')
    }
})

function AlarmOut() {
    $('body').addClass('BgAnimation')
    resetTimer()
    stopChecker = 1
}

update_time()
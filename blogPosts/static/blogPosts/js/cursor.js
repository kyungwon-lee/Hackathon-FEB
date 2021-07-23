$(document).ready(function () {
    $(document).mousemove(function (e) {
        //마우스커서 위치 담을 변수
        var mouseX = e.pageX;
        var mouseY = e.pageY;

        $("#cursor").show().css({
            left: mouseX + 2 + "px",
            top: mouseY + 2 + "px"
        });
    });
});

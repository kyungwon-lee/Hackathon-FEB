const onMypageElement = async () => {
    const dropDown = document.getElementById(`usermenu-dropdown`);
    const clickIcon = document.getElementById(`click_icon`);

    if (dropDown.style.display == "none") {
        var src1 = clickIcon.getAttribute("dataup");
        clickIcon.setAttribute("src", src1);
        dropDown.style.display = "block";
    }
    else {
        var src2 = clickIcon.getAttribute("datadown");
        clickIcon.setAttribute("src", src2);
        dropDown.style.display = "none";
    }
};
function autocomplete(inp, arr, categoryId, rId) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function (e) {
    var a, b, i, val = this.value;
    var section_list = ['금융', '사랑', '운동', '취미', '학습', '전자기기', '어플리케이션', '기타'];
    /*close any already open lists of autocompleted values*/
    closeAllLists();
    if (!val) { return false; }
    currentFocus = -1;
    /*create a DIV element that will contain the items (values):*/
    a = document.createElement("a");
    a.setAttribute("id", this.id + "autocomplete-list");
    a.setAttribute("class", "autocomplete-items");
    a.setAttribute("style", "position:relative;")
    /*append the DIV element as a child of the autocomplete container:*/
    this.parentNode.appendChild(a);

    // Add ~에 대한 검색 결과 html
    searchTitle = document.createElement("div");
    searchTitle.setAttribute("id", this.id + "autocomplete-title");
    searchTitle.setAttribute("class", "autocomplete-title");
    searchTitle.innerHTML = `"${val}"에 대한 검색결과가 없습니다.`;
    a.appendChild(searchTitle);

    b_parent = document.createElement("ul");
    b_parent.setAttribute("class", "sleeping_ul");
    /*for each item in the array...*/
    for (i = 0; i < arr.length; i++) {
      /*check if the item starts with the same letters as the text field value:*/
      console.log(arr[i].toUpperCase());
      if (arr[i].toUpperCase().indexOf(val.toUpperCase()) != -1) {
        searchTitle.innerHTML = `<strong>"${val}"에 대한 검색결과</strong>`;
        // a.appendChild(searchTitle);
        /*create a DIV element for each matching element:*/
        b = document.createElement("li");
        b.setAttribute('class', "sleeping_NQ");
        /*make the matching letters bold:*/
        b.innerHTML = `<a href="/mainPage/${categoryId[i]}/post/${rId[i]}/">`
          /*insert a input field that will hold the current array item's value:*/
          // + "<input type='hidden'>"
          + `<div class="inner_NQ">` + `${section_list[categoryId[i]]} > ` + arr[i] + `</div>`
          + `</a>`;
        /*execute a function when someone clicks on the item value (DIV element):*/
        b.addEventListener("click", function (e) {
          /*insert the value for the autocomplete text field:*/
          inp.value = this.getElementsByTagName("input")[0].value;
          /*close the list of autocompleted values,
          arr[i].substr(0, val.length) + arr[i].substr(val.length)
          (or any other open lists of autocompleted values:*/
          closeAllLists();
        });
        b_parent.appendChild(b);
      }
    }
    a.appendChild(b_parent);
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function (e) {
    var x = document.getElementById(this.id + "autocomplete-list");
    if (x) x = x.getElementsByTagName("div");
    if (e.keyCode == 40) {
      /*If the arrow DOWN key is pressed,
      increase the currentFocus variable:*/
      currentFocus++;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 38) { //up
      /*If the arrow UP key is pressed,
      decrease the currentFocus variable:*/
      currentFocus--;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 13) {
      /*If the ENTER key is pressed, prevent the form from being submitted,*/
      e.preventDefault();
      if (currentFocus > -1) {
        /*and simulate a click on the "active" item:*/
        if (x) x[currentFocus].click();
      }
    }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
    closeAllLists(e.target);
  });
}

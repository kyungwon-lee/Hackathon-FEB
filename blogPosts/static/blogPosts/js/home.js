const searchDataList = [
  "김갑생",
  "갑생김",
  "생깁감",
  "생김갑",
  "갑김생",
  "김생갑",
]

const autoMaker = () => {
  const searchValue = document.getElementById('homeSearch').value;
  searchedResults = searchDataList.filter(query => query.includes(searchValue));
  const selectBoxElement = document.getElementsByClassName('myselect')[0];

  if(searchValue) {
    selectBoxElement.setAttribute('style', 'display: visible');
    console.log(searchedResults.length);
    if(searchedResults.length) {
      var searchPreview = document.createElement('option');
      searchPreview.innerHTML = searchedResults[0];
      selectBoxElement.appendChild(searchPreview);
      console.log(selectBoxElement);
    }
  } else {
    selectBoxElement.setAttribute('style', 'display: none');
  }

  


}

const onAddComment = async (postId, rid) => {
    const commentInputElement = document.getElementById("review-input-type");
    if (commentInputElement.value) {
        let data = new FormData();
        data.append("content", commentInputElement.value);
        const response = await axios.post(`/mainPage/${rid}/post/${postId}/comments/`, data);
        const { commentId, commentCount, createdTime, author, author_profile } = response.data;
        const commentElement = getCommentElement(postId, rid, commentId, commentInputElement.value, createdTime, author, author_profile);
        document.getElementById("async_comment").appendChild(commentElement);
        commentInputElement.value = '';
        const postCommentNum = document.getElementById(`commentset-num`);
        postCommentNum.innerHTML = `게시판 후기&nbsp;<em>(${commentCount})</em>`;
    }
};

const getCommentElement = (postId, rid, commentId, comment, createdTime, author, author_profile) => {
    // 새로 Element 만들기
    let newCommentElement = document.createElement("ul");
    newCommentElement.setAttribute('class', `review-1st`);
    newCommentElement.id = `post${postId}-comment${commentId}`;
    newCommentElement.innerHTML =
        `
        <li class="1st">
            <div class="user-info">
                <span class="img">
                <div class="profile">
                    <img src = ${author_profile}>
                </div>
                </span>
                <div class="txt">
                <span class="username">${author}</span>
                <p class="date">
                ${createdTime} 
                <button onclick="onDeleteComment(${postId}, ${rid}, ${commentId})">댓글 삭제</button>
                </p>
                </div>
            </div>
            <div class="content">
                <p> ${comment}  </p>
            </div>
        </li>`
    return newCommentElement;
};

const onDeleteComment = async (postId, rid, commentId) => {
    const alert = window.confirm("정말 삭제하시겠습니까?");
    if (alert) {
        const response = await axios.delete(`/mainPage/${rid}/post/${postId}/comments/${commentId}/`);
        document.getElementById(`post${postId}-comment${commentId}`).remove();
        const postCommentNum = document.getElementById(`commentset-num`);
        postCommentNum.innerHTML = `게시판 후기&nbsp;<em>(${response.data.commentNum})</em>`;
    }
};
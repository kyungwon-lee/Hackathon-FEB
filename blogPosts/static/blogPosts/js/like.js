const onClickLikeButton = async (postId, rid) => {
    const postLikeButton = document.getElementById(`${postId}-like-button`);
    const postDisLikeButton = document.getElementById(`${postId}-dislike-button`);

    const response = await axios.post(`/mainpage/${rid}/posts/${postId}/like/`);
    const { postLikeOfUser, flag, voteTotalCount, voteLikeCount } = response.data;
    if (postLikeOfUser == 1) {
        if (flag) {
            // 만약에 이미 싫어요를 누른 User라면?
            postDisLikeButton.style.backgroundColor = "#ffffff"
        }
        postLikeButton.style.backgroundColor = "#ffe599"
    }
    else {
        postLikeButton.style.backgroundColor = "#ffffff"
    }
    const voteCount = document.getElementById(`${postId}-votes-count`);
    voteCount.innerHTML = `<span class="article-vote-label">${voteTotalCount} 명 중 ${voteLikeCount} 명은 도움이 되었다고 했습니다.</span>`;
};

const onClickDislikeButton = async (postId) => {
    const postLikeButton = document.getElementById(`${postId}-like-button`);
    const postDisLikeButton = document.getElementById(`${postId}-dislike-button`);

    const response = await axios.post(`/posts/${postId}/dislike/`);
    const { postLikeOfUser, flag, voteTotalCount, voteLikeCount } = response.data;
    if (postLikeOfUser == 1) {
        if (flag) {
            // 만약에 이미 좋아요를 누른 User라면?
            postLikeButton.style.backgroundColor = "#ffffff"
        }
        postDisLikeButton.style.backgroundColor = "#ffe599"
    }
    else {
        postDisLikeButton.style.backgroundColor = "#ffffff"
    }
    const voteCount = document.getElementById(`${postId}-votes-count`);
    voteCount.innerHTML = `<span class="article-vote-label">${voteTotalCount} 명 중 ${voteLikeCount} 명은 도움이 되었다고 했습니다.</span>`;
};
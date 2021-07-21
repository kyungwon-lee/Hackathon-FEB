const addUserImage = (profile_image) => {
    const image = document.getElementsByName('photo')[0].files[0];
    const url = URL.createObjectURL(image);

    const imageEl = document.getElementsByClassName('profileImage')[0];
    imageEl.src = url;
}


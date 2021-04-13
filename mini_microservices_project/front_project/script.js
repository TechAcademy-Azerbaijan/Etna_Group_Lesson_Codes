async function renderPost(post){
    let commentList = await getComments(post.id);
    let commentListHTML = commentList ? commentList.map(comment => `<li>${comment.content}</li>` ).join(' ') : ''
    return `<div class="col-md-3">
                <div class="card ">
                        <div class="card-body">
                            <h3 class="card-title">${post.title}</h3>
                            <span>${commentList.length} comments</span>
                            <ul>
                                ${ commentListHTML }
                            </ul>
                            <hr>
                            <form method="post" data-id="${post.id}" class="create-comment">
                                <input name="content" type="text" placeholder="Write comment">
                                <input type="submit" value="Create Comment">
                            </form>
                        </div>
                </div>
            </div>`
}

async function getComments(post_id){
    let response = await fetch(`http://localhost:5002/api/v1.0/posts/${post_id}/comments/`);
    if( !response.ok){
        alert('Something went wrong');
        throw Exception('Something went wrong');
    }

    let commentList = await response.json();
    return commentList.comments;
}

async function getPosts() {
    let response = await fetch('http://localhost:5000/api/v1.0/posts/');
    if( !response.ok){
        alert('Something went wrong');
        throw Error('Something went wrong');
    }
    let postList = await response.json();
    let postHTML = '';
    for (let post of postList){
        postHTML+= await renderPost(post);
    }
    return postHTML;
}

window.onload = async function () {
    let postHTML = await getPosts();
    let postsElement = document.getElementById('post-list');
    postsElement.innerHTML = postHTML;

}

document.addEventListener('submit', async function (e) {
    e.preventDefault();
    console.log(e.target);
    if (!e.target.classList.contains('create-comment')){
        return null
    }
    let form = e.target;
    let postId = form.dataset.id;
    let commentData = {
        content: form.content.value
    };
    console.log(postId);
    let response = await fetch(`http://localhost:5002/api/v1.0/posts/${postId}/comments/`, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(commentData)
    });
    if (!response.ok){
        alert('Something went wrong');
        throw Error('Something went wrong');
    }
    let createdData = await response.json();
    let content = createdData.content;
    let ulElement = form.previousElementSibling.previousElementSibling;
    let newComment = document.createElement('li')
    newComment.innerText = content;
    ulElement.appendChild(newComment);
    form.reset();
});


const likeBtn = document.querySelector('.fa-heart')

console.log(likeBtn)


likeBtn.addEventListener("click", (e) => {
  console.log(e)
  const movieId = e.target.dataset.id

  axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
  axios.defaults.xsrfCookieName = 'csrftoken'
  axios.defaults.xsrfHeaderName = 'X-CSRFToken'

  axios.post(`/like/${movieId}/`)
  .then((response) => {
    console.log(response)
    count = document.querySelector('#nanum')

    console.log(count)
    count.innerText = `${response.data.like_count}명이 좋아합니다.`

    if (response.data.is_like){
      e.target.classList.remove('far')
      e.target.classList.add('fas')
    } else {
      e.target.classList.remove('fas')
      e.target.classList.add('far')
    }
  })
  .catch((error) => {console.log(error)})
  
})
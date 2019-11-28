const posters = document.querySelectorAll('.card-img-top')
const htags = document.querySelectorAll('.hover_test')
// posters.forEach((poster)=>{
  
//   poster.addEventListener("mouseover", (e) => {
//     // e.target.style.opacity = 0.5
//     const poster_id = e.target.dataset.id
//     // const ptag = document.querySelector(`#p_${poster_id}`)
    
//     const ptag = document.getElementById(`p_${poster_id}`)
//     const p2tag = document.getElementById(`p2_${poster_id}`)
    
//     ptag.style.display = 'block'
//     p2tag.style.display = 'block'
//     // ptag.innerHTML = ''
//     axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
//     axios.defaults.xsrfCookieName = 'csrftoken'
//     axios.defaults.xsrfHeaderName = 'X-CSRFToken'

//     axios.post(`/movies/show/${poster_id}/`)
//     .then((response) => {
      
//       document.getElementById(`p2_${poster_id}`).innerText = `⭐ ${response.data.avg_rating}`
//       document.getElementById(`p_${poster_id}`).innerText = `😍 ${response.data.like_count}`
//     })
//     .catch((error) => {console.log(error)})
//   })
//   poster.addEventListener("mouseout", (e) => {
//     e.target.style.opacity = 1
//     const poster_id = e.target.dataset.id
//     const ptag = document.getElementById(`p_${poster_id}`)
//     const p2tag = document.getElementById(`p2_${poster_id}`)
    
//     ptag.style.display = 'none'
//     p2tag.style.display = 'none'
//   })
//   // poster.addEventListener("mouseout")
// })
htags.forEach((htag)=>{
  
  htag.addEventListener("mouseover", (e) => {
    e.target.style.opacity=0.5
    const poster_id = e.target.dataset.id
    if (poster_id) {
      console.log(poster_id)
      const ptag = document.getElementById(`p_${poster_id}`)
      const p2tag = document.getElementById(`p2_${poster_id}`)
      
      ptag.style.display = 'block'
      p2tag.style.display = 'block'

      axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
      axios.defaults.xsrfCookieName = 'csrftoken'
      axios.defaults.xsrfHeaderName = 'X-CSRFToken'
  
      axios.post(`/movies/show/${poster_id}/`)
      .then((response) => {
        
        document.getElementById(`p2_${poster_id}`).innerText = `⭐ ${response.data.avg_rating}`
        document.getElementById(`p_${poster_id}`).innerText = `😍 ${response.data.like_count}`
      })
      .catch((error) => {console.log(error)})

    }

  })

  htag.addEventListener("mouseout", (e) => {
    const poster_id = e.target.dataset.id
    
    e.target.style.opacity=1
    if (poster_id) {
      const ptag3 = document.getElementById(`p_${poster_id}`)
      const ptag4 = document.getElementById(`p2_${poster_id}`)
      
      ptag3.style.display = 'none'
      ptag4.style.display = 'none'
  
      axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
      axios.defaults.xsrfCookieName = 'csrftoken'
      axios.defaults.xsrfHeaderName = 'X-CSRFToken'
  
      axios.post(`/movies/show/${poster_id}/`)
      .then((response) => {
        
        document.getElementById(`p2_${poster_id}`).innerText = `⭐ ${response.data.avg_rating}`
        document.getElementById(`p_${poster_id}`).innerText = `😍 ${response.data.like_count}`
      })
      .catch((error) => {console.log(error)})

    }
  })
  // poster.addEventListener("mouseout")
})

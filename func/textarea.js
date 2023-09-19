const textareaResize = () => {
    document.querySelectorAll('textarea').forEach( element => {
      element.style.height = `${element.scrollHeight}px`;
      element.addEventListener('input', event => {
        event.target.style.height = 'auto'; 
        event.target.style.height = `${event.target.scrollHeight}px`;
        console.log(event.target.style.height);
        })
    });
  } 

export default textareaResize;
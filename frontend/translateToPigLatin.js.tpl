var formEl = document.getElementById('translateToPigLatinForm');

formEl.addEventListener('submit', event => {
    event.preventDefault();

    const textToTranslate = formEl[0].value
    const content = {engText: textToTranslate};

    const url = {TRANS_URL}
    const fetchOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(content)
      }

    fetch(url, fetchOptions)
      .then(response => {
        return response.json();
      })
      .then(data => {
        document.getElementById('piglatinText').value = data["translation"];
      })
      .catch(error => {
        console.log('Request failed', error);
      });
})


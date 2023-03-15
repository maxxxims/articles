const requestURL = 'http://127.0.0.1:5000/predict_category'
    function sendRequest(method, url, body = null) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest()

        xhr.open(method, url)

        xhr.responseType = 'json'
        xhr.setRequestHeader('Content-Type', 'application/json')

        xhr.onload = () => {
        if (xhr.status >= 400) {
            reject(xhr.response)
        } else {
            resolve(xhr.response)
        }
        }

        xhr.onerror = () => {
        reject(xhr.response)
        }

        xhr.send(JSON.stringify(body))
    })
    }

    function write(data){
        

        var el = document.getElementById('input');
        if (data['msg'] == "ok"){
            el.innerHTML = "IT is a text";
        }
        else{
            el.innerHTML = "IT is not a text";
        }
       el.innerHTML = data['category'] 
       $("#result").show();
    }

    function sendGet(){
        sendRequest('GET', requestURL)
        .then(data => write(stringify(data)))
        .catch(err => console.log(err))
    }
    
    function sendPOST(){
        var article_title = document.getElementById('article-title').value;
        var article_text = document.getElementById('article-text').value;
        console.log(article_title + article_text);
        const body = {
    title: article_title,
    text: article_text
    }

    sendRequest('POST', requestURL, body)
    .then(data => write(data))
    .catch(err => console.log(err))
    }

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
            el.innerHTML = data['category'] 
            $("#result").show();
        }
        else{
            el.innerHTML = "IT is not a text";
        }
       
    }

    function sendGet(){
        sendRequest('GET', requestURL)
        .then(data => write(stringify(data)))
        .catch(err => console.log(err))
    }
    
    function predictCategory(URL){
        var article_title = document.getElementById('article-title').value;
        var article_text = document.getElementById('article-text').value;
        console.log(article_title + article_text);
        const body = {
                        title: article_title,
                        text: article_text
                    }
    sendRequest('POST', URL, body)
    .then(data => write(data))
    .catch(err => console.log(err))
    }
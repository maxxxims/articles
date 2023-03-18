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
        if (data['status'] == 200){
            el.innerHTML = data['category'] 
            $("#result").show();
        }
        else{
            el.innerHTML = "IT is not a text";
        }
       
    }

    function write_media(data){
        var el = document.getElementById('input-2');
        if (data['status'] == 200){
            el.innerHTML = "This is <b>" + data['category'] + "</b> Media";
            $("#result-2").show();
        }
        else{
            el.innerHTML = "Media not found"
            $("#result-2").show();
        }
       
    }

    function write_media_table(data){
        var el = document.getElementById('input-3');
        
        table = document.getElementById('input-table');
        table.innerHTML = "";
        el.innerHTML = "";
        
        if (data['status'] == 200){
            let thead = document.createElement('thead');
            let tbody = document.createElement('tbody');

            let row_1 = document.createElement('tr');
            let heading_1 = document.createElement('th');
            heading_1.innerHTML = "Type";
            let heading_2 = document.createElement('th');
            heading_2.innerHTML = "Value";

            row_1.appendChild(heading_1);
            row_1.appendChild(heading_2);
            thead.appendChild(row_1);  

            for (key in data['data']){
                let row_2 = document.createElement('tr');
                let row_2_data_1 = document.createElement('td');
                // row_2_data_1.setAttribute("id", "right");
                row_2_data_1.innerHTML = key;
                let row_2_data_2 = document.createElement('td');
                row_2_data_2.innerHTML = data['data'][key];

                row_2.appendChild(row_2_data_1);
                row_2.appendChild(row_2_data_2);
                tbody.appendChild(row_2);
            }
            document.getElementById('input-table').appendChild(thead);
            document.getElementById('input-table').appendChild(tbody);
            $("#result-3").show();
        }
        else{
            el.innerHTML = "Media not found"
            $("#result-3").show();
        }
       
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


    function predictMedia(URL){
        var media_site = document.getElementById('media-1').value;
        const body = {
                media: media_site,
                    }
    sendRequest('POST', URL, body)
    .then(data => write_media(data))
    .catch(err => console.log(err))
    }


    function predictMediaProfile(URL){
        var media_site = document.getElementById('media-2').value;
        const body = {
                media: media_site,
                    }
    sendRequest('POST', URL, body)
    .then(data => write_media_table(data))
    .catch(err => console.log(err))
    }
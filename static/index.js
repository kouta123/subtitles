document.getElementById("img_file").onchange = sendFile

function sendFile(){
    let form = document.getElementById("file-name");
    form.submit()
}
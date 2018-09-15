folders = []

var ipVAL = "10.10.1.112:8000"


$('#folderList').ready((e) => {
    // alert("Hello world")
    HTTP = new XMLHttpRequest()
    HTTP.open("GET", 'http://'+ ipVAL + '/getfolders', true) // 
    HTTP.send()
    HTTP.onreadystatechange = (e) => {
        if (HTTP.readyState === 4) {
            if( HTTP.status === 200) {
                folders = JSON.parse(HTTP.responseText)
                console.log(folders)
                for(i = 0; i < folders.length; i++) {
                    $('#folderList').append("<li class=\"list-group-item noselect " + folders[i][1] + "\" data-folder-num=\"" + i + "\">"+folders[i][0]+"</li>")
                }
                console.log()
            }
            else {
                console.log("something went wrong")
            }
        }
    }
})

$(document).on('click', '.list-group-item',function() {
    if ($(this).hasClass('active')) {
        $(this).removeClass('active').addClass("disabled")
        console.log("Should add")
        folderRevoke($(this).data("folder-num"), 'H2CmE81MStvEw5pkoHDkKnkpxWeGj3sam')
    }   
    else {
        $(this).removeClass('disabled').addClass('active')
        console.log("Should remove")

        folderAdd($(this).data("folder-num"), 'H2CmE81MStvEw5pkoHDkKnkpxWeGj3sam')
    }
})

function folderAdd(folderIndex, targetAddress) {
    folderNum = "" + folderIndex
    for (var i = folderNum.length; i < 4; i++) { folderNum = "0" + folderNum }
    folderNum += "0002"
    $.get('http://'+ ipVAL + '/sendtx?amount='+folderNum)
}

function folderRevoke(folderIndex, targetAddress) {
    folderNum = "" + folderIndex
    for (var i = folderNum.length; i < 4; i++) { folderNum = "0" + folderNum }
    folderNum += "0001"
    $.get('http://'+ ipVAL + '/sendtx?amount='+folderNum)
}
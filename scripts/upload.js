document.getElementById('file1').addEventListener('change', function() {
    document.getElementById('file1Button').textContent = 'File selected: ' + this.files[0].name;
});

document.getElementById('file2').addEventListener('change', function() {
    document.getElementById('file2Button').textContent = 'File selected: ' + this.files[0].name;
});

function uploadFiles() {
    const formData = new FormData(document.getElementById('uploadForm'));
    fetch('http://127.0.0.1:5700/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').textContent = data.message + ". Download the output file: " + data.output_file;
    })
    .catch(error => {
        document.getElementById('message').textContent = "An error occurred: " + error.message;
    });
}

document.getElementById('fileInput').addEventListener('change', function() {
    alert('文件已选择');
});

function async_data() {
    async_map_data();
    async_chart_2_data();
    // 定时从服务器更新数据
    setTimeout(async_data, 1000);
}

$(document).ready(function () {
    async_data();
});

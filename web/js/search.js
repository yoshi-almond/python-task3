document.addEventListener('DOMContentLoaded',() => {
    document.getElementById('search-btn').addEventListener('click',log);
});

const log = () => {
    let search_word = document.getElementById("search-field").value;
    let csv_file_name = document.getElementById("csv-file-name").value;
    if(search_word === ""){
        window.alert("何も入力されていません");
    }else{
        const search = async () => {
            let res = await eel.py_search(search_word,csv_file_name)();
            let text_area = document.getElementById("log-field");
            if(res == 0){
                window.alert("ファイルが存在しません");
            }else if(res == 1){
                text_area.value += `${search_word}は見つかりました\n`;
            }else if(res == 2){
                text_area.value += `${search_word}は見つかりませんでした\n`;
                text_area.value += `${search_word}を追加しました\n`;
            }
        };
        search(); 
    };
};
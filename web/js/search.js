document.addEventListener('DOMContentLoaded',() => {
    document.getElementById('search-btn').addEventListener('click',log);
});

const log = () => {
    let search_word = document.getElementById("search-field").value;
    if(search_word === ""){
        window.alert("何も入力されていません");
    }else{
        const search = async () => {
            let res = await eel.py_search(search_word)();
            let text_area = document.getElementById("log-field");
            text_area.value += "追加\n";
            /* if(res){
                text_area.value += `${search_word}は見つかりました\n`;
            }else{
                text_area.value += `${search_word}は見つかりませんでした\n`;
                text_area.value += `${search_word}を追加しました\n`;
            } */
        };
        search(); 
    };
};
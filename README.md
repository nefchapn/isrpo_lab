# **Волков Игорь м3101**
## My-first-plugin: cppSearch

**Работа плагина:** Плагин добавляет команду, которая берет выделенный текст в редакторе и открывает страницу с его описанием на сайте cppreference.com в браузере.

<br>

## Пошаговый алгоритм
**1.** Плагин проверяет, открыт ли файл.
<br>
>>const editor = vscode.window.activeTextEditor;
>>
>>if (!editor) {
>>	vscode.window.showInformationMessage('No active editor found.');
>>	return;
>>}
<br>

**2.** Берет выделенный текст или предупреждает, если ничего не выделено.
>>let searchText = editor.document.getText(editor.selection);
>>if (!searchText) {
>>    vscode.window.showWarningMessage('️ Выделите текст с названием функции/класса');
>>     return;
>>}
<br>

**3.** Превращает текст в нормальную ссылку.
>>const url = `https://en.cppreference.com/w/index.php?search=${encodeURIComponent(searchText)}`;
<br>

**4.** Открывает эту ссылку в обычном браузере.
>>vscode.env.openExternal(vscode.Uri.parse(url));
<br>
<br>

[Пример работы при выделении vector](https://en.cppreference.com/w/index.php?search=vector)




**Enjoy!**

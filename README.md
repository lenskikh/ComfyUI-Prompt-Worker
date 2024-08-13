# Prompt Worker

![Screenshot](/workflows/scr.png)

### [English]

The multifunctional node optimizes the prompt by performing the following tasks:

1. Eliminate duplicates, ensuring the uniqueness of each element.
2. Alphabetical ordering (if the corresponding setting is activated).
3. Removing lore names, keeping the prompt clean and concise.
4. Using a blacklist to filter unwanted content.
5. Selective removal of individual characters.
6. Unlimited multi-swap of tokens. Reduces complex circuits.

To fine-tune the removal function, the user can specify unwanted characters and words, separated by commas. This allows you to fine-tune the process of cleaning and formatting the prompt.

Workflow can be found in the workflows directory

A small feature: put a dash in the token and you will temporarily disable it.

Update from August 13:
* All tokens are converted to lower case, that is, BW and bw are the same thing for the plugin.
* Added a new scheme in the workflows directory. It cleans the prompt before generation.
* Added word replacement function. In the blacklist, write the word you want to replace, then put a vertical line followed by the token that you want to see in the prompt. For example, <code>sea|beach with palms</code> sea will be replaced with beach with palms
* Fixed a bug with lore names not being deleted. Now deletes in 100% of cases.

### Installation

1. Go to the custom_nodes directory
2. Write cmd in explorer
3. In cmd write git clone https://github.com/lenskikh/ComfyUI-Prompt-Worker.git

### [Russian]

Многофункциональная нода оптимизирует промпт, выполняя следующие задачи:

1. Устранение дубликатов, обеспечивая уникальность каждого элемента.
2. Алфавитное упорядочивание (при активации соответствующей настройки).
3. Удаление названий лор, сохраняя чистоту и лаконичность промпта.
4. Применение черного списка для фильтрации нежелательного контента.
5. Избирательное удаление отдельных символов. 
6. Неограниченная мультизамена токенов. Сокращает сложные схемы.

Для точной настройки функции удаления, пользователь может указать нежелательные символы и слова, разделяя их запятыми. Это позволяет тонко контролировать процесс очистки и форматирования промпта.

Воркфлоу можете найти в директории workflows

Небольшая фича, поставьте знак тире - в токене и вы его временно отключите.

Обновление от 13 августа: 
* Все токены конвертируются в нижний регистр, то есть BW и bw - это одно и тоже для плагина.
* Добавлена новая схема в директории workflows. Она чистит промпт перед генерацией.
* Добавлена функция замены слов. В blacklist пишите слово, которое хотите заменить, затем ставите вертикальную черту после которой идёт токен, который вы хотите видеть в промпте. Например <code>sea|beach with palms</code> sea заменится на beach with palms
* Исправлен баг с неудалением названий лор. Теперь удаляет в 100% случаев.

### Установка

1. Зайдите в директорию custom_nodes
2. Напишите cmd в проводнике
3. В cmd напишите git clone https://github.com/lenskikh/ComfyUI-Prompt-Worker.git



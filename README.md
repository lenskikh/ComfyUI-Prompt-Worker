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

Updated June 30, 2025:
* Disabling lore is now optional. Conversion to lowercase is also optional. Made at the request of the user.

Updated June 28, 2025:
* Fixed a bug with alphabetical sorting that occurred due to new nodes

Updated June 27, 2025:
* Added styles: weather, photographic style, cinematic style
* Added a new diagram to the workflows folder that shows how you can combine translation and handwritten prompts

Updated June 25, 2025
* Minor update. Add scheme with translator node.

Updated July 10, 2025:
* Style settings are completely moved to external files. You can now edit the lists yourself

Updated July 11, 2025:
* Two separate nodes were created. One for styles, the second for clothes. Now three nodes. The first node is the main one, it removes duplicates, sorts alphabetically, replaces tokens, removes tokens from the blacklist. The second node and the third node are optional. The second one is responsible for styles. The third one is responsible for the type of clothing. The lists are located in external files in the settings directory.

Updated July 12, 2025:
* Added new node "body", you can choose body type, hairstyle, makeup and etc.

Updated July 14, 2025:
* Added a node that combines prompts from other nodes. This node has 4 inputs and automatically puts a comma at the end of the prompt.
![Screenshot](/workflows/merge.png)

* Added a custom list, the user can modify it in the file custom_list.json
![Screenshot](/workflows/custom.png)

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

Обновление от 30 июня 2025:
* Отключение лоры теперь опционально. Конверсия в нижний регистр тоже опционально. Сделано по просьбе пользователя.

Обновление от 28 июня 2025:
* Исправлен баг с алфавитной сортировкой, который возник из-за новых нод

Обновление от 27 июня 2025:
* Добавлены стили: погода, фотографический стиль, кинематографический стиль
* В папке workflows добавлена новая схема, которая показывает, как можно объеденить перевод и собственноручный промпт

Обновление от 25 июня 2025:
* Небольшое обновление. Добавлена схема, где присувствует нода автоматического перевода. 

Обновление от 10 июля 2025:
* Настройки стилей полностью вынесены во внешние файлы. Вы теперь сами можете редактировать списки. Находится в директории settings

Обновление от 11 июля 2025:
* Были созданы две отдельные ноды. Одна по стилям, вторая по одежде. Теперь три ноды. Первая нода основная убирает дубликаты, сортирует по алфавиту, заменяет токены, убирает токены из черного списка. Вторая нода конструирует стили. Вторая отвечает за стили. Третья за тип одежды. Списки находятся во внешних файлах в директории settings.

Обновление от 12 июля 2025:
* Добавлена новая нода "тело", вы можете выбрать телосложение, прическу, макияж и так далее.

Обновление от 14 июля 2025:
* Добавлена нода, которая объядиняет промпты с других нод. Эта нода имеет 4 входа и автоматически ставит запятую в конце промпта. 
![Screenshot](/workflows/merge.png)

* Добавлен пользовательский список, пользователь может сам модифировать его в файле custom_list.json
![Screenshot](/workflows/custom.png)

### Установка

1. Зайдите в директорию custom_nodes
2. Напишите cmd в проводнике
3. В cmd напишите git clone https://github.com/lenskikh/ComfyUI-Prompt-Worker.git



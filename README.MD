# Helper class views

```python
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
```

## GIT

- `git init` - инициализация репозитория локально (1 раз на проект)
- `git status` - состояние репозитория и файлов 

### Добавление к отслеживанию

`git add <filename> / <dirname>` - добавить файл или папку

`git add .` или `git add -A` - добавить текущий каталог и все файлы

### Откатиться к комиту *

`git checkout 519b354b032cd64fc2e3ce123490ce694c34 ` - откатиться к комиту

`git switch -c work_code` - создали ветку от несломанного комита

```
git reset --hard <commit> - все изменения после комита уделаны
git reset --soft 
git reset --mixed 
```

### Работа с ветками 

- `git branch` - посмотреть ветки 
- `git checkout master` - перейти на ветку
- `git checkout -b new` - создание ветки
- `git merge name_branch` - мердж (слияние) ветки `name_branch` в текущую 


### Удаленный сервер

- `git pull` - стянуть с сервера себе
- `git push` - залить на сервер

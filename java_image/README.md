# Техническое задание

## Сrop-crop-resize-resize
В качестве задания предлагается выполнить проект «crop-crop». Эта утилита позволит ресайзить изображение для остальных сервисов МТС: изменение изображений рекламных баннеров, превью для альбомов и обложки фильмов в маленьком разрешении и другие.

## Используемые технологии
- Код приложения пишется на Java.
- Библиотеки, которые можно использовать:
    - Работа с консольными параметрами [picocli.info](https://picocli.info/).
    - Работа с изображением [thumbnailator](https://github.com/coobird/thumbnailator). Рекомендуем взять из неё функции обрезки  и изменения параметров картинки.
    - Библиотека для работы с изображениями и видео [marvin project](https://github.com/gabrielarchanjo/marvin-framework). Рекомендуем взять из неё  [GaussianBlur](http://marvinproject.sourceforge.net/en/plugins/gaussianBlur.html) и [Crop](http://marvinproject.sourceforge.net/en/plugins/crop.html).
    - Библиотека, необходимая для запуска тестов [junit5](https://github.com/junit-team/junit5).

## Интерфейс взаимодействия
```
Version: name version https://gitlab.com/link/
Available formats: jpeg png
Usage: convert input-file [options ...] output-file
Options Settings:
  --resize width height       resize the image
  --quality value             JPEG/PNG compression level
  --crop width height x y     cut out one rectangular area of the image
  --blur {radius}             reduce image noise detail levels 
  --format "outputFormat"     the image format type
```

## Описание параметров

**--resize width height** — уменьшает, увеличивает картинку или задает необходимый размер для изображения. [Пример в документации](https://imagemagick.org/script/command-line-options.php#resize).

**--quality value** — задает уровень сжатия файлов JPEG / PNG. Форматы изображений могут быть JPEG и PNG, качество от 1 (самое низкое качество изображения и самое высокое сжатие) до 100 (лучшее качество, но наименее эффективное сжатие). [Пример в документации](https://imagemagick.org/script/command-line-options.php#quality).

**--crop width height x y** —  Вырезает прямоугольную область изображения. Обработанное изображения должно иметь ширину (**width**) и высоту (**height**). Точка отсчета задаётся значениями **x** и **y.** [Пример из документации](https://imagemagick.org/script/command-line-options.php#crop).

**--blur radius** — добавляет размытие. [Пример в документации](https://imagemagick.org/script/command-line-options.php#blur).

**--format "outputFormat"** — конвертирует изображение в "outputFormat". Параметр "outputFormat" может быть JPEG / PNG. [Пример в документации](https://imagemagick.org/script/command-line-options.php#format).

Валидация входных параметров должна быть реализована. 

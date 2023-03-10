# imageFilesInfoReader
A GUI application, developed in Python, that outputs meta-information(size(in px), dpi, color depth, compression) about graphic files in a specified folder. Developed as part of the second laboratory work on the discipline Computer Graphics.
![image](https://user-images.githubusercontent.com/79499100/223454129-75362a8f-c85b-48c4-ad61-99583f68ea2d.png)

## build and run
- To run with Python interpreter open CMD in root project folder and run: ```python main.py``` (make sure that the interpreter is added to the environment variables)
- To build and run executable file you need:
  - install <b>pyinstaller</b>: ```pip install pyinstaller```
  - open CMD in root folder and run: ```pyinstaller --windowed -F --add-data "pics/seo.ico;pics" --icon=pics/seo.ico -d bootloader main.py --name inspect_images --onefile``` in Windows or ```pyinstaller --windowed -F --add-data "pics/seo.ico:pics" --icon=pics/seo.ico -d bootloader main.py --name inspect_images --onefile``` in Unix systems
  - after that you can find one-file executable <b>inspect_images</b> in <b>dist</b> folder and excecute it.

Built one-file executable <b>inspect_images.exe</b> (Windows) is altready in the repository.

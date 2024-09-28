[Setup]
AppName=SuperNotepad
AppVersion=1.0
DefaultDirName={pf}\SuperNotepad
DefaultGroupName=SuperNotepad
OutputDir=.
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes
Uninstallable=yes

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "notepad.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\SuperNotepad"; Filename: "{app}\main.exe"; IconFilename: "{app}\notepad.ico"
Name: "{userdesktop}\SuperNotepad"; Filename: "{app}\main.exe"; Tasks: desktopicon; IconFilename: "{app}\notepad.ico"
Name: "{group}\Удалить SuperNotepad"; Filename: "{app}\uninstall.exe"; IconFilename: "{app}\notepad.ico"

[Tasks]
Name: "desktopicon"; Description: "Создать иконку на рабочем столе"; GroupDescription: "Дополнительные задачи"

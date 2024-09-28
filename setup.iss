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
Source: "dist\SupeR_notepad.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "notepad.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Super Notepad"; Filename: "{app}\SupeR_notepad.exe"; IconFilename: "{app}\notepad.ico"
Name: "{userdesktop}\Super Notepad"; Filename: "{app}\SupeR_notepad.exe"; Tasks: desktopicon; IconFilename: "{app}\notepad.ico"
Name: "{group}\Удалить Super Notepad"; Filename: "{app}\uninstall.exe"; IconFilename: "{app}\notepad.ico"

[Tasks]
Name: "desktopicon"; Description: "Создать иконку на рабочем столе"; GroupDescription: "Дополнительные задачи"

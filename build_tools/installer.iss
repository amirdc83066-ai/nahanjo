#define MyAppName "Nahanjo"
#define MyAppVersion "1.0"
#define MyAppPublisher "Nahanjo Project"
#define MyAppExeName "Nahanjo.exe"

[Setup]
AppId={{A2B8E3D4-9F31-4E6B-9A52-7C3A1F5B8D21}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=C:\anomaly_ai_analyzer\installer_output
OutputBaseFilename=Nahanjo_Setup
SetupIconFile="C:\anomaly_ai_analyzer\ui\logo.ico"
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "persian"; MessagesFile: "C:\anomaly_ai_analyzer\Persian.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create Desktop Icon"; GroupDescription: "Additional Icons:"; Flags: unchecked

[Files]
; --- EXE ---
Source: "C:\anomaly_ai_analyzer\dist\Nahanjo.exe"; DestDir: "{app}"; Flags: ignoreversion

; --- UI files ---
Source: "C:\anomaly_ai_analyzer\ui\about.ui"; DestDir: "{app}\ui"; Flags: ignoreversion
Source: "C:\anomaly_ai_analyzer\ui\ai_prompt.txt"; DestDir: "{app}\ui"; Flags: ignoreversion
Source: "C:\anomaly_ai_analyzer\ui\analysis_ai_page.ui"; DestDir: "{app}\ui"; Flags: ignoreversion
Source: "C:\anomaly_ai_analyzer\ui\Data_Select_Page.ui"; DestDir: "{app}\ui"; Flags: ignoreversion
Source: "C:\anomaly_ai_analyzer\ui\Intro.ui"; DestDir: "{app}\ui"; Flags: ignoreversion
Source: "C:\anomaly_ai_analyzer\ui\result_core.ui"; DestDir: "{app}\ui"; Flags: ignoreversion
Source: "C:\anomaly_ai_analyzer\ui\ui_app.py"; DestDir: "{app}\ui"; Flags: ignoreversion
Source: "C:\anomaly_ai_analyzer\ui\Vazir.ttf"; DestDir: "{app}\ui"; Flags: ignoreversion
Source: "C:\anomaly_ai_analyzer\ui\logo.ico"; DestDir: "{app}\ui"; Flags: ignoreversion

; --- App packages (Only folders with files) ---
Source: "C:\anomaly_ai_analyzer\core\*"; DestDir: "{app}\core"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\anomaly_ai_analyzer\ai_layer\*"; DestDir: "{app}\ai_layer"; Flags: ignoreversion recursesubdirs createallsubdirs

[Dirs]
; این بخش پوشه data را می‌سازد حتی اگر خالی باشد
Name: "{app}\data"

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Run {#MyAppName}"; Flags: nowait postinstall skipifsilent

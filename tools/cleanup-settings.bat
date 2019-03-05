:: cleanup settings
::
:: UNDER development 
::
@echo OFF
setlocal

set HERE=%~dp0
set REPODIR=%HERE%..\

set SETTINGSPATH="%REPODIR%\.vscode\settings.json"
type %SETTINGSPATH% | python -m json.tool --sort-keys > %HERE%workspace-settings.json
:: TODO this should update %SETTINGSPATH%

set SETTINGSPATH="%APPDATA%\Code\User\settings.json"
type %SETTINGSPATH% | python -m json.tool --sort-keys > %HERE%user-settings.json

# Paths to you django's root and to the project itself
$djangoroot = "<Path to the ENV>"
$djangoproject = "Path to the project"
# Functional variables
$activatevenv = ".\Scripts\activate"
$rundjangoserver = ".\manage.py runserver"

# Venv activation and server start process
Write-Host "Locating and activating a virtual enviroment..."
Set-Location $djangoroot; 
Get-ChildItem; 
Invoke-Expression $activatevenv;
Write-Host "Virtual enviroment activated. Now starting the server..."
Set-Location $djangoproject;
Get-ChildItem;
Invoke-Expression $rundjangoserver;


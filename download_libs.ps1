$libsDir = "C:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\libs"
if (-not (Test-Path $libsDir)) {
    New-Item -ItemType Directory -Path $libsDir -Force | Out-Null
}

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$pdfLibUrl = "https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"
$pdfLibPath = "$libsDir\pdf-lib.min.js"
if (-not (Test-Path $pdfLibPath)) {
    Write-Output "Downloading pdf-lib.min.js..."
    Invoke-WebRequest -Uri $pdfLibUrl -OutFile $pdfLibPath -UseBasicParsing
}

$pdfJsUrl = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"
$pdfJsPath = "$libsDir\pdf.min.js"
if (-not (Test-Path $pdfJsPath)) {
    Write-Output "Downloading pdf.min.js..."
    Invoke-WebRequest -Uri $pdfJsUrl -OutFile $pdfJsPath -UseBasicParsing
}

$pdfJsWorkerUrl = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js"
$pdfJsWorkerPath = "$libsDir\pdf.worker.min.js"
if (-not (Test-Path $pdfJsWorkerPath)) {
    Write-Output "Downloading pdf.worker.min.js..."
    Invoke-WebRequest -Uri $pdfJsWorkerUrl -OutFile $pdfJsWorkerPath -UseBasicParsing
}

Write-Output "All libraries downloaded successfully to $libsDir"
Get-ChildItem $libsDir | Select-Object Name, Length

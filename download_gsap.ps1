$libsDir = "C:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\libs"
$gsapPath = "$libsDir\gsap.min.js"
if (-not (Test-Path $gsapPath)) {
    Write-Output "Downloading gsap.min.js..."
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Invoke-WebRequest -Uri "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" -OutFile $gsapPath -UseBasicParsing
    Write-Output "GSAP downloaded successfully to $gsapPath"
} else {
    Write-Output "GSAP already exists"
}

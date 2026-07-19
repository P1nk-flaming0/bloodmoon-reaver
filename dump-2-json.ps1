$basePath = Join-Path (Get-Location).Path "PF#werefighter"
$folders = @("spl", "itm", "cre", "eff")

foreach ($folder in $folders) {
    $fullPath = Join-Path $basePath $folder
    if (Test-Path -LiteralPath $fullPath) {
        Write-Host "Processing folder: $fullPath"
        # Uses npx to ensure it hits your local node_modules installation
        npx fgbin "$fullPath" -r --save
    }
}
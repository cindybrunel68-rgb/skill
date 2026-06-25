$ErrorActionPreference = 'Stop'
$repoPath = 'C:\Users\legue\Downloads\mon aios\template-aios-local-v1-main'
$logPath = Join-Path $repoPath 'data\backup_log.txt'

Set-Location $repoPath

$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
Add-Content -Path $logPath -Value "$timestamp - backup started"

try {
    git status --porcelain > $null
    $hasChanges = (git status --porcelain).Trim() -ne ''

    if (-not $hasChanges) {
        Add-Content -Path $logPath -Value "$timestamp - no changes to backup"
        exit 0
    }

    git add .
    git commit -m "Daily backup $timestamp" -q
    git push origin main
    Add-Content -Path $logPath -Value "$timestamp - backup completed"
}
catch {
    Add-Content -Path $logPath -Value "$timestamp - backup failed: $($_.Exception.Message)"
    throw
}

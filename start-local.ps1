# start-local.ps1
# Opens two PowerShell windows: one running the mock Kepware server, the other running the poller.

param(
    [string]$PythonExe = "python",
    [switch]$NoNewWindows
)

function Start-WindowedProcess($command, $title) {
    # Open a new PowerShell window and run the command
    Start-Process powershell -ArgumentList ("-NoExit","-Command","Write-Host \"$title\"; $command")
}

Write-Host "Starting local test environment..."

$mockCmd = "$PythonExe ./mock_kepware.py"
$pollCmd = "$PythonExe ./poll_kepware.py"

if ($NoNewWindows) {
    # Run mock in background job and poller in current shell
    Write-Host "Starting mock server as background job..."
    Start-Job -ScriptBlock { param($py) & $py ./mock_kepware.py } -ArgumentList $PythonExe | Out-Null
    Write-Host "Starting poller in current window..."
    iex $pollCmd
} else {
    Start-WindowedProcess $mockCmd "Mock Kepware"
    Start-WindowedProcess $pollCmd "Poll Kepware"
    Write-Host "Started mock server and poller in new windows."
}

Write-Host "To stop the mock server job (if run as job), use: Get-Job | Stop-Job; Get-Job | Remove-Job"

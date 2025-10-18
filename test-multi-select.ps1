# Test script for Turbo Delete multi-selection support
Write-Host "Testing Turbo Delete multi-selection support..." -ForegroundColor Cyan

# Create test directories
$testDir1 = "test-folder-1"
$testDir2 = "test-folder-2"
$testFile1 = "test-file-1.txt"
$testFile2 = "test-file-2.txt"

Write-Host "Creating test files and directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Path $testDir1 -Force | Out-Null
New-Item -ItemType Directory -Path $testDir2 -Force | Out-Null
New-Item -ItemType File -Path $testFile1 -Force | Out-Null
New-Item -ItemType File -Path $testFile2 -Force | Out-Null

# Add some content to test directories
New-Item -ItemType File -Path "$testDir1\file1.txt" -Force | Out-Null
New-Item -ItemType File -Path "$testDir2\file2.txt" -Force | Out-Null

Write-Host "Test files created:" -ForegroundColor Green
Write-Host "  - $testDir1" -ForegroundColor White
Write-Host "  - $testDir2" -ForegroundColor White
Write-Host "  - $testFile1" -ForegroundColor White
Write-Host "  - $testFile2" -ForegroundColor White

Write-Host "`nTo test multi-selection context menu:" -ForegroundColor Cyan
Write-Host "1. Select multiple files/folders in File Explorer" -ForegroundColor White
Write-Host "2. Right-click and look for 'Turbo Delete' option" -ForegroundColor White
Write-Host "3. The context menu should now appear for multiple selections!" -ForegroundColor White

Write-Host "`nTo test command line multi-selection:" -ForegroundColor Cyan
Write-Host "Run: td.exe `"$testDir1`" `"$testDir2`" `"$testFile1`" `"$testFile2`"" -ForegroundColor White

Write-Host "`nPress any key to clean up test files..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Clean up
Remove-Item -Path $testDir1 -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path $testDir2 -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path $testFile1 -Force -ErrorAction SilentlyContinue
Remove-Item -Path $testFile2 -Force -ErrorAction SilentlyContinue

Write-Host "Test files cleaned up!" -ForegroundColor Green

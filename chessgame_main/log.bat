$path
$date = get-date -format "yyyy-MM-dd-HH-mm"
$file = ("Log_" + $date + ".log")
$logfile = $path + "\" + $file

function Write-Log([string]$logtext, [int]$level=0)
{
	$logdate = get-date -format "yyyy-MM-dd HH:mm:ss"
	if($level -eq 0)
	{
		$logtext = "[INFO] " + $logtext
		$text = "["+$logdate+"] - " + $logtext
		Write-Host $text
	}
	if($level -eq 1)
	{
		$logtext = "[WARNING] " + $logtext
		$text = "["+$logdate+"] - " + $logtext
		Write-Host $text -ForegroundColor Yellow
	}
	if($level -eq 2)
	{
		$logtext = "[ERROR] " + $logtext
		$text = "["+$logdate+"] - " + $logtext
		Write-Host $text -ForegroundColor Red
	}
	$text >> $logfile
}

# log something
Write-Log "this is a simple log test"

# create warning log entry
Write-Log "this is a simple log test" 2

# use more than simple variables in a string
$cmds = get-command
Write-Log "there are $($cmds.count) commands available"
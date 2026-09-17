$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

function Write-JsonRpcResponse {
    param($Response)
    $json = $Response | ConvertTo-Json -Depth 10 -Compress
    [Console]::Out.WriteLine($json)
    [Console]::Out.Flush()
}

while ($true) {
    $line = [Console]::In.ReadLine()
    if ($null -eq $line) { break }
    if ([string]::IsNullOrWhiteSpace($line)) { continue }

    try {
        $request = $line | ConvertFrom-Json
    } catch {
        continue
    }

    $id = $request.id
    $method = $request.method

    switch ($method) {
        'initialize' {
            $result = @{
                protocolVersion = '2024-11-05'
                capabilities    = @{ tools = @{} }
                serverInfo      = @{ name = 'echo-windows'; version = '1.0.0' }
            }
            Write-JsonRpcResponse @{ jsonrpc = '2.0'; id = $id; result = $result }
        }
        'notifications/initialized' {
            # notification, no response expected
        }
        'tools/list' {
            $result = @{
                tools = @(
                    @{
                        name        = 'echo'
                        description = 'Echoes back the provided text.'
                        inputSchema = @{
                            type       = 'object'
                            properties = @{
                                text = @{ type = 'string'; description = 'Text to echo back.' }
                            }
                            required   = @('text')
                        }
                    },
                    @{
                        name        = 'reverse'
                        description = 'Reverses the provided text.'
                        inputSchema = @{
                            type       = 'object'
                            properties = @{
                                text = @{ type = 'string'; description = 'Text to reverse.' }
                            }
                            required   = @('text')
                        }
                    },
                    @{
                        name        = 'uppercase'
                        description = 'Converts the provided text to uppercase.'
                        inputSchema = @{
                            type       = 'object'
                            properties = @{
                                text = @{ type = 'string'; description = 'Text to uppercase.' }
                            }
                            required   = @('text')
                        }
                    },
                    @{
                        name        = 'get_time'
                        description = 'Returns the current local date and time.'
                        inputSchema = @{
                            type       = 'object'
                            properties = @{}
                        }
                    },
                    @{
                        name        = 'calculate'
                        description = 'Performs a basic arithmetic operation (add, subtract, multiply, divide) on two numbers.'
                        inputSchema = @{
                            type       = 'object'
                            properties = @{
                                a         = @{ type = 'number'; description = 'First operand.' }
                                b         = @{ type = 'number'; description = 'Second operand.' }
                                operation = @{ type = 'string'; description = 'One of: add, subtract, multiply, divide.'; enum = @('add', 'subtract', 'multiply', 'divide') }
                            }
                            required   = @('a', 'b', 'operation')
                        }
                    }
                )
            }
            Write-JsonRpcResponse @{ jsonrpc = '2.0'; id = $id; result = $result }
        }
        'tools/call' {
            $toolName = $request.params.name
            $toolArgs = $request.params.arguments
            $text = $toolArgs.text
            switch ($toolName) {
                'echo' {
                    $resultText = $text
                }
                'reverse' {
                    $chars = $text.ToCharArray()
                    [Array]::Reverse($chars)
                    $resultText = -join $chars
                }
                'uppercase' {
                    $resultText = $text.ToUpperInvariant()
                }
                'get_time' {
                    $resultText = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss')
                }
                'calculate' {
                    $a = [double]$toolArgs.a
                    $b = [double]$toolArgs.b
                    switch ($toolArgs.operation) {
                        'add' { $resultText = ($a + $b).ToString() }
                        'subtract' { $resultText = ($a - $b).ToString() }
                        'multiply' { $resultText = ($a * $b).ToString() }
                        'divide' {
                            if ($b -eq 0) {
                                $resultText = $null
                            } else {
                                $resultText = ($a / $b).ToString()
                            }
                        }
                        default { $resultText = $null }
                    }
                }
                default {
                    $resultText = $null
                }
            }

            if ($null -ne $resultText) {
                $result = @{
                    content = @(
                        @{ type = 'text'; text = $resultText }
                    )
                }
                Write-JsonRpcResponse @{ jsonrpc = '2.0'; id = $id; result = $result }
            } else {
                Write-JsonRpcResponse @{ jsonrpc = '2.0'; id = $id; error = @{ code = -32601; message = "Unknown tool: $toolName" } }
            }
        }
        default {
            if ($null -ne $id) {
                Write-JsonRpcResponse @{ jsonrpc = '2.0'; id = $id; error = @{ code = -32601; message = "Method not found: $method" } }
            }
        }
    }
}

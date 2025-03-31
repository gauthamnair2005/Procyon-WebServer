<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <script>
        function getUserInput() {
            const userInput = prompt("Enter a value for y:");
            if (userInput !== null) {
                document.getElementById("userInputDisplay").innerHTML = userInput;
            }
        }
    </script>
</head>
<body onload="getUserInput()">
<?lsp var x = 12 ?>
<?lsp display "<marquee><h1>Value is " + x + "</h1></marquee>" ?>
    
    <h2>User Input:</h2>
    <p id="userInputDisplay">Waiting for input...</p>
</body>
</html>
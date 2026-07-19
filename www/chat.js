// Before you read this:
// I havent done js before.

// i've gotta make sure to set this in html
var aiResponseTextField = null
var userResponseTextField = null

async function getResponseFromAfm(message) {
    if (!aiResponseTextField) {
        return
    }

    userResponseTextField.innerText = "User: " + message
    aiResponseTextField.innerText = "AI: thinking..."

    try {
        const response = await fetch(window.location.origin + "/v1/simple/getAiResponse", {
            method: 'POST',
            body: JSON.stringify({
                "message": message
            })
        });

        if (!response.ok) {
            aiResponseTextField.textContent = "SYSTEM: Error. Try again later."
        }

        var responseData = await response.json()

        aiResponseTextField.innerText = "AI: " + responseData.response
    }
    catch (error) {
        console.error(error)
        aiResponseTextField.textContent = "SYSTEM: Error. Try again later."
    }
}

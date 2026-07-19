// Before you read this:
// I havent done js before.

// i've gotta make sure to set this in html
var aiResponseTextField = null
var userResponseTextField = null
var errorBanner = null

function throwErrorBannerNew(errorMessage) {
    const text = document.getElementById("errorMessage")
    text.textContent = errorMessage

    errorBanner.style.display = 'flex'
}

function closeError() {
    errorBanner.style.display = 'none'
}

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

        var responseData = await response.json()

        if (!response.ok) {
            throwErrorBannerNew(responseData.response)
            aiResponseTextField.textContent = "AI: ..."
            return
        }

        aiResponseTextField.innerText = "AI: " + responseData.response
    }
    catch (error) {
        console.error(error)
        aiResponseTextField.textContent = "SYSTEM: Error. Try again later."
    }
}

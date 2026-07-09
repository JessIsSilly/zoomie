import apple_fm_sdk as fm
import asyncio

class appleFoundationModels():
    def __init__(self):
        self.model = fm.SystemLanguageModel()
        self.isAvailable, self.isNotAvailableReason = self.model.is_available()
        self.session = fm.LanguageModelSession()

    def getIfFoundationModelsAvailable(self) -> bool:
        return self.isAvailable

    def getFoundationModelUnavailableErrorMessage(self) -> str:
        return self.isNotAvailableReason

    def askModelAndReturnResponse(self, question: str) -> str:
        response = asyncio.run(self.session.respond(question))
        return response
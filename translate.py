# try:
#     # import translators as ts

# except:
ts = None


from translator.madlad import MADLAD400Translator as TranslationModel
class TranslatorWrapper:
    _instance = None
    _dlt_model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TranslatorWrapper, cls).__new__(cls)
            cls._madlad = TranslationModel(target_lang="en")
        return cls._instance

    @staticmethod
    def translate(chunk, lang=None, method="offline"):
        if method == "api":
            assert ts, "Please install the required libraries to use this method"
            return ts.translate_text(
                chunk,
                from_language=lang,
                to_language="en",
                translator="google",
            )
        elif method == "offline":
            return TranslatorWrapper._madlad(chunk)
        else:
            raise ValueError("Unsupported translation method")

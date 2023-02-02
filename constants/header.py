class HeaderConsts:
    CREATE_POST_BUTTON_XPATH = ".//a[@href='/create-post']"
    SIGN_OUT_BUTTON_TEXT = 'Sign Out'
    SIGN_OUT_BUTTON_XPATH = f".//button[text()='{SIGN_OUT_BUTTON_TEXT}']"
    MY_PROFILE_BUTTON_XPATH = ".//a[@href='/profile/{username}']"
    CHAT_BUTTON_XPATH = ".//*[@data-original-title='Chat']"

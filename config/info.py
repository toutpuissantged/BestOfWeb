from typing import TypedDict

class AppInfo(TypedDict):
    AppName: str
    AppScreen: str
    AppVersion: str
    AppAuthor: str
    AppEmail: str
    AppWebsite: str
    AppDescription: str
    AppCopyright: str
    AppIcon: str

class Color(TypedDict):
    Background: str
    Text: str
    Button: str
    ButtonText: str
    ButtonHover: str
    Entry: str
    EntryText: str

class Design(TypedDict):
    Color: Color
    
class Config : 

    AppInfo : AppInfo = {
        "AppName":"BEst of Web (Beta) by toutpuissantged",
        "AppScreen":"400x380",
        "AppIcon":"icon.png",
        "AppVersion":"0.0.1",
        "AppAuthor":"Nathan",
        "AppCopyright":"Copyright (c) 2020 Nathan",
        "AppLicense":"MIT",
        "AppLicenseURL":"https://opensource.org/licenses/MIT",

    }
    
    Design : Design = {
        "Color":{
            "Background":"#00232e",
            "Entry":"#00232e",
            "EntryText":"#ffffff",
            "Text":"#ffffff",
            "Button":"#004a61",
            "ButtonText":"#ffffff",
            "ButtonHover":"#ffffff",
        },
    }
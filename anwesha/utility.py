import hashlib
import uuid
import jwt
import qrcode
from django.core.files import File
from io import BytesIO
from django.core.mail import send_mail
from anwesha.settings import EMAIL_HOST_USER ,COOKIE_ENCRYPTION_SECRET
import datetime

def varification_mail(email):
    user = email
    payload = {
        'email':email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow()
    }
    token = jwt.encode(
        payload, COOKIE_ENCRYPTION_SECRET, algorithm='HS256')
    link = "https://backend.anwesha.live/campasambassador/verifyemail/"+token
    localhost_link = "http://127.0.0.1:8000/campasambassador/verifyemail/"+token
    subject = "No replay"
    body = f'''
    Hello,\n
        Please click on the link below to verify your email address for anwesha login:
         \n{link}
        \n\nThanks,
        \nTeam  Anwesha
        \n\n for testing pourposes :- {localhost_link}
    '''
    recipient_list = []
    recipient_list.append(email)
    res = send_mail(subject, body, EMAIL_HOST_USER, recipient_list)
    return res

def hashpassword(password):
    return hashlib.sha256(password.encode()).hexdigest()


def createId(prefix, length):
    """
    Utility function to create a random id of given length
    prefix : prefix of the id ( ex : "TEAM", "ANW" )
    length : length of the id excluding the prefix
    """

    id = str(uuid.uuid4()).replace("-", "")
    return prefix + id[:length]


def checkPhoneNumber(phone_number: str):
    """
    Utility function to check if the given phone number is valid or not
    """
    pass


def isemail(email_id: str):
    """
    Utility function to check if the given email id is valid or not
    """
    if "@" in email_id:
        return True
    return False


def get_anwesha_id(request):
    """
    Utility function to get the anwesha_id of the user from the cookie
    """
    token = request.COOKIES.get("jwt")
    if not token:
        return None
    try:
        payload = jwt.decode(token, "ufdhufhufgefef", algorithms="HS256")
        id = payload["id"]
        return id
    except jwt.ExpiredSignatureError:
        return None


def generate_qr(anwesha_id):
    img = qrcode.make(anwesha_id)
    blob = BytesIO()
    img.save(blob, "PNG")
    qr = File(blob, name = anwesha_id + "-qr.png")
    return qr
    # img.save(anwesha_id+".png")

def generate_jwt_token(anwesha_id):
    return anwesha_id


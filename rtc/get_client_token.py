import os
from dotenv import load_dotenv

from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant


load_dotenv()
twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_api_key_sid = os.environ.get('TWILIO_API_KEY_SID')
twilio_api_key_secret = os.environ.get('TWILIO_API_KEY_SECRET')


def get_client_token(user_pk, room_id):

    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=user_pk)
    token.add_grant(VideoGrant(room=room_id))

    return {'token': token.to_jwt().decode()}
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "XXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXXXXXXXXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+123456789", 
    from_="+0987654321",
    body="Hello World!")

print(message.sid)   # Output the message id
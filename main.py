from http.client import HTTPSConnection
from sys import stderr
from json import dumps

header_data = {
    "content-type": "application/json",
    "user-agent": "discord.com",
    "authorization": "USER ACCOUNT TOKEN",
    "host": "discord.com",
    "referer": "DISCORD CHANNEL LINK"
}


def get_connection():
    return HTTPSConnection("discord.com", 443)


def send_message(conn, channel_id, message_data):
    try:
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            print("Submitted successfully")
            pass

        else:
            stderr.write(f"HTTP received {resp.status}: {resp.reason}\n")
            pass

    except:
        stderr.write("There was an error trying to send the message\n")


def main():
    message_data = {
        "content": "MESSAGE",
        "tts": "false",
    }

    send_message(get_connection(), "CHANNEL ID", dumps(message_data))


if __name__ == '__main__':
    main()
